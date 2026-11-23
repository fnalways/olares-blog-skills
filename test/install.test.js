import test from 'node:test';
import assert from 'node:assert/strict';
import { mkdtempSync, readFileSync, writeFileSync, existsSync, readdirSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';
import { spawnSync } from 'node:child_process';

const cli = resolve('bin/cli.js');
test('installs complete skills, refuses overwrites, and backs up forced replacements', () => {
  const root = mkdtempSync(join(tmpdir(), 'olares-skills-test-'));
  const target = join(root, 'skills');
  const run = (...args) => spawnSync(process.execPath, [cli, ...args], { encoding: 'utf8' });
  try {
    assert.equal(run('install', '--dir', target).status, 0);
    assert.ok(existsSync(join(target, 'olares-blog-cover/scripts/compose_svg.py')));
    assert.ok(existsSync(join(target, 'olares-blog/references/wordpress.md')));
    const file = join(target, 'olares-blog/SKILL.md');
    writeFileSync(file, 'local customization');
    assert.equal(run('install', '--dir', target).status, 1);
    assert.equal(readFileSync(file, 'utf8'), 'local customization');
    assert.equal(run('install', '--dir', target, '--force').status, 0);
    const backups = join(root, '.olares-blog-skills-backups');
    const backup = readdirSync(backups)[0];
    assert.equal(readFileSync(join(backups, backup, 'olares-blog/SKILL.md'), 'utf8'), 'local customization');
    assert.match(readFileSync(file, 'utf8'), /name: olares-blog/);
    assert.ok(existsSync(join(target, 'olares-blog-writer/types/launch-overview.md')));
    assert.deepEqual(readdirSync(target).sort(), ['olares-blog', 'olares-blog-cover', 'olares-blog-writer']);
    assert.equal(run('install', '--dir').status, 1);
    assert.equal(run('install', '--agent', 'unknown').status, 1);
  } finally { rmSync(root, { recursive: true, force: true }); }
});
