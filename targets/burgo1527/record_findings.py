"""Record this attempt; preserve all other targets in the shared ledgers."""
from pathlib import Path
import hashlib, json
from PIL import Image

ROOT=Path(__file__).resolve().parent
REPO=ROOT.parent
def read(p): return json.loads(p.read_text(encoding='utf-8'))
def write(p,d): p.write_text(json.dumps(d,ensure_ascii=False,indent=1)+'\n',encoding='utf-8')

manifest=[]
for n,archive_page in [(1,3),(2,1),(3,2),(4,4)]:
    f=ROOT/'img'/f'IMG_R9970_I46409_P{n}.jpg'
    manifest.append({'file':f.name,'decode_position':n,'archive_page':archive_page,
                     'archive_banner':f'AGS_EST_LEG_1563_0572_{archive_page:04}',
                     'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),
                     'dimensions':list(Image.open(f).size)})
write(ROOT/'image_manifest.json',manifest)

p=read(ROOT/'profile.json')
d=p['documents'][0]
d['year']='unknown'
d['date']='Undated on inspected scans; DECODE attribution 26 October 1527 not verified'
d['cleartext_in_document']='mostly clear'
d['transcription']={'by':'llm from images','source':'reading_evidence.md','image_quality':'fair',
                    'notes':'Limited unciphered excerpts, not a cipher transcription or full diplomatic edition. Attached financial drafts headed al principe do not establish supplied Burgo/Gattinara identity.'}
p['system']['summary']='No authenticated ciphertext for the named letter; attached Spanish financial drafts contain a repeated Roman-numeral amount.'
p['conditions']['tools']=['DECODE image retrieval','visual inspection and crops','British History Online calendar','cached Cryptiana pages','DECODE metadata search','PARES search']
p['solution'] = p['solution'][:3] + [
 {'kind':'verification','what':'Compared both draft openings and the repeated numeral line; headings read al principe and the numeral expression occurs after cambios / hazer otro de. Accounting notation, not a recovered cipher.','result':'worked'},
 {'kind':'literature search','what':'Read CSP Spain III.2 October 26–31, pp.432–449. Sanchez mentions Burgo reports but no matching Burgo/Gattinara letter or decipherment appears.','result':'failed'},
 {'kind':'literature search','what':'Live Cryptiana failed; cached spanish2.htm and spanish2C.htm consulted, with no matching R9970 key or reading found.','result':'failed'},
 {'kind':'access','what':'Searched harvested DECODE metadata for Burgo/Borgo/shelfmark/Gattinara: no matching sibling. R9970 lists no documents or associated records.','result':'failed'},
 {'kind':'access','what':'PARES lookup unsuccessful: one request rate limited, subsequent name search returned application search error. Full Galende PDF retrieval failed; exact p.163 citation visible only in search-index text.','result':'failed'},
 {'kind':'verification','what':'Closed attempt with source-identification blocker. Four scans inspected; no sender/date/address authenticating target. Preserved excerpts and hashes, retained open catalogue entry and queued DECODE review note.','result':'partial'}]
p['outcome']={'class':'not read','key':'none','fraction_read':'unknown','verification':['none'],
              'notes':'Named target unread: likely mismatch between catalogue attribution and attached scans. No cryptanalytic failure or impossibility claim. Need correct manuscript identity before attack.'}
write(ROOT/'profile.json',p)

cp=REPO/'catalogue.json'
c=read(cp)
e=next(x for x in c['entries'] if x['id']==198)
e['status']='Attempted 22 Sept 2026: named letter unread. All four DECODE R9970 images inspected (archive order 3,1,2,4). They show revised Spanish financial drafts headed al principe, with a repeated Roman-numeral amount, and a blank back. No date/signature establishing Burgo to Gattinara found; probable attribution/image mismatch. Exact supplied citation occurs in Galende Diaz p.163; no matching reading found in CSP Spain III.2 October 26–31 or cached Cryptiana. See burgo1527/NOTES.md.'
e['verify']='Verify the shelfmark and image association with AGS/DECODE and obtain the correctly identified 26 October 1527 Burgo letter before transcription or cryptanalysis.'
e['seen']='image'
e['outcome']='attempted, open'
e['score_note']='Images reviewed 22 Sept 2026: source identity unresolved. Original rule scores retained; they do not establish that the attached scans contain this cipher.'
write(cp,c)

qp=REPO/'decode_updates/queue.json'
q=read(qp)
q['targets']['burgo1527']={
 'writeup':None,
 'key':{'none':'No authenticated ciphertext for the described letter; image attribution requires review.'},
 'cite':'Galende Diaz, La escritura cifrada durante el reinado de los Reyes Catolicos, p.163 (exact citation from search-index text; full PDF not inspected).',
 'fields':{},
 'records':{'R9970':{
  'decode_status':'Non-decrypted','proposed':'Non-decrypted',
  'note':'Source-identification review needed, not a decryption. All four attached images were inspected. Archive banners order them 0003, 0001, 0002, 0004 in the DECODE display; page 0004 is blank. Pages 0001–0003 contain two revised Spanish financial drafts headed al principe, with the repeated opening demas de los cambios and a Roman-numeral monetary amount (apparently CX thousands DCC LXX). No date, signature or address confirming Andrea del Burgo to Gattinara on 26 October 1527 was identified. The supplied attribution and shelfmark do occur in Galende Diaz p.163, so verify the citation and image association before replacing descriptive fields. Keep Non-decrypted pending identification; no target plaintext recovered.',
  'reading':None,'reading_not_needed':True,'sent':False}}
}
write(qp,q)
print('Recorded image manifest, profile, catalogue item 198 and unsent DECODE review note.')
