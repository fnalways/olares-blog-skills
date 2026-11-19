# Olares Blog Skills

Two agent skills for producing Olares blog posts and covers, maintained by [fnalways](https://github.com/fnalways).

| Skill | Purpose |
| --- | --- |
| `olares-blog` | Writing and editing, release posts, WordPress formatting, Yoast SEO, media handling, draft synchronization, and authorized publication |
| `olares-blog-cover` | Cover art direction, visual references, editable SVG composition, and wide/social layouts |

## Install from npm

Requires Node.js 20 or newer. Install both skills for Codex:

```sh
npx olares-blog-skills install
```

For Claude Code:

```sh
npx olares-blog-skills install --agent claude
```

For another agent or a project-specific skills folder:

```sh
npx olares-blog-skills install --dir .agents/skills
```

Codex defaults to `$CODEX_HOME/skills` when set, otherwise `~/.codex/skills`. Claude Code uses `~/.claude/skills`. Open a new agent session after installing.

To update an existing installation:

```sh
npx olares-blog-skills@latest install --force
```

`--force` backs up existing skill folders under `.olares-blog-skills-backups` beside the destination skills directory before replacing them. Review and merge local customizations from those backups. Without `--force`, existing skills are left untouched. The package has no runtime npm dependencies and no automatic install scripts.

## Install from GitHub

The repository's `skills/` directory contains standard `SKILL.md` folders. You can clone this repository and copy either folder into your agent's skills directory, including its references, scripts, and assets.

## Use

Example prompts for Codex:

```text
Use $olares-blog to format this approved draft in WordPress and configure Yoast.
Keep it as a draft.

Use $olares-blog-cover to design an editable cover for this article.
Deliver a 1800×600 header and a 1600×900 social card.
```

The skills describe a workflow; they do not supply WordPress, Figma, or image-generation access. Configure the relevant connectors or credentials in your own environment. Never commit credential files. Python 3 is needed for the bundled helper scripts. Screenshot compression additionally uses `cwebp` and Pillow. A renderer such as Sharp is needed when exporting SVG to PNG. These tools are not installed automatically.

## Included conventions

- Gutenberg tables: **Stripes**, font size **S**.
- Article-body page links: new tab with `noopener`; same-page anchors and mail/phone links retain normal behavior.
- Screenshots: lossless WebP when smaller, with decoded pixel verification.
- Cover pair: **1800×600** header and **1600×900** `_card` social image.
- Preserve approved wording and publication status. Publish or schedule only when requested.

These are authoring defaults, not global WordPress settings. Existing site themes and plugins remain under the site's control.

## Portability and references

This distribution removes machine-specific paths, private Figma URLs, and local draft thumbnails. It preserves the written design observations and editorial preferences. Historical examples are not current product specifications. Read the current project's brand guidelines and verify product claims against official sources. No credentials, unpublished article drafts, or production exports are included.

The two skills can be used without the author's private SEO workspace. Additional writing/design skills are optional when available. The included Olares logo is a brand asset subject to its owner's rights; see [NOTICE](NOTICE).

## Development and releases

```sh
npm test
npm pack --dry-run
```

For a release, review the package contents, update the version, authenticate with npm, and run `npm publish --access public`. Publishing may require npm's browser/2FA verification. GitHub is the source of record for this portable distribution.

## License

Authored instructions and code are MIT licensed. Brand assets, trademarks, and third-party material are excluded from that grant; see [NOTICE](NOTICE).
