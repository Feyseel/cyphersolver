// The Key Web: keys.json + pages.json. Keys that read several letters on a timeline, one-letter keys as cards,
// keys tried and ruled out as a list; one key card, filters, and a link per key (keys.html#k-balbases).
(async()=>{
  const tl=document.getElementById('tl'); if(!tl) return;
  const [K,pages]=await Promise.all([fetch('keys.json').then(r=>r.json()),fetch('pages.json').then(r=>r.json())]);
  const page=Object.fromEntries(pages.map(p=>[p.slug,p]));
  const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  const BANDS=[['period','Keys of the period','surviving in the archives or on DECODE'],['scholar',"Scholars' keys",'recovered or published by others'],['here','Rebuilt here','recovered by this project']];
  const band=k=>k.kind==="scholar's key"?'scholar':k.kind==='rebuilt here'?'here':'period';
  const EDGES=[['rebuilt','rebuilt from',h=>/rebuilt/.test(h)],['unchanged','read unchanged',h=>/unchanged|explained/.test(h)],
               ['adapted','adapted',h=>/adapt/.test(h)],['partial','partial',h=>/partial/.test(h)],['tried','tried, did not fit',h=>h==='tried']];
  const ecls=h=>(EDGES.find(e=>e[2](h))||EDGES[1])[0];

  // the model: one record per key, its read edges and its tried edges
  const keys=K.keys.map(k=>({...k,band:band(k),reads:[],tried:[],srcs:[]})), byId=Object.fromEntries(keys.map(k=>[k.id,k]));
  const srcById=Object.fromEntries((K.sources||[]).map(s=>[s.id,s]));
  (K.source_links||[]).forEach(l=>{ if(byId[l.key]&&srcById[l.source]) byId[l.key].srcs.push(srcById[l.source].label); });
  const letter=slug=>{ const p=page[slug]; return p&&{slug,label:p.label,y:typeof p.y==='number'?p.y:null,st:p.st,stt:p.stt}; };
  K.links.forEach(l=>{ const k=byId[l.key], t=letter(l.target); if(k&&t) k.reads.push({...t,how:l.how,note:l.note||'',e:ecls(l.how)}); });
  (K.tried||[]).forEach(l=>{ const k=byId[l.key], t=letter(l.target); if(k&&t) k.tried.push({...t,how:'tried',note:l.note||'',e:'tried'}); });
  keys.forEach(k=>{ k.reads.sort((a,b)=>(a.y??0)-(b.y??0)); k.letters=new Set(k.reads.map(r=>r.slug)).size;
    k.hay=[k.id,k.label,k.by,k.kind,k.note,k.year,k.found,...k.srcs,...[...k.reads,...k.tried].flatMap(r=>[r.slug,r.label,r.note])].join(' ').toLowerCase(); });
  const multi=keys.filter(k=>k.letters>=2), single=keys.filter(k=>k.letters===1);
  const triedOnly=keys.filter(k=>!k.letters&&k.tried.length);

  // stats
  const lset=new Set(keys.flatMap(k=>k.reads.map(r=>r.slug))), ntried=keys.reduce((s,k)=>s+k.tried.length,0);
  document.getElementById('kwstats').innerHTML=[[keys.filter(k=>k.letters).length,'keys that read a letter'],[lset.size,'letters and series read with them'],
    [multi.length,'keys that read more than one'],[keys.filter(k=>k.band==='here'&&k.letters).length,'keys rebuilt here'],[ntried,'tests of a key that did not fit']]
    .map(([n,t])=>`<span><b>${n}</b>${t}</span>`).join('');

  let showAll=false;
  document.getElementById('triedlist').insertAdjacentHTML('afterend','<button type="button" class="kw-chip" id="triedmore" hidden></button>');
  document.getElementById('triedmore').addEventListener('click',()=>{ showAll=true; render(); });
  // filter state
  const st={q:'',bands:new Set(BANDS.map(b=>b[0])),edges:new Set(EDGES.map(e=>e[0]))};
  const chips=(el,list,set,cls)=>{ el.innerHTML=list.map(([id,label])=>`<button type="button" class="kw-chip ${cls(id)}" data-v="${id}" aria-pressed="true">${cls(id).startsWith('e-')?'<i></i>':''}${esc(label)}</button>`).join('');
    el.addEventListener('click',e=>{ const b=e.target.closest('button'); if(!b) return; const v=b.dataset.v;
      set.has(v)?set.delete(v):set.add(v); b.setAttribute('aria-pressed',set.has(v)); render(); }); };
  chips(document.getElementById('kwband'),BANDS,st.bands,id=>'b-'+id);
  chips(document.getElementById('kwedge'),EDGES,st.edges,id=>'e-'+id);
  const q=document.getElementById('kwq'); q.addEventListener('input',()=>{ st.q=q.value.trim().toLowerCase(); render(); });
  const match=k=>st.bands.has(k.band)&&(!st.q||st.q.split(/\s+/).every(w=>k.hay.includes(w)));
  const edgesOf=k=>[...k.reads,...k.tried].filter(r=>st.edges.has(r.e));

  // timeline geometry
  const ys=multi.flatMap(k=>[...k.reads,...k.tried].map(r=>r.y).concat(k.year||[])).filter(y=>y!=null);
  const y0=Math.floor(Math.min(...ys)/25)*25, y1=Math.ceil(Math.max(...ys)/25)*25, pct=y=>((y-y0)/(y1-y0)*100).toFixed(2)+'%';
  const step=(y1-y0)>300?50:25;
  document.getElementById('tlgrid').innerHTML=Array.from({length:Math.floor((y1-y0)/step)+1},(_,i)=>y0+i*step)
    .map(y=>`<span style="left:${pct(y)}"><b>${y}</b></span>`).join('');
  const dot=(r,cls)=>`<a class="dot ${r.e==='tried'?'tried':esc(r.st||'')} h-${r.e}${cls||''}" href="${r.slug}.html" style="left:${pct(r.y)};top:var(--t)"
      aria-label="${esc(r.label)}: ${esc(r.how)}" title="${esc(r.label)}${r.y!=null?' ('+Math.floor(r.y)+')':''} · ${esc(r.how)}${r.note?' · '+esc(r.note):''}"></a>`;
  // letters of the same years sit side by side: each dot at its date, pushed right just enough to clear the one before
  let W=600; const GAP=14, px=y=>(y-y0)/(y1-y0)*W;
  function row(k){
    const es=edgesOf(k).filter(r=>r.y!=null).sort((a,b)=>a.y-b.y); let last=-1e9;
    const placed=es.map(r=>{ const x=Math.max(px(r.y),last+GAP); last=x; return {r,x}; });
    const ry=k.reads.map(r=>r.y).filter(y=>y!=null);
    const xs=placed.map(p=>p.x).concat(k.year?[px(k.year)]:[]), lo=Math.min(...xs), hi=Math.max(...xs);
    const dots=placed.map(({r,x})=>dot(r).replace(`left:${pct(r.y)}`,`left:${x.toFixed(1)}px`).replace('var(--t)','50%')).join('');
    const km=k.year&&ry.length&&(k.year<Math.min(...ry)-2||k.year>Math.max(...ry)+2)?`<i class="kmark" style="left:${px(k.year).toFixed(1)}px" title="key dated ${k.year}"></i>`:'';
    return `<div class="row" id="row-${esc(k.id)}" data-id="${esc(k.id)}"><button class="rl" type="button" data-key="${esc(k.id)}">${esc(k.label)}<small>${k.letters} letters${k.tried.length?` · ${k.tried.length} tried`:''}${k.by&&k.band!=='here'?' · '+esc(k.by):''}</small></button>
      <div class="track"><span class="span" style="left:${lo.toFixed(1)}px;width:${(hi-lo).toFixed(1)}px"></span>${km}${dots}</div></div>`;
  }
  const card=k=>{ const r=k.reads[0];
    return `<div class="kc b-${k.band}" id="card-${esc(k.id)}">${k.image?`<img class="thumb" src="${esc(k.image.src)}" alt="" loading="lazy">`:''}
      <button type="button" data-key="${esc(k.id)}">${esc(k.label)}</button>
      <a class="to" href="${r.slug}.html">&rarr; ${esc(r.label)}</a><small>${esc(r.how)}${r.y!=null?' · '+Math.floor(r.y):''} · ${esc(r.stt)}${k.tried.length?` · also tried on ${k.tried.length}`:''}</small></div>`; };

  function render(){
    let shown=0;
    const g=document.getElementById('tlgrid').getBoundingClientRect(); W=Math.max(200,g.width);
    // timeline
    const tb=BANDS.map(([b,label,sub])=>{ const ks=multi.filter(k=>k.band===b&&match(k)&&edgesOf(k).length).sort((a,b)=>(a.reads[0].y??0)-(b.reads[0].y??0));
      shown+=ks.length; return ks.length?`<section class="band b-${b}"><h3>${label} <span>· ${sub}</span></h3>${ks.map(row).join('')}</section>`:''; }).join('');
    tl.querySelectorAll('.band,.tl-empty').forEach(e=>e.remove());
    tl.insertAdjacentHTML('beforeend',tb||'<p class="tl-empty">No key that read several letters matches.</p>');
    // one-letter keys
    const cs=BANDS.map(([b,label])=>{ const ks=single.filter(k=>k.band===b&&match(k)&&k.reads.some(r=>st.edges.has(r.e))).sort((a,b)=>(a.reads[0].y??0)-(b.reads[0].y??0));
      shown+=ks.length; return ks.length?`<p class="cards-h b-${b}">${label} · ${ks.length}</p><div class="cards">${ks.map(card).join('')}</div>`:''; }).join('');
    document.getElementById('singles').innerHTML=cs||'<p class="tl-empty">No one-letter key matches.</p>';
    // ruled out, grouped by letter
    const byT={};
    if(st.edges.has('tried')) keys.filter(k=>match(k)).forEach(k=>k.tried.forEach(t=>(byT[t.slug]=byT[t.slug]||{t,ks:[]}).ks.push({k,note:t.note})));
    const all=Object.values(byT).sort((a,b)=>(a.t.y??0)-(b.t.y??0)), filtered=st.q||st.bands.size<BANDS.length;
    const tg=showAll||filtered?all:all.slice(0,12);
    document.getElementById('triedmore').hidden=tg.length===all.length;
    document.getElementById('triedmore').textContent=`Show all ${all.length} letters`;
    shown+=triedOnly.filter(k=>match(k)&&st.edges.has('tried')).length;
    document.getElementById('triedlist').innerHTML=tg.map(({t,ks})=>`<li><div class="tgt"><a href="${t.slug}.html">${esc(t.label)}</a><small>${t.y!=null?Math.floor(t.y)+' · ':''}${esc(t.stt)}</small></div>
      <ul>${ks.map(({k,note})=>`<li><button type="button" class="kn" data-key="${esc(k.id)}">${esc(k.label)}</button>${note?' — '+esc(note):''}</li>`).join('')}</ul></li>`).join('')
      ||'<li class="tl-empty">No ruled-out key matches.</li>';
    document.getElementById('kwcount').textContent=`${shown} of ${keys.length} keys`;
    if(cur) mark(cur);
  }

  // the key card
  const side=document.getElementById('kwside'), cardEl=document.getElementById('kwcard'), idle=cardEl.innerHTML;
  let cur=null;
  const decode=k=>{ const m=(k.kind==='DECODE key record')&&(k.label.match(/\bR(\d{2,5})\b/)||k.id.match(/^k-r(\d{2,5})$/)); return m?`https://de-crypt.org/decrypt-web/RecordsView/${m[1]}`:null; };
  const li=r=>`<li><a href="${r.slug}.html">${esc(r.label)}</a><small>${esc(r.how)}${r.note?' · '+esc(r.note):''}${r.y!=null?' · '+Math.floor(r.y):''} · ${esc(r.stt)}</small></li>`;
  function mark(id){ document.querySelectorAll('.row.sel,.kc.sel').forEach(e=>e.classList.remove('sel'));
    document.querySelectorAll(`#row-${CSS.escape(id)},#card-${CSS.escape(id)}`).forEach(e=>e.classList.add('sel')); }
  function show(id,{scroll=false,push=true}={}){
    const k=byId[id];
    if(!k){ cur=null; cardEl.innerHTML=idle; side.classList.remove('open'); mark(''); if(push) history.replaceState(null,'',location.pathname); return; }
    cur=id; mark(id);
    const bl=BANDS.find(b=>b[0]===k.band)[1], dl=decode(k);
    cardEl.innerHTML=`<p class="k">${esc(k.kind)} · ${bl}</p><h3>${esc(k.label)}</h3>
      <p class="by">${[k.by,k.year&&('key of '+k.year),k.found&&((k.band==='scholar'?'published ':'found ')+k.found)].filter(Boolean).map(esc).join(' · ')}${k.srcs.length?'<br>Held or published by '+k.srcs.map(esc).join(', '):''}</p>
      ${k.image?`<figure data-credit="${esc(k.image.credit)}"><a href="${esc(k.image.page)}.html"><img src="${esc(k.image.src)}" alt="${esc(k.image.caption||k.label)}" loading="lazy"></a><figcaption>${esc((k.image.caption||'').slice(0,160))}${(k.image.caption||'').length>160?'…':''} <span class="credit">Image: ${esc(k.image.credit)}</span></figcaption></figure>`:''}
      <p>${esc(k.note)}</p>
      ${k.reads.length?`<h4>Read ${k.letters} letter${k.letters>1?'s':''}</h4><ul>${k.reads.map(li).join('')}</ul>`:''}
      ${k.tried.length?`<h4>Tried, did not fit</h4><ul>${k.tried.map(li).join('')}</ul>`:''}
      <div class="acts"><button type="button" data-copy>Copy link</button>${dl?`<a href="${dl}" rel="noopener">DECODE record &#8599;</a>`:''}</div>`;
    side.classList.add('open'); side.scrollTop=0;
    if(push) history.replaceState(null,'','#'+id);
    if(scroll){ const el=document.getElementById('row-'+id)||document.getElementById('card-'+id); el&&el.scrollIntoView({block:'center',behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth'}); }
  }
  document.addEventListener('click',e=>{
    const b=e.target.closest('[data-key]'); if(b){ show(b.dataset.key); return; }
    if(e.target.closest('[data-copy]')){ const u=location.href; (navigator.clipboard?navigator.clipboard.writeText(u):Promise.reject()).then(()=>{ e.target.textContent='Link copied'; },()=>prompt('Link to this key',u)); }
  });
  side.querySelector('.x').addEventListener('click',()=>show(null));
  document.addEventListener('keydown',e=>{ if(e.key==='Escape'&&cur&&!document.querySelector('#search:not([hidden])')) show(null); });
  const fromHash=()=>{ const h=decodeURIComponent(location.hash.slice(1)); if(h.startsWith('q=')){ q.value=h.slice(2); st.q=h.slice(2).toLowerCase(); render(); } else if(byId[h]) show(h,{scroll:true,push:false}); };
  window.addEventListener('hashchange',fromHash);
  let rz; window.addEventListener('resize',()=>{ clearTimeout(rz); rz=setTimeout(()=>{ const w=document.getElementById('tlgrid').getBoundingClientRect().width; if(Math.abs(w-W)>4) render(); },150); });
  render(); setTimeout(fromHash,60);   // after the layout settles, or the scroll to the row lands short
})();
