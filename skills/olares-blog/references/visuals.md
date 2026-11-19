# Visuals and images

Read the available `olares-blog-cover` skill for new designs or substantial design changes. This reference covers blog delivery conventions rather than duplicating a full design manual.

## Source files and edit scope

The user wants editable Figma/SVG files. Prefer existing native layers or native SVG, keep text as text, and use official vector logos. Do not deliver a single generated raster image as the final design. When the user requests or accepts a raster illustration, retain editable titles, branding, and source files, and identify the parts that remain bitmaps.

When referencing a style, extract visual characteristics such as palette, whitespace, font weight, and connector treatment. Do not mechanically copy green status dots, corner labels, product names, or panel layouts from the reference.

For title-readability improvements, preserve the approved background and graphics and change only the necessary typography and spacing. Keep model names and benefit wording within the same title at the same or similar size and weight, with the whole title readable as a thumbnail. Do not reduce key information to a tiny subtitle or treat the 80 px size used in one design as a universal cover rule.

## Paired WordPress cover assets

The current Olares blog uses this pairing, based on the user's request and site operations verified on November 5, 2026. Recheck when the site behavior changes.

| Purpose | Dimensions | Example filename |
| --- | --- | --- |
| Wide article cover / featured image | 1800 × 600 | `article-topic.webp` |
| Listing card and social sharing | 1600 × 900 | `article-topic_card.webp` |

**The 1600 × 900 filename must end in `_card` before its extension.** The user states that the frontend depends on this convention. Preserve the paired base name. Use `article-topic-v2.webp` and `article-topic-v2_card.webp` for a new version, avoiding an upload renamed to `article-topic_card-1.webp`.

A design discussion may begin with one size. Full WordPress delivery requires both assets, not just the wide version. Compose the title and main visual separately for each aspect ratio rather than stretching. When syncing a new version, update the featured image, paired card, and Yoast social image references.

## Inline images and captions

- Give each image one main point. A conceptual diagram should explain relationships without carrying the test device's complete hardware specification. Keep device configuration and resource figures in the text or relevant screenshots.
- Keep diagram text, nodes, and arrows editable. Preserve real screenshots rather than regenerating their values or state with an image model.
- Make titles, nodes, and labels readable at the actual article width. Split an overcrowded image or remove nonessential detail instead of merely shrinking type.
- A caption states the fact or significance readers should see in the image. Use a short, complete, natural sentence without repeating a subheading or describing production work. Clearly distinguish a conceptual architecture illustration from a screenshot of an actual run.
- Alt text describes the image's information in context. The caption explains its relationship to the article. Do not turn either into a keyword list.
- Place images near the first discussion of their subject. Images inside ordered lists must not interrupt numbering. The cover is usually not repeated in the body.

## Export and verification

### Lossless WebP for screenshots

For PNG interface screenshots, prefer Google's `cwebp` CLI (libwebp) to produce lossless WebP before uploading. Preserve the screenshot's dimensions, composition, and text. This is a format conversion; use the original screenshot as input.

```bash
cwebp -lossless -z 9 -exact "input.png" -o "output.webp"
```

`-exact` preserves RGB values in transparent pixels as well. Use the installed `cwebp` from PATH. Decode the input and output with Pillow, convert both to RGBA, and compare dimensions and pixel bytes:

```python
from PIL import Image

with Image.open("input.png") as source, Image.open("output.webp") as converted:
    original = source.convert("RGBA")
    result = converted.convert("RGBA")
    assert original.size == result.size
    assert original.tobytes() == result.tobytes()
```

Compare file sizes and use the WebP when it is smaller. Record actual savings rather than assuming a fixed compression ratio. If WordPress processes the uploaded file, verify the served full-size asset again before claiming pixel-identical output. Keep the original media for rollback, preserve alt text/captions, and confirm responsive sizes, width/height, and lazy loading in the rendered body. For detailed interface screenshots, link the image to its full-size media file so readers can inspect the text on a phone.

### Export checks

Record the Figma file key, the node ID for each size, and the approved version. Read the latest nodes and export at original dimensions. Do not crop an editor screenshot into a production asset. When tool limits prevent export, use the normal export function in an existing authenticated browser and briefly explain the fallback.

Inspect the actual exports for correct dimensions, loaded fonts, uncropped text and logos, and consistent content across sizes. Use site-supported WebP, PNG, or JPEG for production. Conversion must preserve composition and text. Retain SVG/Figma sources for editing. Upload SVG only if supported by the site, without changing security settings to allow it.

After uploading, read the actual URLs, filenames, and dimensions to ensure WordPress has not added a collision suffix that breaks `_card`. Retain older media for rollback unless the user requests cleanup. Do not delete historical assets incidentally.
