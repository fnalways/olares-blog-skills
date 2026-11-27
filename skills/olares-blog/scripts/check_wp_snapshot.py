#!/usr/bin/env python3
"""Check local WordPress API snapshots. No network access or remote mutations."""
import argparse
import json
from pathlib import Path
from urllib.parse import unquote, urlsplit


def load(path):
    value = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("Expected a JSON object")
    return value


def image_url(value):
    parts = urlsplit(value or "")
    return parts.scheme.lower(), parts.netloc.lower(), unquote(parts.path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("post")
    parser.add_argument("--media", required=True)
    parser.add_argument("--expected-status", choices=["draft", "pending", "publish", "future", "private"])
    parser.add_argument("--expected-author", type=int)
    parser.add_argument("--legacy-pair", action="store_true", help="Validate an existing wide/card pair instead of the default card-only delivery")
    parser.add_argument("--before")
    parser.add_argument("--images-only", action="store_true")
    args = parser.parse_args()
    if args.images_only and not args.before:
        parser.error("--images-only requires --before")
    try:
        post, media = load(args.post), load(args.media)
        before = load(args.before) if args.before else None
        card = media["card"]
        header = media["header"] if args.legacy_pair else None
        seo = post.get("yoast_head_json") or {}
        checks = []

        def check(name, condition):
            checks.append({"check": name, "passed": bool(condition)})

        check("post identity present", isinstance(post.get("id"), int) and post["id"] > 0)
        if args.expected_status:
            check("expected status", post.get("status") == args.expected_status)
        if args.expected_author is not None:
            check("expected author", post.get("author") == args.expected_author)
        assets = [("card", card, (1600, 900))]
        if args.legacy_pair:
            assets.append(("header", header, (1800, 600)))
        for name, item, size in assets:
            details = item.get("media_details") or {}
            check(name + " dimensions", (details.get("width"), details.get("height")) == size)
            check(name + " media ID", isinstance(item.get("id"), int) and item["id"] > 0)
            check(name + " source URL", urlsplit(item.get("source_url", "")).scheme in ("https", "http"))
        card_path = Path(image_url(card.get("source_url"))[2])
        check("card suffix", card_path.stem.endswith("_card"))
        if args.legacy_pair:
            header_path = Path(image_url(header.get("source_url"))[2])
            check("paired filenames", card_path.stem == header_path.stem + "_card" and card_path.suffix == header_path.suffix and card_path.parent == header_path.parent)
        check("featured image reference", post.get("featured_media") == (header if args.legacy_pair else card).get("id"))
        for key in ("title", "description", "og_title", "og_description"):
            check("SEO " + key, isinstance(seo.get(key), str) and bool(seo[key].strip()))
        og_images = seo.get("og_image") or []
        first = og_images[0] if isinstance(og_images, list) and og_images else {}
        check("primary OG card reference", image_url(first.get("url")) == image_url(card.get("source_url")))
        check("primary OG dimensions", (first.get("width"), first.get("height")) == (1600, 900))
        if seo.get("twitter_image"):
            check("explicit X image reference", image_url(seo["twitter_image"]) == image_url(card.get("source_url")))
        if before:
            check("same target post", before.get("id") == post.get("id"))
        if args.images_only:
            for key in ("title", "content", "excerpt"):
                old_raw = (before.get(key) or {}).get("raw")
                new_raw = (post.get(key) or {}).get("raw")
                check(key + " preserved (edit context)", isinstance(old_raw, str) and old_raw == new_raw)
            for key in ("status", "slug", "author", "categories", "tags"):
                old, new = before.get(key), post.get(key)
                if key in ("categories", "tags") and isinstance(old, list) and isinstance(new, list):
                    old, new = sorted(old), sorted(new)
                check(key + " preserved", key in before and key in post and old == new)
            old_seo = before.get("yoast_head_json") or {}
            for key in ("title", "description", "og_title", "og_description", "twitter_title", "twitter_description"):
                check(key + " preserved", old_seo.get(key) == seo.get(key))
            old_meta, new_meta = before.get("meta") or {}, post.get("meta") or {}
            for key in ("_yoast_wpseo_focuskw", "_yoast_wpseo_title", "_yoast_wpseo_metadesc"):
                if key in old_meta:
                    check(key + " preserved", old_meta[key] == new_meta.get(key))
        passed = all(item["passed"] for item in checks)
        print(json.dumps({"passed": passed, "checks": checks,
                          "limits": "Local snapshots only. Inspect live visual output, links, source version, and publication authorization separately."},
                         ensure_ascii=False, indent=2))
        return 0 if passed else 1
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
        print(json.dumps({"passed": False, "error": type(exc).__name__,
                          "message": "Invalid snapshot or media manifest. Check input files and documented schema."}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
