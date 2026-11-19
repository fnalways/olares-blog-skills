# Olares release posts

A release post helps readers understand the release's main changes, why they matter, and how they affect the Olares experience. Use connected explanations and deliberate selection of material. Follow SKILL.md and writing.md for shared brand guidance, writing preferences, and delivery boundaries.

## Editorial references

The observations below come from rereading the WordPress bodies of these two posts on November 18, 2026. They are current editorial references. Their structure can inform new work, but their features and numbers belong to those releases and require separate verification before reuse.

| Reference | How the article develops | Reusable editorial judgment |
| --- | --- | --- |
| [1.12.6](https://www.olares.com/blog/olares-1-12-6/) | The opening identifies Agent Skills, Model Console, and shared apps as the three main changes. Model Console begins with earlier ways of running models and explains the significance of separating engines from instances. Shared apps explains the infrastructure change before showing the concrete difference: members no longer install a separate Client. | Technical explanation and user value can develop in the same narrative. Start with an existing problem, a concept, or a change as understanding requires, rather than always putting benefits before mechanisms. |
| [1.12.7](https://www.olares.com/blog/olares-1-12-7/) | The opening establishes Router and Lares as the main theme. It explains their shared foundation and distinct roles before expanding into models, LarePass, languages, and support. Research and app-porting examples show how Lares works, while configuration details link to documentation. | Explain the relationship between connected features before exploring each one. Use concrete scenarios to make capabilities understandable without turning every feature into instructions. |

Both posts include At a glance, major features, Market, updating, and a closing section, but organize their main sections differently. Version 1.12.6 groups material under themes such as “Local AI gets real infrastructure” and “Everyday polish.” Version 1.12.7 develops the relationship between Router and Lares. Learn from their hierarchy and selection rather than freezing the table of contents into a template.

## Theme and emphasis

- Identify the changes that best represent the release, then assign order and space accordingly. Explain major features fully. Combine smaller fixes into brief paragraphs or lists. Do not allocate space according to PR count.
- Enter the release theme directly, without a fixed “What is Olares?” section. Summarize major changes and their relationship when useful. The opening does not always need a “you can now…” scenario.
- Make the post understandable on its own. Connect to earlier releases only when it improves understanding. Do not impose a release-evolution narrative or frame every change as AI or agent functionality.
- At a glance supports scanning, while later sections provide depth. It is a useful form shared by both reference posts. Whether to use it and how many points to include depend on the release's information load.
- Thematic headings help readers understand a group of changes. Related capabilities can share an H2 with H3 subsections. Independent major themes can have their own H2s.

## Developing feature sections

Explain what the section actually needs to establish: why the earlier experience fell short, what the product changed, how capabilities work together, or how a specific task differs as a result. Choose the most natural starting point and sequence. Do not make every section answer the same checklist.

Give explanations substance. The engine–instance relationship in Model Console and the division of responsibilities between Router and Lares deserve explanation in the article. Keep technical detail when it helps readers understand a change or choice. Do not flatten it into vague benefits in the name of user value. Explain terminology in context without accumulating unrelated component names.

Scenarios demonstrate capabilities. A research or app-porting example can show the work Lares coordinates without proceeding into startup, configuration, clicking, and acceptance steps. Use paragraphs for explanation, lists for parallel capabilities, tables for comparing choices, and screenshots or diagrams to make changes understandable. Choose the form for the information rather than prescribing paragraph counts, image counts, or a fixed combination in every section.

Include short commands, entry points, or conditions when they have explanatory value. The CLI commands in 1.12.6 clarify two ways to connect, and Overlay Gateway's wired-network requirement affects readers' understanding of the feature. Keep such necessary information while leaving detailed installation, configuration, permission procedures, and troubleshooting to the relevant documentation. A release post is not deficient simply because it has not taught the reader how to perform every operation.

## Market and other updates

System releases, LarePass, and Market follow their own schedules. Explain their relationship accurately without presenting all concurrent app updates as new system features.

Use a short description of each Market app's purpose. Preserve useful documentation links and verified community attribution. Distinguish new apps, updates, renames, and returning apps, avoiding repeated claims that an app is new. Group by purpose, thank community contributors separately, or retain a flat list according to what is easiest to scan. A long list does not by itself require grouping or deletion of user-provided apps.

A model catalog or collection of apps can receive its own explanation when it supports the release theme, as in the model section of 1.12.7. Do not repeat those descriptions in Market.

## The role of upgrade guidance and the closing

Upgrade guidance is a separate practical part of the article, not a pattern for every feature section. Provide the current official upgrade guide and concise update instructions. Highlight a change in the article when it materially affects an upgrade decision or existing use. Leave detailed migrations and alternative paths to the guide. Version 1.12.6 needed to emphasize reinstalling some apps, while 1.12.7 relied more on the guide for specific paths. Neither implies that every future post must expand every compatibility consideration.

Verify version requirements, UI paths, and procedures when they appear. Their absence does not by itself require adding them. Distinguish RC from stable releases and delivered features from plans. Do not turn unconfirmed information into a promise of availability.

The closing may connect to a real future direction, community feedback, or an experience worth trying in this release. Choose what fits the article. A fixed “What’s next” heading, thank-you paragraph, or operational task is unnecessary. Avoid empty future promises.

## Sources and facts

- When the user specifies earlier posts, read them in full and observe their selection and development of ideas. Prioritize the latest draft, user feedback, and current facts rather than an old skill template or an unapproved rewrite.
- When drafting from PRs, read titles and bodies and inspect diffs, related documentation, and evidence as needed. Combine PRs supporting the same change. Select internal changes according to their actual effect on users. Flag conflicts between a PR description and implementation for confirmation.
- Keep performance, compatibility, permissions, and capability boundaries accurate. Do not describe GPU switching time as overall inference speed or expand a claim to make the copy more appealing. Place unconfirmed information in review notes without importing the entire internal fact-checking process into the article.
- Do not reuse the old skill's mandatory channel package, product introduction, fixed closing, per-section format, or hard title-length limits. Current examples are not sentences to imitate mechanically either. Explicit user writing preferences still take priority.

## Editorial review

First assess whether readers can identify the release's main points, whether major features are explained sufficiently, whether sections connect naturally, and whether secondary material is crowding out the main story. Then examine repetition, vague phrasing, factual boundaries, and sentence flow.

For each addition, ask whether it helps readers understand this change or is included merely because it exists in the source material. Identify whether the missing element is explanation, an example, evidence, or a link instead of automatically adding instructions. When shortening, preserve necessary technical explanation and concrete differences.

A request for suggestions without changing the original calls for a review only. A new review draft is a separate version with editorial notes outside the proposed article body. Updating this skill does not authorize changing an existing blog post or review draft.
