#!/usr/bin/env node
import { cpSync, existsSync, mkdirSync, renameSync, rmSync } from 'node:fs';
import { homedir } from 'node:os';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const names = ['olares-blog', 'olares-blog-cover'];
const source = resolve(dirname(fileURLToPath(import.meta.url)), '../skills');
const help = `Olares Blog Skills

  node bin/cli.js list
  node bin/cli.js install [--agent codex|claude] [--dir PATH] [--force]

Default: install both skills into CODEX_HOME/skills or ~/.codex/skills.
--agent claude uses ~/.claude/skills. --dir specifies a skills directory instead.
Existing skills are never replaced unless --force is given; replacements are backed up.
No network calls, credentials, or automatic postinstall actions.
`;

try {
  const [command = 'help', ...args] = process.argv.slice(2);
  if (['help', '--help', '-h'].includes(command)) {
    console.log(help);
  } else if (command === 'list') {
    if (args.length) throw new Error('list takes no arguments');
    console.log(names.join('\n'));
  } else if (command === 'install') {
    let agent = 'codex', dest, force = false, explicitAgent = false;
    for (let i = 0; i < args.length; i++) {
      if (args[i] === '--force') force = true;
      else if (args[i] === '--agent' || args[i] === '--dir') {
        const option = args[i], value = args[++i];
        if (!value || value.startsWith('--')) throw new Error(`${option} requires a value`);
        if (option === '--agent') { agent = value; explicitAgent = true; }
        else dest = value;
      } else throw new Error(`Unknown option: ${args[i]}`);
    }
    if (!['codex', 'claude'].includes(agent)) throw new Error('Supported agents: codex, claude');
    if (dest && explicitAgent) throw new Error('Use --dir or --agent, not both');
    const target = resolve(dest || (agent === 'claude'
      ? join(homedir(), '.claude/skills')
      : join(process.env.CODEX_HOME || join(homedir(), '.codex'), 'skills')));
    if (target === source || target.startsWith(source + '/')) throw new Error('Cannot install into bundled sources');
    const conflicts = names.filter(name => existsSync(join(target, name)));
    if (conflicts.length && !force) throw new Error(`Already installed: ${conflicts.join(', ')}. Use --force to back up and replace them.`);
    mkdirSync(target, { recursive: true });
    const stamp = new Date().toISOString().replace(/[:.]/g, '-');
    // Backups live outside the skills directory so agents do not discover duplicate skills.
    const backupRoot = join(dirname(target), '.olares-blog-skills-backups', `${stamp}-${process.pid}`);
    for (const name of names) {
      const destination = join(target, name);
      const stage = join(target, `.${name}-${process.pid}`);
      const backup = join(backupRoot, name);
      try {
        cpSync(join(source, name), stage, { recursive: true, errorOnExist: true, force: false });
        if (existsSync(destination)) {
          mkdirSync(backupRoot, { recursive: true });
          renameSync(destination, backup);
        }
        try { renameSync(stage, destination); }
        catch (error) {
          if (existsSync(backup)) renameSync(backup, destination);
          throw error;
        }
        console.log(`Installed ${name}: ${destination}`);
        if (existsSync(backup)) console.log(`Backup: ${backup}`);
      } finally { rmSync(stage, { recursive: true, force: true }); }
    }
    console.log('Open a new agent session to load the installed skills.');
  } else throw new Error(`Unknown command: ${command}. Use --help.`);
} catch (error) {
  console.error(error.message);
  process.exitCode = 1;
}
