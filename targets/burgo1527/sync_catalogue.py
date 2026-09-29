"""Use standard catalogue renderers for only item 198, preserving shared edits."""
from pathlib import Path
import sys, re, json
ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/'docs'))
import _catalogue_page as build
e=next(x for x in build.DATA['entries'] if x['id']==198)
p=ROOT/'CATALOGUE.md'
s=p.read_text(encoding='utf-8')
s,n=re.subn(r'^\| [^\n]*\| 198 \|[^\n]*$',lambda m:build.md_table([e]).splitlines()[-1],s,flags=re.M)
assert n==1,n
p.write_text(s,encoding='utf-8')
p=ROOT/'docs/catalogue.html'
s=p.read_text(encoding='utf-8')
s,n=re.subn(r'<tr class="e" data-id="198".*?<tr class="d" data-for="198".*?</tr>',lambda m:build.row(e),s,flags=re.S)
assert n==1,n
pattern=r'(<script id="catdata" type="application/json">)(.*?)(</script>)'
m=re.search(pattern,s,re.S)
assert m
d=json.loads(m.group(2))
assert sum(x['id']==198 for x in d['entries'])==1
d['entries']=[e if x['id']==198 else x for x in d['entries']]
s=s[:m.start(2)]+json.dumps(d,ensure_ascii=False).replace('</','<\\/')+s[m.end(2):]
p.write_text(s,encoding='utf-8')
print('Updated only item 198 in Markdown and HTML catalogue; preserved navigation and other records.')
