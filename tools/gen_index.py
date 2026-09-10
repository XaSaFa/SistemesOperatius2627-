#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera l'index.html autònom (offline) per navegar per la base de coneixements.

Ús:
    python tools/gen_index.py

Llegeix tots els fitxers .md del repositori (excepte la carpeta tools/) i escriu
index.html a l'arrel amb tot el contingut incrustat en base64: funciona amb doble
clic, sense servidor ni connexió.
"""
import base64, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)                      # arrel del repositori
SKIP_DIRS = {".git", "tools", "node_modules", ".github", "assets-src"}
SKIP_FILES = {"CONTRIBUTING.md", "PUBLICACIO.md"}  # docs del repo, no de la base de coneixements

# L'ordre d'aquest diccionari fixa l'ordre del menú lateral i de la navegació
# Anterior/Següent: RA1 -> RA4 -> RA5 -> RA3 -> RA2 (ordre del curs).
GROUPS = {
    "":                          "Inici",
    "00-referencia":             "Referència",
    "01-caracteritzacio-dels-so":"RA1 · Caracterització dels SO",
    "04-administracio-del-so":   "RA4 · Administració del SO",
    "05-maquines-virtuals":      "RA5 · Màquines virtuals",
    "03-configuracio-basica":    "RA3 · Configuració bàsica",
    "02-instal-lacio-de-so":     "RA2 · Instal·lació de SO",
}
GROUP_ORDER = list(GROUPS.keys())


def first_h1(text, fallback):
    for line in text.splitlines():
        m = re.match(r'^#\s+(.*\S)\s*$', line)
        if m:
            return m.group(1).strip()
    return fallback


def collect():
    docs, content = [], {}
    for root, dirs, files in os.walk(BASE):
        dirs[:] = [d for d in sorted(dirs) if d not in SKIP_DIRS and not d.startswith(".")]
        for fn in sorted(files):
            if not fn.endswith(".md") or fn in SKIP_FILES:
                continue
            full = os.path.join(root, fn)
            rel = os.path.relpath(full, BASE).replace("\\", "/")
            with open(full, "r", encoding="utf-8") as f:
                txt = f.read()
            gkey = "" if "/" not in rel else rel.split("/")[0]
            docs.append({"path": rel, "title": first_h1(txt, fn), "group": gkey})
            content[rel] = base64.b64encode(txt.encode("utf-8")).decode("ascii")

    def key(d):
        g = GROUP_ORDER.index(d["group"]) if d["group"] in GROUP_ORDER else 99
        return (0 if d["path"] == "README.md" else 1, g, d["path"])

    docs.sort(key=key)
    manifest = [{"path": d["path"], "title": d["title"],
                 "group": GROUPS.get(d["group"], d["group"])} for d in docs]
    return manifest, content


HTML = r"""<!doctype html>
<html lang="ca" data-theme="auto">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Base de coneixements · SO monolloc (MP0222)</title>
<style>
  :root{
    --bg:#ffffff; --bg-alt:#f5f6f8; --bg-code:#f1f2f4; --text:#1f2328; --text-dim:#57606a;
    --border:#d0d7de; --accent:#0969da; --accent-soft:#ddf4ff; --shadow:rgba(0,0,0,.08);
    --sidebar-w:320px;
  }
  @media (prefers-color-scheme: dark){
    :root:not([data-theme="light"]){
      --bg:#0d1117; --bg-alt:#161b22; --bg-code:#161b22; --text:#e6edf3; --text-dim:#8b949e;
      --border:#30363d; --accent:#4493f8; --accent-soft:#132a45; --shadow:rgba(0,0,0,.4);
    }
  }
  :root[data-theme="dark"]{
    --bg:#0d1117; --bg-alt:#161b22; --bg-code:#161b22; --text:#e6edf3; --text-dim:#8b949e;
    --border:#30363d; --accent:#4493f8; --accent-soft:#132a45; --shadow:rgba(0,0,0,.4);
  }
  *{box-sizing:border-box}
  html,body{margin:0;padding:0;height:100%}
  body{background:var(--bg);color:var(--text);font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;-webkit-text-size-adjust:100%}
  a{color:var(--accent);text-decoration:none}
  a:hover{text-decoration:underline}
  .layout{display:grid;grid-template-columns:var(--sidebar-w) 1fr;height:100%}
  .sidebar{background:var(--bg-alt);border-right:1px solid var(--border);display:flex;flex-direction:column;min-height:0}
  .brand{padding:16px 18px 12px;border-bottom:1px solid var(--border)}
  .brand h1{margin:0;font-size:15px;line-height:1.35}
  .brand p{margin:4px 0 0;font-size:12px;color:var(--text-dim)}
  .search{padding:12px 14px;border-bottom:1px solid var(--border)}
  .search input{width:100%;padding:8px 10px;border:1px solid var(--border);border-radius:8px;background:var(--bg);color:var(--text);font-size:14px}
  .nav{overflow-y:auto;padding:8px 0 40px;flex:1;min-height:0}
  .grp{margin:2px 0}
  .grp>button{width:100%;text-align:left;background:none;border:0;color:var(--text-dim);font:600 11px/1.4 inherit;letter-spacing:.06em;text-transform:uppercase;padding:12px 18px 6px;cursor:pointer;display:flex;justify-content:space-between;align-items:center}
  .grp>button .chev{transition:transform .15s}
  .grp.collapsed>button .chev{transform:rotate(-90deg)}
  .grp.collapsed .items{display:none}
  .items a{display:block;padding:6px 18px 6px 22px;color:var(--text);font-size:13.5px;border-left:3px solid transparent;white-space:normal}
  .items a:hover{background:var(--bg);text-decoration:none}
  .items a.active{background:var(--accent-soft);border-left-color:var(--accent);color:var(--accent);font-weight:600}
  .results a{display:block;padding:8px 18px;border-bottom:1px solid var(--border)}
  .results .r-title{font-size:13.5px;font-weight:600}
  .results .r-snip{font-size:12px;color:var(--text-dim);margin-top:2px}
  .results .r-empty{padding:16px 18px;color:var(--text-dim);font-size:13px}
  .main{overflow-y:auto;min-height:0;display:flex;flex-direction:column}
  .topbar{position:sticky;top:0;z-index:5;background:var(--bg);border-bottom:1px solid var(--border);display:flex;align-items:center;gap:10px;padding:10px 20px;min-height:52px}
  .topbar .crumb{font-size:13px;color:var(--text-dim);flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
  .topbar button,.hamb{background:var(--bg-alt);border:1px solid var(--border);color:var(--text);border-radius:8px;padding:6px 10px;font-size:13px;cursor:pointer;line-height:1}
  .topbar button:hover{border-color:var(--accent);color:var(--accent)}
  .topbar button[disabled]{opacity:.4;cursor:not-allowed}
  .hamb{display:none}
  .wrap{display:grid;grid-template-columns:minmax(0,1fr) 232px;gap:36px;max-width:1120px;width:100%;margin:0 auto;padding:28px 32px 96px}
  .content{min-width:0}
  .toc{position:sticky;top:72px;align-self:start;font-size:13px;max-height:calc(100vh - 96px);overflow:auto}
  .toc h4{margin:0 0 8px;font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--text-dim)}
  .toc a{display:block;padding:3px 0;color:var(--text-dim);border-left:2px solid var(--border);padding-left:10px}
  .toc a:hover{color:var(--accent)}
  .toc a.lvl3{padding-left:22px}
  .toc a.cur{color:var(--accent);border-left-color:var(--accent)}
  .content h1{font-size:28px;margin:.2em 0 .6em;line-height:1.25}
  .content h2{font-size:21px;margin:1.6em 0 .5em;padding-bottom:.3em;border-bottom:1px solid var(--border)}
  .content h3{font-size:17px;margin:1.4em 0 .4em}
  .content h4{font-size:15px;margin:1.2em 0 .3em}
  .content p{margin:.7em 0}
  .content ul,.content ol{margin:.6em 0;padding-left:1.6em}
  .content li{margin:.25em 0}
  .content li>ul,.content li>ol{margin:.2em 0}
  .content code{background:var(--bg-code);border:1px solid var(--border);border-radius:5px;padding:.12em .35em;font-size:.88em;font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
  .content pre{background:var(--bg-code);border:1px solid var(--border);border-radius:10px;padding:14px 16px;overflow-x:auto;margin:1em 0}
  .content pre code{background:none;border:0;padding:0;font-size:13px;line-height:1.5;white-space:pre}
  .content blockquote{margin:1em 0;padding:.4em 1em;border-left:4px solid var(--accent);background:var(--accent-soft);border-radius:0 8px 8px 0}
  .content blockquote p{margin:.3em 0}
  .content hr{border:0;border-top:1px solid var(--border);margin:2em 0}
  .table-wrap{overflow-x:auto;margin:1em 0}
  .content table{border-collapse:collapse;width:100%;font-size:14px}
  .content th,.content td{border:1px solid var(--border);padding:7px 11px;text-align:left;vertical-align:top}
  .content thead th{background:var(--bg-alt)}
  .content tbody tr:nth-child(even){background:var(--bg-alt)}
  .content h2 a.anchor,.content h3 a.anchor{opacity:0;margin-left:.35em;font-weight:400;text-decoration:none}
  .content h2:hover a.anchor,.content h3:hover a.anchor{opacity:.5}
  .pager{display:flex;justify-content:space-between;gap:12px;margin-top:48px;border-top:1px solid var(--border);padding-top:20px}
  .pager a{flex:1;border:1px solid var(--border);border-radius:10px;padding:12px 16px;display:block;background:var(--bg-alt)}
  .pager a:hover{border-color:var(--accent);text-decoration:none}
  .pager .lbl{font-size:11px;color:var(--text-dim);text-transform:uppercase;letter-spacing:.05em}
  .pager .t{font-weight:600;font-size:14px;margin-top:2px}
  .pager .next{text-align:right}
  .pager .spacer{flex:1}
  .backdrop{display:none}
  @media (max-width:1080px){ .wrap{grid-template-columns:minmax(0,1fr)} .toc{display:none} }
  @media (max-width:860px){
    .layout{grid-template-columns:1fr}
    .sidebar{position:fixed;inset:0 auto 0 0;width:86%;max-width:340px;transform:translateX(-100%);transition:transform .2s;z-index:30;box-shadow:0 0 40px var(--shadow)}
    body.nav-open .sidebar{transform:none}
    body.nav-open .backdrop{display:block;position:fixed;inset:0;background:rgba(0,0,0,.4);z-index:20}
    .hamb{display:inline-block}
    .wrap{padding:20px 18px 80px}
  }
  @media print{
    .sidebar,.topbar,.toc,.pager,.backdrop{display:none!important}
    .layout{display:block} .main{overflow:visible} .wrap{display:block;max-width:none;padding:0}
  }
</style>
</head>
<body>
<div class="layout">
  <aside class="sidebar" id="sidebar">
    <div class="brand">
      <h1>Sistemes operatius monolloc</h1>
      <p>Base de coneixements · MP0222 (SMX)</p>
    </div>
    <div class="search"><input id="q" type="search" placeholder="Cerca temes i contingut…" autocomplete="off"></div>
    <nav class="nav" id="nav"></nav>
  </aside>
  <div class="backdrop" id="backdrop"></div>
  <main class="main" id="main">
    <div class="topbar">
      <button class="hamb" id="hamb" aria-label="Menú">☰</button>
      <span class="crumb" id="crumb"></span>
      <button id="prev" title="Anterior">←</button>
      <button id="next" title="Següent">→</button>
      <button id="theme" title="Tema clar/fosc">◐</button>
    </div>
    <div class="wrap">
      <article class="content" id="content"></article>
      <nav class="toc" id="toc" aria-label="En aquesta pàgina"></nav>
    </div>
  </main>
</div>
<script id="__MANIFEST__" type="application/json">__MANIFEST_JSON__</script>
<script id="__CONTENT__" type="application/json">__CONTENT_JSON__</script>
<script>
"use strict";
var MANIFEST = JSON.parse(document.getElementById("__MANIFEST__").textContent);
var CONTENT  = JSON.parse(document.getElementById("__CONTENT__").textContent);
function b64utf8(b64){
  var bin = atob(b64), bytes = new Uint8Array(bin.length);
  for (var i=0;i<bin.length;i++) bytes[i] = bin.charCodeAt(i);
  return new TextDecoder("utf-8").decode(bytes);
}
function esc(s){return s.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");}
function norm(s){return s.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g,"");}
function slug(s){
  return s.toLowerCase().replace(/`/g,"").replace(/\*\*/g,"").replace(/\*/g,"").trim()
    .replace(/[^\p{L}\p{N}\s-]/gu,"").replace(/\s+/g,"-");
}
function resolvePath(base, rel){
  var dir = base.indexOf("/")>=0 ? base.replace(/\/[^\/]*$/,"") : "";
  var parts = dir ? dir.split("/") : [];
  rel.split("/").forEach(function(p){
    if(p==="."||p==="") return;
    if(p==="..") parts.pop(); else parts.push(p);
  });
  return parts.join("/");
}
function renderInline(text, cur){
  var store=[];
  text = text.replace(/`([^`]+)`/g,function(m,c){store.push(c);return "\u0000"+(store.length-1)+"\u0000";});
  text = esc(text);
  text = text.replace(/\[([^\]]+)\]\(([^)\s]+)\)/g,function(m,label,url){
    url=url.trim();
    var mm=url.match(/^([^#]*\.md)(#.*)?$/);
    if(mm){
      var tgt=resolvePath(cur,mm[1]), frag=mm[2]?mm[2].slice(1):"";
      var h="#doc="+encodeURIComponent(tgt)+(frag?"&h="+encodeURIComponent(frag):"");
      return '<a href="'+h+'">'+label+'</a>';
    }
    if(url.charAt(0)==="#") return '<a href="#h:'+url.slice(1)+'">'+label+'</a>';
    return '<a href="'+url+'" target="_blank" rel="noopener">'+label+'</a>';
  });
  text = text.replace(/\*\*([^*]+)\*\*/g,"<strong>$1</strong>");
  text = text.replace(/\*([^*\n]+)\*/g,"<em>$1</em>");
  text = text.replace(/\u0000(\d+)\u0000/g,function(m,i){return "<code>"+esc(store[+i])+"</code>";});
  return text;
}
function isTableSep(l){ return l.indexOf("|")>=0 && /^[\s:|-]+$/.test(l) && l.indexOf("-")>=0; }
function splitRow(l){
  l = l.trim().replace(/^\|/,"").replace(/\|$/,"");
  return l.split(/(?<!\\)\|/).map(function(c){return c.replace(/\\\|/g,"|").trim();});
}
function renderBlocks(md, cur, headings){
  var lines = md.replace(/\r\n?/g,"\n").split("\n");
  var out=[], i=0;
  function listMarker(l){ return l.match(/^(\s*)([-*+]|\d+[.)])\s+(.*)$/); }
  while(i<lines.length){
    var line = lines[i];
    if(/^\s*$/.test(line)){ i++; continue; }
    var fm = line.match(/^\s*```+\s*([\w.-]*)\s*$/);
    if(fm){
      var buf=[]; i++;
      while(i<lines.length && !/^\s*```+\s*$/.test(lines[i])){ buf.push(lines[i]); i++; }
      i++;
      out.push("<pre><code>"+esc(buf.join("\n"))+"</code></pre>");
      continue;
    }
    var hm = line.match(/^(#{1,6})\s+(.*\S)\s*$/);
    if(hm){
      var lvl=hm[1].length, raw=hm[2], id=slug(raw), inner=renderInline(raw,cur);
      if(headings && (lvl===2||lvl===3)) headings.push({id:id,text:raw.replace(/[`*]/g,""),lvl:lvl});
      var a = (lvl===2||lvl===3) ? ' <a class="anchor" href="#h:'+id+'">#</a>' : '';
      out.push("<h"+lvl+' id="h-'+id+'">'+inner+a+"</h"+lvl+">");
      i++; continue;
    }
    if(/^(-{3,}|\*{3,}|_{3,})\s*$/.test(line)){ out.push("<hr>"); i++; continue; }
    if(line.indexOf("|")>=0 && i+1<lines.length && isTableSep(lines[i+1])){
      var head=splitRow(line); i+=2;
      var rows=[];
      while(i<lines.length && lines[i].indexOf("|")>=0 && !/^\s*$/.test(lines[i])){ rows.push(splitRow(lines[i])); i++; }
      var t="<div class='table-wrap'><table><thead><tr>";
      head.forEach(function(c){ t+="<th>"+renderInline(c,cur)+"</th>"; });
      t+="</tr></thead><tbody>";
      rows.forEach(function(r){
        t+="<tr>";
        for(var k=0;k<head.length;k++) t+="<td>"+renderInline(r[k]||"",cur)+"</td>";
        t+="</tr>";
      });
      t+="</tbody></table></div>";
      out.push(t); continue;
    }
    if(/^\s*>/.test(line)){
      var qb=[];
      while(i<lines.length && /^\s*>/.test(lines[i])){ qb.push(lines[i].replace(/^\s*>\s?/,"")); i++; }
      out.push("<blockquote>"+renderBlocks(qb.join("\n"),cur,null)+"</blockquote>");
      continue;
    }
    if(listMarker(line)){
      var baseIndent = listMarker(line)[1].length;
      var ordered = /\d/.test(listMarker(line)[2]);
      var items=[];
      while(i<lines.length){
        var lm = listMarker(lines[i]);
        if(!lm || lm[1].length < baseIndent) break;
        if(lm[1].length > baseIndent) break;
        var dedent = lm[1].length + lm[2].length + 1;
        var cbuf=[lm[3]]; i++;
        while(i<lines.length){
          var l = lines[i];
          if(/^\s*$/.test(l)){
            var j=i+1;
            while(j<lines.length && /^\s*$/.test(lines[j])) j++;
            if(j<lines.length){
              var lead = lines[j].match(/^(\s*)/)[1].length;
              var jm = listMarker(lines[j]);
              if((jm && lines[j].match(/^(\s*)/)[1].length<=baseIndent) || (!jm && lead<=baseIndent)){ break; }
            } else { break; }
            cbuf.push(""); i++; continue;
          }
          var lead2 = l.match(/^(\s*)/)[1].length;
          var im = listMarker(l);
          if(im && lead2<=baseIndent) break;
          if(!im && lead2<=baseIndent) break;
          cbuf.push(l.slice(Math.min(lead2, dedent)));
          i++;
        }
        var inner = renderBlocks(cbuf.join("\n"), cur, headings);
        var only = inner.match(/^<p>([\s\S]*)<\/p>$/);
        items.push("<li>"+(only? only[1] : inner)+"</li>");
      }
      out.push((ordered?"<ol>":"<ul>")+items.join("")+(ordered?"</ol>":"</ul>"));
      continue;
    }
    var pbuf=[];
    while(i<lines.length && !/^\s*$/.test(lines[i]) &&
          !/^(#{1,6})\s/.test(lines[i]) && !/^\s*>/.test(lines[i]) &&
          !/^\s*```+/.test(lines[i]) && !listMarker(lines[i]) &&
          !/^(-{3,}|\*{3,})\s*$/.test(lines[i]) &&
          !(lines[i].indexOf("|")>=0 && i+1<lines.length && isTableSep(lines[i+1]))){
      pbuf.push(lines[i]); i++;
    }
    if(pbuf.length) out.push("<p>"+renderInline(pbuf.join(" ").replace(/\s+/g," ").trim(),cur)+"</p>");
  }
  return out.join("\n");
}
var byPath = {};
MANIFEST.forEach(function(d,idx){ d.idx=idx; byPath[d.path]=d; });
function buildNav(){
  var nav = document.getElementById("nav");
  var groups = [];
  MANIFEST.forEach(function(d){
    var g = groups[groups.length-1];
    if(!g || g.name!==d.group){ g={name:d.group,items:[]}; groups.push(g); }
    g.items.push(d);
  });
  nav.innerHTML = groups.map(function(g){
    return '<div class="grp" data-g="'+g.name+'">'+
      '<button>'+esc(g.name)+'<span class="chev">▾</span></button>'+
      '<div class="items">'+ g.items.map(function(d){
        var label = d.title.replace(/^\d+\.\s*/,"");
        return '<a data-path="'+esc(d.path)+'" href="#doc='+encodeURIComponent(d.path)+'">'+esc(label)+'</a>';
      }).join("") + '</div></div>';
  }).join("");
  nav.querySelectorAll(".grp>button").forEach(function(b){
    b.addEventListener("click",function(){ b.parentNode.classList.toggle("collapsed"); });
  });
}
function currentHash(){
  var h = location.hash.replace(/^#/,"");
  var m = /(?:^|&)doc=([^&]+)/.exec(h), hm = /(?:^|&)h=([^&]+)/.exec(h);
  return { path: m?decodeURIComponent(m[1]):"README.md", anchor: hm?decodeURIComponent(hm[1]):"" };
}
var tocLinks=[];
function render(){
  var st = currentHash();
  var doc = byPath[st.path] || byPath["README.md"];
  var md = b64utf8(CONTENT[doc.path]);
  var headings = [];
  var html = renderBlocks(md, doc.path, headings);
  var C = document.getElementById("content");
  C.innerHTML = html;
  document.title = doc.title + " · SO monolloc";
  document.getElementById("crumb").textContent = (doc.group && doc.group!=="Inici" ? doc.group + "  ›  " : "") + doc.title;
  var toc = document.getElementById("toc");
  if(headings.length>1){
    toc.innerHTML = "<h4>En aquesta pàgina</h4>" + headings.map(function(h){
      return '<a class="'+(h.lvl===3?"lvl3":"")+'" href="#h:'+h.id+'">'+esc(h.text)+'</a>';
    }).join("");
  } else { toc.innerHTML=""; }
  tocLinks = Array.prototype.slice.call(toc.querySelectorAll("a"));
  document.querySelectorAll('a[href^="#h:"]').forEach(function(a){
    a.addEventListener("click",function(e){
      e.preventDefault();
      scrollToAnchor(a.getAttribute("href").slice(3));
    });
  });
  var prev = MANIFEST[doc.idx-1], next = MANIFEST[doc.idx+1];
  var pager = '<div class="pager">';
  pager += prev ? '<a href="#doc='+encodeURIComponent(prev.path)+'"><div class="lbl">← Anterior</div><div class="t">'+esc(prev.title.replace(/^\d+\.\s*/,""))+'</div></a>' : '<span class="spacer"></span>';
  pager += next ? '<a class="next" href="#doc='+encodeURIComponent(next.path)+'"><div class="lbl">Següent →</div><div class="t">'+esc(next.title.replace(/^\d+\.\s*/,""))+'</div></a>' : '<span class="spacer"></span>';
  pager += '</div>';
  C.insertAdjacentHTML("beforeend", pager);
  var pb=document.getElementById("prev"), nb=document.getElementById("next");
  pb.disabled=!prev; nb.disabled=!next;
  pb.onclick=function(){ if(prev) location.hash="#doc="+encodeURIComponent(prev.path); };
  nb.onclick=function(){ if(next) location.hash="#doc="+encodeURIComponent(next.path); };
  document.querySelectorAll("#nav .items a").forEach(function(a){
    var on = a.getAttribute("data-path")===doc.path;
    a.classList.toggle("active", on);
    if(on){
      var grp = a.closest(".grp"); if(grp) grp.classList.remove("collapsed");
      a.scrollIntoView({block:"nearest"});
    }
  });
  document.body.classList.remove("nav-open");
  document.getElementById("main").scrollTop = 0;
  if(st.anchor){ setTimeout(function(){ scrollToAnchor(st.anchor); }, 30); }
  else window.scrollTo(0,0);
  updateTocActive();
}
function scrollToAnchor(id){
  var el = document.getElementById("h-"+id) || document.getElementById(id);
  if(!el){
    var hs = document.querySelectorAll("#content h2, #content h3");
    for(var k=0;k<hs.length;k++){ if(hs[k].id==="h-"+id){ el=hs[k]; break; } }
  }
  if(el){
    var top = el.getBoundingClientRect().top + document.getElementById("main").scrollTop - 64;
    document.getElementById("main").scrollTo({top:top, behavior:"smooth"});
  }
}
function updateTocActive(){
  if(!tocLinks.length) return;
  var mainTop = document.getElementById("main").scrollTop;
  var cur=null;
  document.querySelectorAll("#content h2, #content h3").forEach(function(h){
    if(h.getBoundingClientRect().top + mainTop - 90 <= document.getElementById("main").scrollTop) cur=h.id;
  });
  tocLinks.forEach(function(a){
    a.classList.toggle("cur", cur && a.getAttribute("href")==="#h:"+cur.slice(2));
  });
}
document.getElementById("main").addEventListener("scroll", function(){ requestAnimationFrame(updateTocActive); });
var searchIndex = MANIFEST.map(function(d){
  return { d:d, hay: norm(d.title+" "+d.path+" "+b64utf8(CONTENT[d.path])) };
});
var q = document.getElementById("q");
q.addEventListener("input", function(){
  var v = norm(q.value.trim());
  var nav = document.getElementById("nav");
  if(!v){ buildNav(); render(); return; }
  var hits = searchIndex.filter(function(x){ return x.hay.indexOf(v)>=0; }).slice(0,40);
  nav.innerHTML = '<div class="results">' + (hits.length? hits.map(function(x){
    var raw = b64utf8(CONTENT[x.d.path]);
    var pos = norm(raw).indexOf(v);
    var snip = pos>=0 ? raw.replace(/\s+/g," ").slice(Math.max(0,pos-40), pos+70) : "";
    return '<a href="#doc='+encodeURIComponent(x.d.path)+'">'+
             '<div class="r-title">'+esc(x.d.title)+'</div>'+
             '<div class="r-snip">'+esc(x.d.group)+(snip? '  ·  …'+esc(snip)+'…':'')+'</div></a>';
  }).join("") : '<div class="r-empty">Cap resultat per «'+esc(q.value)+'»</div>') + '</div>';
});
var themeBtn = document.getElementById("theme");
function applyTheme(t){
  document.documentElement.setAttribute("data-theme", t);
  try{ localStorage.setItem("kb-theme", t); }catch(e){}
}
try{ var sv=localStorage.getItem("kb-theme"); if(sv) document.documentElement.setAttribute("data-theme",sv); }catch(e){}
themeBtn.addEventListener("click", function(){
  var cur = document.documentElement.getAttribute("data-theme");
  var order = ["auto","light","dark"];
  applyTheme(order[(order.indexOf(cur)+1)%3]);
});
document.getElementById("hamb").addEventListener("click", function(){ document.body.classList.toggle("nav-open"); });
document.getElementById("backdrop").addEventListener("click", function(){ document.body.classList.remove("nav-open"); });
window.addEventListener("hashchange", render);
buildNav();
render();
</script>
</body>
</html>
"""


def main():
    manifest, content = collect()
    html = (HTML
            .replace("__MANIFEST_JSON__", json.dumps(manifest, ensure_ascii=False))
            .replace("__CONTENT_JSON__", json.dumps(content, ensure_ascii=False)))
    out_path = os.path.join(BASE, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Escrit:", out_path)
    print("Documents:", len(manifest))
    print("Mida index.html: {:.1f} KB".format(os.path.getsize(out_path) / 1024))


if __name__ == "__main__":
    main()
