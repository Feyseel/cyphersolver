"""Move what git left behind after the targets/ + research/ reorganisation (26 Sept 2026).

git moves tracked files, but a checkout's git-ignored and untracked files (images, corpora, caches, DECODE
cookies) stay in the old top-level folders. Run this once in each checkout or worktree after pulling the move:

    python tools/migrate_to_targets.py            # dry run: lists what would move
    python tools/migrate_to_targets.py --apply    # moves it, never overwriting; removes emptied old folders

A leftover whose name already exists at the new place is reported and left where it is.
"""
import os, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESEARCH = ('catalogue_harvest', 'gallica_sweep', 'gallica_siblings', 'oldest', 'top50', 'mtc3')
STAY = {'docs', 'lang', 'papers', 'unpublished', 'decode_updates', 'tools', 'targets', 'research'}
APPLY = '--apply' in sys.argv

def merge(src, dst, report):
    """Move the contents of src into dst, recursing into folders that exist on both sides."""
    for name in sorted(os.listdir(src)):
        s, d = os.path.join(src, name), os.path.join(dst, name)
        if os.path.isdir(s) and os.path.isdir(d):
            merge(s, d, report)
        elif os.path.exists(d):
            report['conflict'].append(os.path.relpath(s, ROOT))
        else:
            report['move'].append(os.path.relpath(s, ROOT))
            if APPLY: shutil.move(s, d)
    if APPLY and not os.listdir(src): os.rmdir(src)

def main():
    report = {'move': [], 'conflict': []}
    for name in sorted(os.listdir(ROOT)):
        old = os.path.join(ROOT, name)
        if not os.path.isdir(old) or name.startswith('.') or name in STAY: continue
        new = os.path.join(ROOT, 'research' if name in RESEARCH else 'targets', name)
        if not os.path.isdir(new):
            print(f'  skip {name}/: no {os.path.relpath(new, ROOT)}/ in this checkout (not a moved folder)')
            continue
        merge(old, new, report)
    for p in report['move']: print(('moved ' if APPLY else 'would move ') + p)
    for p in report['conflict']: print('CONFLICT, left in place: ' + p)
    print(f"{len(report['move'])} item(s) {'moved' if APPLY else 'to move'}, {len(report['conflict'])} conflict(s)"
          + ('' if APPLY else '; rerun with --apply'))

if __name__ == '__main__':
    main()
