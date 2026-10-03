"""Measure the share of cipher tokens read as sense in an (a)/(b) reading file (r9873_cipher.txt, r9898_cipher.txt).

Each (b) line is the reading of the (a) line above it. A (b) word is a run of hyphen-joined pieces, one piece per
cipher token (code group or letter sign); clear-text quotes, "...", "/", "¶" and (glosses) are skipped. A word counts
as read as sense when (1) it has no open group ([x] with no '=value') and no {..} letters-without-sense, and (2) the
assembled word scores at or above THRESH per character on the Spanish model es-golden-age (lang/), so a spelled run
that does not make a Spanish word is not counted. Tentative values ([x=value]) are counted as read and reported.
usage: python measure_read.py <file> [--list]   (--list prints the words that fail the language test)
"""
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm  # noqa: E402

THRESH = -4.5


def words_of(body):
    body = re.sub(r'"[^"]*"', ' ', body)
    body = re.sub(r'\((?:[^()]*)\)', ' ', body)
    body = body.replace('...', ' ').replace('¶', ' ').replace('/', ' ')
    out = []
    for w in re.findall(r'\{[^}]*\}|(?:\[[^\]]*\]|[^\s\[])+', body):
        out.append(w)
    return out


def main():
    path = sys.argv[1]
    show = '--list' in sys.argv
    m = lm.load('es-golden-age')
    tot = read = opn = garb = tent = 0
    fails = []
    for ln in open(path, encoding='utf-8'):
        mm = re.match(r'\s*\d+[bd]\s+(.*)', ln)
        if not mm:
            continue
        for w in words_of(mm.group(1)):
            if w.startswith('{'):
                n = len([p for p in re.split(r'[\s-]+', w.strip('{}')) if p])
                tot += n
                garb += n
                continue
            pieces = [p for p in re.split(r'-(?![^\[]*\])', w) if p]
            n = len(pieces)
            if n == 0:
                continue
            tot += n
            groups = re.findall(r'\[([^\]]*)\]', w)
            if any('=' not in g for g in groups):
                opn += n
                continue
            tent += sum(1 for g in groups if '=' in g)
            word = re.sub(r'\[[^=\]]*=([^\]]*)\]', r'\1', w)
            word = re.sub(r'[^A-Za-zÀ-ÿñÑçÇ ]', '', word.replace('-', '')).replace('ç', 'c').replace('ñ', 'n')
            if not word:
                tot -= n
                continue
            # period spelling: n before p/b (sienpre, enbio) is written m in the model's corpus
            word = re.sub(r'n(?=[pb])', 'm', word.lower()).replace('embi', 'envi')
            s = m.per_char(lm.norm(' ' + word + ' ', 'early'))
            if s >= THRESH:
                read += n
            else:
                garb += n
                fails.append((round(s, 2), w))
    print(f'{path}: tokens {tot}; read as sense {read} ({read / tot:.1%}); open groups {opn}; '
          f'letters without sense {garb}; tentative values counted as read {tent}')
    if show:
        for s, w in sorted(fails):
            print(s, w)


if __name__ == '__main__':
    main()
