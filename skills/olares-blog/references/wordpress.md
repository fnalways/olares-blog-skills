# WordPress formatting, synchronization, and publication

## Connection and task records

Prefer connected tools when they can complete the task. Otherwise, use existing authorized credentials with the actual REST API and an authenticated admin session for plugin fields that cannot be written through the API. Do not install plugins, change permissions, or modify the theme for a content task.

A project may provide a local, gitignored environment file with `WORDPRESS_SITE_URL`, `WORDPRESS_USERNAME`, and `WORDPRESS_APPLICATION_PASSWORD`. Its location is project-specific; no credentials are bundled. Read credentials only at runtime. Never print them or copy them into skills, logs, or deliverables. If no connection is available, complete the local draft and upload package first, then ask only for the missing connection information.

The current site is `https://www.olares.com/blog`. Confirm the post ID, target status, and latest remote content from task records before acting, avoiding similarly named posts. Before first creation, check for duplicate slugs/titles. Before retrying creation or a media upload, check whether the previous attempt succeeded rather than creating duplicates.

## Importing a draft

1. Read the latest source draft and required images, confirming that this is the approved version to transfer. Compare new Feishu revisions before syncing rather than overwriting them with a stale local copy.
2. Convert the body to editable Gutenberg blocks. Start with the first paragraph. The WordPress title field supplies the page title, so do not insert a duplicate H1 in the body. This is a site formatting convention, not a universal search-ranking rule.
3. Preserve H2/H3 headings, links, table headers, quotations, code, and ordered lists. Apply the link defaults below. Use native image blocks with `figcaption` and actual media IDs. Avoid one giant HTML block that makes the article difficult to edit.
4. After inserting images into steps, verify that numbering continues instead of restarting at 1. Apply the table defaults below and keep tables readable on narrow screens without putting every explanation inside a cell.
5. Upload the 1600 × 900 card cover and inline images according to [Visuals and images](visuals.md), with accurate alt text/captions. A cover-only update does not require reuploading inline images.
6. Query authors and site taxonomies and apply the user's chosen values. `official-recommend` is a **tag**, not a category. Before publishing or scheduling, follow the explicit-confirmation rule below for homepage recommendation. Read back and report the final tag state with the other taxonomy.
7. Configure search and social fields according to [SEO configuration](seo.md), then save in the requested status.

## Current template and editorial fields

The November 2026 layout supplies the global navigation, footer, shared newsletter form, title area, author/date/share controls, table of contents, author bio, and related articles. Do not recreate these elements inside each post. Use editable semantic blocks and let the template control body width, typography, spacing, and mobile overflow. Preserve the table and code block defaults below.

- Write an explicit, concise excerpt that stands on its own without merely repeating the title. It is used in listings and the article title area. The article template only displays an introduction when an explicit excerpt exists.
- Use H2/H3 headings and preserve meaningful existing anchors. The template generates a desktop table of contents and a collapsible mobile version when there is more than one eligible heading. Do not add a manual table of contents to new posts or mass-delete legacy ones.
- Keep inline screenshots, diagrams, captions, semantic tables, and code. Check mobile table/code scrolling and readable images instead of adding per-post CSS or screenshotting tables.
- Check the author, category, and relevant profile information because archives and article pages display them. The article date is the original publication date. Do not change it for a cosmetic update or treat administrative modification time as a substantive update date.
- The blog home has one featured article, categories/search, then regular posts in descending publication order. WordPress native `sticky` controls the featured selection, with the latest published sticky winning. Set sticky only when explicitly selected for this role, and otherwise preserve an existing post's sticky state. New regular posts are not sticky by default. Search retains its own relevance ordering.
- Blog `sticky` and the `official-recommend` tag are separate settings. The tag decision rule below remains in force and does not authorize changing sticky.

After publication, inspect the listing card with its title/excerpt, article title area without a cover, generated heading anchors/TOC when applicable, and desktop/mobile body. Check relevant category/author/search views when changing their metadata. Layout inspection does not authorize editing the global template.

## Homepage recommendation requires an explicit decision

Before publishing or scheduling each post, establish whether the user has explicitly confirmed adding or omitting `official-recommend` for that post. A previous confirmation remains valid within its stated scope, including a confirmation covering both named posts. Do not ask again when that decision is already clear.

- If there is no explicit confirmation, ask the user whether to add `official-recommend`. This is required even when the tag is currently unchecked. Continue preparing the draft, but wait for the answer before publishing or scheduling.
- The current tag state is not a user decision. An unchecked box, an API response without the tag, silence, or a task record saying “not added” or “preserved existing tags” does not establish that the user chose to omit it. A task record counts only if it records the user's explicit decision and the posts it covers.
- General approval to publish or schedule does not answer the homepage-recommendation question. Do not infer a yes or no from that approval, and do not add the tag automatically.
- Record the confirmed choice for each post, apply it, then read it back. Include whether `official-recommend` is present in the publication or scheduling result.
- If the missing confirmation is discovered after publication or scheduling, disclose it and ask about the tag. Do not silently change tags, unpublish, or cancel a schedule. Read-only questions about the tag do not authorize changing it.

## Link defaults

For Olares blog posts being created, imported, or formatted, the user's default is to open article-body page links in a **new tab**, including Olares internal links, external references, and links to full-size images. Write `target="_blank"` and add `noopener` to `rel`, preserving any existing relationship tokens. Leave same-page anchors, `mailto:`, and `tel:` links with their normal behavior. A user's explicit exception takes precedence.

Apply the attributes to saved Gutenberg markup, keeping any link settings in block attributes consistent. For blocks such as Yoast FAQ that store rich-text answers in JSON as well as HTML, update both representations if their links change. Check the rendered content after saving. Preserve the current publication status and scheduled date when making a links-only update.

This is the skill's authoring default: apply it automatically to posts in scope without toggling each link manually. It does not change WordPress's global editor preferences or existing posts outside the task. Changing site-wide behavior for manually added links requires a separate site-level implementation in the theme or a plugin; do not claim that updating this skill configures such a switch.

## FAQ blocks and schema

When an article contains a genuine FAQ section, use one Yoast FAQ Gutenberg block for its questions and answers by default. Keep the `FAQ` section heading as a normal heading outside the block. Use ordinary heading and paragraph blocks only when the user explicitly requests them or the Yoast block is unavailable; report the fallback rather than implying that FAQ schema exists.

Preserve the approved wording, formatting, and links when creating or converting the block. Keep the Yoast block's `questions` attributes, `jsonQuestion`/`jsonAnswer` values, and rendered `schema-faq` HTML synchronized. Apply the link defaults above to both stored representations. Do not add a separate hand-written FAQ JSON-LD block, which would duplicate Yoast's schema.

After saving, read the editable post content and verify that there is exactly one Yoast FAQ block with the expected number of questions. For a published post, check the production page for the rendered `wp-block-yoast-faq-block` markup and Yoast JSON-LD containing `FAQPage` and every saved question. If any of these checks fail, fix the block or report the specific limitation before claiming that FAQ schema is active.

## Code block defaults

For code blocks in posts being created or formatted, use the smallest named font-size preset available in the editor. On the current site this is **Small (S)**, serialized as `fontSize: "small"` with `has-small-font-size` on the `wp-block-code` element. Use the theme preset rather than a custom pixel size. Preserve the code, spacing, and line breaks. This applies to code blocks, not inline code. Read back the saved size after editing. Do not apply it to unrelated existing posts without a request.

## Table defaults

Use the native Gutenberg Table block for all tables in Olares blog posts being created or formatted. The user's default is **Stripes** style (alternating row backgrounds) and **S** font size. Preserve the header row, column structure, and cell text. Use the theme's preset rather than a guessed pixel size or custom CSS.

In serialized Gutenberg content, set `className` to `is-style-stripes` and `fontSize` to `small`. The matching figure has `wp-block-table is-style-stripes has-small-font-size` classes. For example, a table with automatic column widths begins:

```html
<!-- wp:table {"hasFixedLayout":false,"className":"is-style-stripes","fontSize":"small"} -->
<figure class="wp-block-table is-style-stripes has-small-font-size"><table>
```

Keep block attributes and saved markup consistent so the editor recognizes the block. Read back the saved style and font-size settings; inspect narrow-screen wrapping or horizontal scrolling when preview access is available. Apply this default to the posts in the current task; updating the skill does not authorize a bulk restyle of previously published articles. A user's explicit per-article styling choice takes precedence.

## Updating an existing post

Before editing, save a recoverable snapshot of the target post and necessary media records, limiting reads to the target resources. Use narrow updates rather than replaying an old full-post payload.

For image synchronization:

1. Export the approved 1600 × 900 card and verify its appearance and dimensions. A wide image is not required.
2. Choose a collision-free filename such as `topic-v2_card.webp`. Check the final URL and filename after uploading.
3. Set the card attachment directly as the post's featured image and configure it as the Yoast social image. Verify the rendered listing and social metadata separately. Legacy pairs may remain unchanged when outside the requested image scope.
4. Save without changing fields outside the image scope. Update an independent old X image if one exists.
5. Read the remote post again and compare the body, title, slug, author, categories, tags, SEO copy, and status. Investigate unexpected changes before attempting recovery. Do not overwrite concurrent user edits with an old full-post rollback.

When using REST and the admin editor together, remember that the editor may hold stale state. Finish API updates first, then load the latest editor state for plugin fields. Compare remote snapshots again after saving.

## Publishing and scheduling

Requests to format, synchronize, or save a draft do not authorize publication. An explicit request to publish the current draft does not need an additional approval round.

Before executing, check the current body, author, categories/tags including the explicitly user-confirmed `official-recommend` choice under the rule above, card cover, captions, links, Yoast FAQ block/schema when an FAQ is present, SEO/social images, and desktop/narrow-screen previews. Stop only when a necessary condition is missing and explain the specific reason. Fix routine issues directly.

- Immediate publication: use a supported publishing operation on the confirmed target post only.
- Scheduling: convert from the user's timezone and verify the WordPress site timezone and UTC. Save the correct future status and report the date/time in the user's timezone. Do not assume the execution machine's timezone is the user's.
- Editing a published post: confirm that the current request authorizes updating that live post. Afterwards, check the production URL, actual images, and SEO output. Do not incidentally change site-wide caching, send social messages, or submit URLs in bulk.

## Remote verification and recovery

Read the target again after every write instead of relying only on the write response. Verify status, author and taxonomy, complete body content, Yoast FAQ block/schema when applicable, actual media dimensions/URLs, the `_card` suffix, and matching featured/OG image references. If readback fails, do not claim completion or retry writes indefinitely.

Use the skill's read-only local checker for saved API JSON:

```bash
python3 <skill-dir>/scripts/check_wp_snapshot.py post.json \
  --media cover-media.json --expected-status draft \
  --before previous-post.json --images-only
```

`post.json` is a WordPress post object fetched in edit context. `cover-media.json` contains `card`, with `id`, `source_url`, and `media_details.width/height`. The default check expects that card as `featured_media`. For an existing legacy pair only, supply both `header` and `card` and pass `--legacy-pair`. This compatibility mode does not require a wide image for new delivery. The checker does not access the network or write to WordPress and does not replace visual inspection. Use `--expected-author` to check a specified author ID.

Deliver a brief report with the edit/preview/production link, actual status, and changes made. For browser updates, save and show evidence screenshots as required by the tool instructions. A successful upload is not publication, and synchronized source files do not prove that frontend caches have refreshed.
