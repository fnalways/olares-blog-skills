# Blog SEO configuration

Help search and social previews accurately convey the article's value. Follow the project's `docs/evidence-rules.md`. These are editorial and verification practices, not ranking promises.

## Distinguish title fields

| Field | Purpose |
| --- | --- |
| Article title / H1 | Express the full subject and value, preserving user-approved wording |
| Cover title | A shorter image-friendly expression consistent with the article |
| Yoast SEO title | A concise, specific search-result title candidate that may differ from the H1 when useful |
| Social title | A concrete reason to read that makes sense by itself in a feed |

Do not force all four to differ merely to fill the fields. Do not replace an approved article title with a short cover title.

## Fields

- **Focus keyphrase:** Choose a natural phrase reflecting the question the article actually answers. This is an editing aid, not a ranking guarantee. Do not invent search volume. Use research tools only when the task calls for topic research.
- **SEO title:** Put the main subject early and check that the site template does not append the brand twice. Inspect desktop and mobile previews. Character counts are guides only.
- **Meta description:** Use natural sentences to explain the audience, subject, or takeaway. Do not insert keyword lists or add empty wording to change a plugin indicator's color.
- **Slug:** Keep it readable and stable. Check for an existing slug or topic before creating a post. Preserve published URLs unless the task explicitly involves migration.
- **Excerpt:** Provide a self-contained summary for article listings. Reuse a suitable description if helpful, but check how the site displays it.
- **Social title / description / image:** Set values consistent with the article. The current blog uses a 1600 × 900 `_card` image. Do not rely solely on automatic fallback to the wide featured image.
- **X appearance:** Check for separate older copy or imagery. When no independent values are configured, verify current Yoast inheritance. Override only when the channel needs a different treatment.
- **Canonical / robots:** Preserve appropriate site behavior. After publication, check the final canonical and intended indexability. A draft preview's `?p=`, temporary date, or status is not evidence of a production SEO defect. Do not publish a draft or change indexing settings merely to inspect a preview.
- **Schema:** Verify that existing Article/BlogPosting, author, image, and date information matches reality. Do not add a second duplicate JSON-LD block. Use relevant skills and current official guidance for specialized schema requests.

## Links and authorship

Choose useful official documentation, Market entries, source repositories, or published related articles, with clear anchor text. Start verification of the current Router documentation at `https://www.olares.com/docs/use-cases/olares-router`. Check actual pages and redirects before saving, rather than reusing a retired connection guide.

Use the author specified by the user and query WordPress for the actual ID and display name. A biography should reflect real responsibilities and research areas, which may include model evaluation across modalities. Do not invent credentials. Account-level biography changes affect other posts and require a task that includes editing that profile.

## Verification

API success does not prove every Yoast field was saved. Inspect the current REST schema and responses and write only supported fields. If social fields are not exposed through REST, use the Yoast editor normally. Do not assume arbitrary `_yoast_wpseo_*` keys are writable.

After saving, read available `yoast_head_json` or actual HTML and verify titles, descriptions, OG image URLs/dimensions, and X behavior. If the plugin's subscription limits previews, verify saved fields, output tags, and images without claiming to have viewed a paid preview. After publication, check the production URL. External platform cache delays do not by themselves mean WordPress failed to save.
