---
name: olares-blog-writer
description: Write and restructure Olares blog posts by article type. Identify the type (app or feature launch overview, press release, concept explainer, hands-on X vs. Y comparison, model on Olares, use case), apply that type's structure, reference articles, and self-check list, and draft English copy that leads with what and why rather than paraphrasing docs. Use when writing or rewriting an Olares blog post, an "Introducing X" or "Meet X" announcement, a post modeled on an external reference article, or when a draft feels shallow, generic, or AI-sounding. Hand off WordPress, SEO fields, covers, and Feishu syncing to olares-blog, and keyword-led alternative or best-of posts to seo-content.
---

# Olares Blog Writer

Decide what kind of article this is, then write it the way that kind of article works. Read the Olares brand context first (`basic/olares.md` in the SEO workspace) for positioning, facts, and red lines.

## Division of work

| Need | Use |
| --- | --- |
| Choose the type, build the structure, draft, revise | This skill |
| Version release posts (Olares 1.12.x) | `olares-blog` release reference |
| WordPress formatting, Yoast, covers, Feishu sync, publication | `olares-blog`, `olares-blog-cover` |
| Hands-on head-to-head comparisons (X vs. Y, tested on Olares) | This skill, [types/comparison.md](types/comparison.md) |
| Keyword-led posts built from SEO research (X alternative, best X) | `seo-content` |

## Workflow

1. **Identify the type** and read its file.

   | Type | Use when | File |
   | --- | --- | --- |
   | Launch overview | An app or feature ships or returns, and readers need what it is, why it exists, and how it fits Olares | [types/launch-overview.md](types/launch-overview.md) |
   | Press release | Partnerships, funding, hardware or event announcements with a dateline and quotes | [types/press-release.md](types/press-release.md) |
   | Concept explainer | Explaining an Olares mechanism such as credentials, access, or CLI and agents | [types/concept-explainer.md](types/concept-explainer.md) |
   | Comparison | A hands-on "X vs. Y" post where we ran both products on Olares and readers need to choose | [types/comparison.md](types/comparison.md) |
   | Others | Model on Olares, use cases, listicles, workflows | [types/README.md](types/README.md) |

   When the user supplies an external reference article, break it into its paragraph skeleton and the job each paragraph does, map that onto the Olares topic, and show the mapping before drafting.

2. **Confirm product facts before writing.** Ask or check the docs. Do not infer.
   - Supported content formats and ways to save or import
   - Which integrations with Files, LarePass, Market, Router, models, and agents work today
   - Which plans can be stated publicly. If the user does not want to promise, write none.
   - What the screenshots show and whose real account they come from, which decides whether first person is honest

3. **Draft** with the type's skeleton plus the shared rules in [lessons.md](lessons.md).

4. **Self-check before delivery**
   - [ ] None of the AI-sounding patterns listed in lessons.md
   - [ ] H1, SEO title, and cover lead with value. Version numbers and "is back" appear once, in the body.
   - [ ] Every capability is confirmed. No invented quotes. No roadmap promises.
   - [ ] Examples serve the story rather than narrating screenshots. Cited sources are current and fit the article's timeline.
   - [ ] External links verified for title, author, and date. Internal links point to docs, Market, or related posts.
   - [ ] Paragraphs hand off to each other, and the ending leads naturally into the CTA.

## Collaboration habits

- When revising in Feishu, copy the document before large rewrites so images survive and versions stay comparable.
- Read comments with `lark-cli drive file.comments list` and answer each quote.
- Keep metadata (H1, SEO title, slug, focus keyphrase, meta description, excerpt, social copy, cover text, author, category) in a callout at the top, to be removed at publication. Launch posts target the brand keyphrase, such as "Olares Wise". Competitor keyphrases go to a separate `seo-content` article that links back.
