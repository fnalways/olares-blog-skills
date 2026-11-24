#!/usr/bin/env python3
"""Compose comparison covers with independent text, logo, card and shadow layers."""

import argparse
import base64
import json
from pathlib import Path
import xml.etree.ElementTree as ET
from compose_svg import SVG, XLINK, node, vector_asset

LAYOUTS = {
    'wide': dict(width=1800, height=600, brand=[82, 70, 190], title=[80, 282, 100, 76],
                 cards=[[1030, 133, 290], [1400, 221, 290]], versus=[1360, 330]),
    'landscape': dict(width=1600, height=900, brand=[80, 80, 190], title=[80, 380, 96, 70],
                      cards=[[860, 225, 310], [1220, 405, 310]], versus=[1195, 462]),
    'square': dict(width=1200, height=1200, brand=[80, 78, 190], title=[80, 275, 100, 78],
                   cards=[[160, 530, 350], [690, 660, 350]], versus=[600, 785]),
}


def add_asset(parent, path, x, y, size, prefix, height=None, crop=None):
    height = size if height is None else height
    if path.suffix.lower() == '.svg':
        svg = vector_asset(path, prefix)
        svg.attrib.update(x=str(x), y=str(y), width=str(size), height=str(height),
                          color='#101010', preserveAspectRatio='xMidYMid meet')
        parent.append(svg)
        return
    mime = {'.png': 'png', '.jpg': 'jpeg', '.jpeg': 'jpeg', '.webp': 'webp'}[path.suffix.lower()]
    data = base64.b64encode(path.read_bytes()).decode('ascii')
    attrs = dict(x=x, y=y, width=size, height=height, preserveAspectRatio='xMidYMid meet')
    if crop:
        vx, vy, vw, vh = crop['viewbox']
        parent = node(parent, 'svg', **attrs, viewBox=f'{vx} {vy} {vw} {vh}')
        clip = node(node(parent, 'defs'), 'clipPath', id=prefix+'-crop')
        node(clip, 'rect', x=vx, y=vy, width=vw, height=vh, rx=crop.get('radius', 0))
        attrs = dict(width=crop['source_width'], height=crop['source_height'])
        attrs['clip-path'] = f'url(#{prefix}-crop)'
    node(parent, 'image', **attrs, **{f'{{{XLINK}}}href': f'data:image/{mime};base64,{data}'})


def text(parent, value, x, y, size, color, weight=600, anchor='start', **attrs):
    node(parent, 'text', x=x, y=y, fill=color, **{'font-family': 'Poppins', 'font-size': size,
         'font-weight': weight, 'text-anchor': anchor, **attrs}).text = value


def compose(spec, base, format_name):
    layout = {**LAYOUTS[format_name], **spec.get('layouts', {}).get(format_name, {})}
    w, h = layout['width'], layout['height']
    products = spec['products']
    if len(products) != 2:
        raise ValueError('This comparison layout requires exactly two products.')
    lines = spec['title']
    if not lines or len(lines) > 3 or not all(isinstance(s, str) for s in lines):
        raise ValueError('Supply one to three title lines and inspect the rendered result.')
    ink = spec.get('ink', '#172A3C')
    secondary = spec.get('secondary', '#3C6176')
    root = ET.Element(f'{{{SVG}}}svg', dict(width=str(w), height=str(h), viewBox=f'0 0 {w} {h}'))
    node(root, 'title').text = ' '.join(lines) + ': ' + ' vs '.join(p['name'] for p in products)
    defs = node(root, 'defs')
    shadow = node(defs, 'filter', id='soft-shadow', x='-40%', y='-40%', width='190%', height='210%')
    node(shadow, 'feGaussianBlur', stdDeviation=15)
    edge = node(defs, 'linearGradient', id='edge', x1=0, y1=0, x2=0, y2=1)
    for offset, opacity in [(0, 1), (.58, .55), (1, .8)]:
        node(edge, 'stop', offset=offset, **{'stop-color': '#FFFFFF', 'stop-opacity': opacity})
    bg = node(root, 'g', id='Background-raster')
    add_asset(bg, base/spec['backgrounds'][format_name], 0, 0, w, 'background', height=h)
    bg[0].set('preserveAspectRatio', 'xMidYMid slice')
    bx, by, bw = layout['brand']
    brand = node(root, 'g', id='Olares-official-logo')
    add_asset(brand, base/spec['brand'], bx, by, bw, 'olares', height=bw*.236)
    tx, ty, leading, size = layout['title']
    title = node(root, 'g', id='Headline-editable')
    for index, line in enumerate(lines):
        text(title, line, tx, ty+index*leading, size, ink, weight=700, **{'letter-spacing': -1.8})
    for index, (product, bounds) in enumerate(zip(products, layout['cards'])):
        x, y, s = bounds
        scale = s/290
        ident = f'Product-{index+1}'
        group = node(root, 'g', id=ident)
        node(group, 'title').text = product['name']
        shade = node(group, 'g', id=ident+'-shadow', opacity='.20', filter='url(#soft-shadow)')
        node(shade, 'rect', x=x+5*scale, y=y+19*scale, width=s, height=s, rx=48*scale,
             fill=spec.get('shadow', '#457695'))
        gradient = node(defs, 'linearGradient', id=ident+'-fill', x1=0, y1=0, x2=.65, y2=1)
        for offset, color, opacity in [(0, '#FFFFFF', .98), (.58, spec.get('surface', '#F6FAFE'), .94),
                                       (1, product['tint'], .98)]:
            node(gradient, 'stop', offset=offset, **{'stop-color': color, 'stop-opacity': opacity})
        tile = node(group, 'g', id=ident+'-tile')
        node(tile, 'rect', x=x, y=y+7*scale, width=s, height=s, rx=48*scale, fill=product['tint'])
        node(tile, 'rect', x=x, y=y, width=s, height=s, rx=48*scale,
             fill=f'url(#{ident}-fill)', stroke='url(#edge)', **{'stroke-width': 3})
        logo = node(group, 'g', id=ident+'-official-logo')
        ls = s*product.get('icon_fraction', .51)
        add_asset(logo, base/product['icon'], x+(s-ls)/2, y+118*scale-ls/2, ls, ident,
                  crop=product.get('crop'))
        label_y = y+(234 if product.get('engine') else 242)*scale
        text(group, product['name'], x+s/2, label_y, 30*scale, ink, anchor='middle',
             id=ident+'-editable-name')
        if product.get('engine'):
            text(group, product['engine'], x+s/2, y+264*scale, 19*scale, secondary,
                 weight=500, anchor='middle', id=ident+'-editable-engine')
    text(root, 'vs.', *layout['versus'], 26 if format_name != 'square' else 30, secondary,
         weight=500, anchor='middle', id='Comparison-vs-editable')
    return ET.ElementTree(root)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('config', type=Path)
    parser.add_argument('output', type=Path)
    parser.add_argument('--format', nargs='+', choices=LAYOUTS, default=['wide'])
    args = parser.parse_args()
    spec = json.loads(args.config.read_text(encoding='utf-8'))
    args.output.mkdir(parents=True, exist_ok=True)
    for fmt in args.format:
        target = args.output/f'{fmt}.svg'
        compose(spec, args.config.resolve().parent, fmt).write(target, encoding='utf-8', xml_declaration=True)
        print(target)


if __name__ == '__main__':
    main()
