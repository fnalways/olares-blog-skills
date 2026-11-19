# Olares Blog Skills

Two agent skills for producing Olares blog posts and covers, maintained by [fnalways](https://github.com/fnalways).

| Skill | Purpose |
| --- | --- |
| `olares-blog` | Writing and editing, release posts, WordPress formatting, Yoast SEO, media handling, draft synchronization, and authorized publication |
| `olares-blog-cover` | Cover art direction, visual references, editable SVG composition, and wide/social layouts |

## Install with npx skills (recommended)

Use the same GitHub-based distribution as `fnalways/olares-writing-skills`:

```sh
npx skills add fnalways/olares-blog-skills
```

The `skills` CLI comes from npm and downloads these two skills from GitHub. Neither the repository owner nor users need an npm account for this installation method. This repository is not published as an `olares-blog-skills` npm registry package.

List the available skills:

```sh
npx skills add fnalways/olares-blog-skills --list
```

Install both for Codex globally, or choose a single skill:

```sh
npx skills add fnalways/olares-blog-skills --skill olares-blog olares-blog-cover -a codex -g
npx skills add fnalways/olares-blog-skills --skill olares-blog-cover
```

For Claude Code, use `-a claude-code`. Omit `-g` for a project installation. Open a new agent session after installing. Review existing local customizations before replacing skills.

## Manual installation and local helper

Clone this repository and copy either folder from `skills/` into your agent's skills directory, including its references, scripts, and assets. Alternatively, the dependency-free local helper requires Node.js 20 or newer:

```sh
git clone https://github.com/fnalways/olares-blog-skills.git
cd olares-blog-skills
node bin/cli.js install
```

The helper defaults to `$CODEX_HOME/skills`, otherwise `~/.codex/skills`. Use `--agent claude` for `~/.claude/skills`, or `--dir PATH` for a specific skills directory. It refuses existing folders unless `--force` is supplied. Forced replacements are backed up under `.olares-blog-skills-backups` beside the destination skills directory. This backup behavior belongs to the local helper, not to the third-party `skills` CLI.

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
node bin/cli.js --help
```

For a release, review the skill contents, run validation, and tag the tested GitHub commit. GitHub is the source of record for this portable distribution. The root package is private to prevent accidental npm publication.

## License

Authored instructions and code are MIT licensed. Brand assets, trademarks, and third-party material are excluded from that grant; see [NOTICE](NOTICE).
