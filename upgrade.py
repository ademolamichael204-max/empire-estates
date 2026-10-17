#!/usr/bin/env python3
"""Usage:  python upgrade.py index.html   ->  writes index.upgraded.html (original untouched)"""
import sys, re
src = sys.argv[1] if len(sys.argv) > 1 else 'index.html'
h = open(src, encoding='utf-8').read()

def rep(old, new, count=1):
    global h
    if old not in h:
        sys.exit('NOT FOUND (file differs from the version I patched): ' + old[:70])
    h = h.replace(old, new, count)

# ---------- 1. CSS ----------
CSS = r'''
/* ===== v2: customer dashboard, dock, polish ===== */
@keyframes rise{from{opacity:0;transform:translateY(24px) scale(.98)}to{opacity:1;transform:none}}
@keyframes sweep{from{background-position:0 0}to{background-position:200% 0}}
.an2{animation:rise .6s var(--ease) both;animation-delay:calc(var(--d,0)*70ms)}
.dash{padding-bottom:1rem}
.dh{position:relative;overflow:hidden;border-radius:calc(var(--rl)*1.3);padding:clamp(1.4rem,4vw,2.2rem);margin-top:1.4rem;color:#fff;background:linear-gradient(135deg,#0b3a53,#14577d 55%,#1d6f9c);box-shadow:var(--sh2)}
:root[data-theme=dark] .dh{background:linear-gradient(135deg,#1a2f3e,#21394b 60%,#2c4a60)}
.dh::after{content:'';position:absolute;right:-70px;top:-70px;width:260px;height:260px;border-radius:50%;background:radial-gradient(circle,rgba(216,167,58,.55),transparent 70%);animation:float 10s ease-in-out infinite}
.dh h1{font-size:clamp(1.6rem,4.5vw,2.4rem);position:relative}
.dh p{opacity:.85;position:relative;max-width:52ch}
.nxt{position:relative;display:flex;align-items:center;gap:1rem;margin-top:1.2rem;padding:.8rem 1rem;border-radius:var(--rl);background:rgba(255,255,255,.12);backdrop-filter:blur(8px);cursor:pointer;transition:background .2s,transform .2s var(--ease)}
.nxt:hover{background:rgba(255,255,255,.2);transform:translateY(-2px)}
.nxt .big{font-family:'DM Serif Display',serif;font-size:2rem;line-height:1;min-width:3.2rem;text-align:center}
.nxt small{display:block;opacity:.75}
.dstats{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:.9rem;margin:1.1rem 0}
.dstat{background:var(--panel);border:1px solid var(--line);border-radius:var(--rl);padding:1rem 1.1rem;box-shadow:var(--sh1);cursor:pointer;position:relative;overflow:hidden;transition:transform .3s var(--ease),box-shadow .3s}
.dstat:hover{transform:translateY(-4px);box-shadow:var(--sh2)}
.dstat i{font-style:normal;font-size:1.3rem;display:block;margin-bottom:.35rem}
.dstat b{display:block;font-family:'DM Serif Display',serif;font-size:1.8rem;font-weight:400;line-height:1.1}
.dstat span{font-size:.78rem;color:var(--muted)}
.dstat::after{content:'';position:absolute;left:0;bottom:0;height:3px;width:100%;background:linear-gradient(90deg,var(--gold),var(--accent),var(--gold));background-size:200% 100%;animation:sweep 3s linear infinite;opacity:.7}
.qa{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:.7rem;margin-bottom:1.2rem}
.qa button{display:flex;flex-direction:column;align-items:center;gap:.3rem;padding:.9rem .5rem;border-radius:var(--rl);background:var(--panel2);font-weight:500;font-size:.85rem;transition:transform .25s var(--ease),background .2s}
.qa button:hover{transform:translateY(-3px);background:var(--panel)}
.qa b{font-size:1.4rem;font-weight:400}
.dcols{display:grid;grid-template-columns:1.5fr 1fr;gap:1.1rem;align-items:start}
.chipf{display:flex;gap:.4rem;overflow-x:auto;scrollbar-width:none;margin-bottom:.8rem}
.chipf button{padding:.35rem .9rem;border-radius:9999px;border:1px solid var(--line);font-size:.82rem;white-space:nowrap;background:var(--panel);transition:background .2s,color .2s}
.chipf button.on{background:var(--accent);color:var(--on);border-color:transparent}
.act{display:flex;gap:.9rem;padding:.9rem;background:var(--panel);border:1px solid var(--line);border-radius:var(--rl);box-shadow:var(--sh1);margin-bottom:.7rem;transition:transform .25s var(--ease),box-shadow .25s}
.act:hover{transform:translateX(4px);box-shadow:var(--sh2)}
.act img,.act .th{width:84px;height:84px;border-radius:.8rem;object-fit:cover;flex:none;cursor:pointer}
.prog{display:flex;align-items:center;gap:.3rem;margin:.4rem 0}
.prog i{flex:1;height:5px;border-radius:9999px;background:var(--line);transition:background .4s}
.prog i.on{background:var(--ok)}
.prog span{font-size:.72rem;font-weight:700;text-transform:capitalize;margin-left:.3rem;color:var(--muted)}
.prog.x span{color:var(--bad);margin:0}
.side .panel{margin-bottom:1rem}
.mrow{display:flex;gap:.7rem;align-items:center;padding:.5rem 0;border-bottom:1px solid var(--line);cursor:pointer}
.mrow:last-child{border:0}
.mrow img{width:54px;height:44px;border-radius:.5rem;object-fit:cover}
.empty{text-align:center;padding:2rem 1rem;color:var(--muted)}
.empty b{display:block;font-size:2.2rem;margin-bottom:.3rem}
#dock{display:none;position:fixed;left:.7rem;right:.7rem;bottom:calc(.6rem + env(safe-area-inset-bottom,0px));z-index:58;background:color-mix(in srgb,var(--panel) 88%,transparent);backdrop-filter:blur(16px) saturate(1.5);border:1px solid var(--line);border-radius:1.4rem;box-shadow:var(--sh2);padding:.35rem;justify-content:space-around;animation:rise .5s var(--ease)}
#dock button{flex:1;display:flex;flex-direction:column;align-items:center;gap:.05rem;padding:.4rem 0;border-radius:1rem;font-size:.68rem;font-weight:500;color:var(--muted);position:relative;transition:background .25s,color .25s,transform .2s var(--ease)}
#dock button b{font-size:1.2rem;font-weight:400;line-height:1.2}
#dock button.on{background:var(--accent);color:var(--on);transform:translateY(-2px)}
#dock .dotb{top:.2rem;right:32%}
@media(max-width:900px){#dock{display:flex}body{padding-bottom:calc(5rem + env(safe-area-inset-bottom,0px))}#cmpbar{bottom:5.4rem}#totop{bottom:5.6rem}.dcols{grid-template-columns:1fr}.nav{display:none!important}}
'''
rep('</style>', CSS + '</style>')

# ---------- 2. hide Admin option once admin slots are full ----------
rep('ready: false,', 'ready: false, adminFull: false, mf: "all", _ds: false,')
rep('function startPublic() {', '''async function checkAdminSlots() {
      try { S.adminFull = lsGet('estate-af', false) } catch { }
      try { const m = await getDoc(doc(fs, 'meta', 'adminCount')); S.adminFull = (m.exists() ? m.data().count : 0) >= MAX_ADMINS; lsSet('estate-af', S.adminFull) } catch (e) { }
      renderFoot();
    }
    function startPublic() {
      checkAdminSlots();''')
rep("const su = mode === 'signup', ad = role === 'admin';", "const su = mode === 'signup', ad = role === 'admin' && !S.adminFull; role = ad ? 'admin' : 'customer';")
rep('''<div class="roles"><button class="${!ad ? 'on' : ''}" onclick="openAuth('${mode}','customer')">Customer</button><button class="${ad ? 'on' : ''}" onclick="openAuth('${mode}','admin')">Admin</button></div>''',
    '''${S.adminFull ? '' : `<div class="roles"><button class="${!ad ? 'on' : ''}" onclick="openAuth('${mode}','customer')">Customer</button><button class="${ad ? 'on' : ''}" onclick="openAuth('${mode}','admin')">Admin</button></div>`}''')
rep('''<a onclick="openAuth('login','admin')">Admin login</a>`}''', '''${S.adminFull ? '' : `<a onclick="openAuth('login','admin')">Admin login</a>`}`}''')
# admins now log in through the normal form: route by account, not by a role button
rep('if (S.authOpen) closeModal(); await startUser(u);',
    "const wasAuth = S.authOpen; if (S.authOpen) closeModal(); await startUser(u); checkAdminSlots(); if (wasAuth && S.isAdmin) { S.adminLogin = false; S.view = 'admin'; toast('Welcome back, admin 👋') }")

# ---------- 3. navigation ----------
rep("['mine', 'My activity']", "['mine', 'Dashboard']")
rep("go('mine')\">My activity</a>", "go('mine')\">My dashboard</a>")
rep('function renderTop() {', '''function renderDock() {
      let d = $('dock'); if (!d) { d = document.createElement('nav'); d.id = 'dock'; d.setAttribute('aria-label', 'Quick navigation'); document.body.appendChild(d) }
      if (!S.user) { d.style.display = 'none'; return } d.style.display = '';
      const un = S.isAdmin ? unreadAdmin() : (S.thread?.unreadUser ? 1 : 0);
      const it = [['home', '🔍', 'Browse'], ['saved', '♥', 'Saved'], ['mine', '▦', 'Dashboard'], S.isAdmin ? ['admin', '⚙', 'Admin'] : ['chat', '💬', 'Messages']];
      d.innerHTML = it.map(([k, i, l]) => `<button class="${S.view === k ? 'on' : ''}" onclick="go('${k}')"><b>${i}</b>${l}${un && (k === 'chat' || k === 'admin') ? '<i class="dotb"></i>' : ''}</button>`).join('');
    }
    function renderTop() { renderDock();''')
rep('S.view = v; show(); scrollTo(0, 0);', 'S.view = v; S._ds = false; show(); scrollTo(0, 0);')
rep('saveSettings, toast, Swal });', 'saveSettings, setMF, toast, Swal });')

# ---------- 4. new customer dashboard ----------
a = h.index('function viewMine() {'); b = h.index('function openNotes() {')
NEW = r'''const STEPS = ['pending', 'confirmed', 'completed'];
    const prog = r => r.status === 'cancelled' ? '<div class="prog x"><span>✕ Cancelled</span></div>' : `<div class="prog">${STEPS.map((s, k) => `<i class="${k <= STEPS.indexOf(r.status) ? 'on' : ''}"></i>`).join('')}<span>${r.status}</span></div>`;
    const setMF = k => { S.mf = k; viewMine() };
    function viewMine() {
      const me = S.me || {}, rs = S.reqs, sv = me.saved || [], saved = S.listings.filter(l => sv.includes(l.id)), an = S._ds ? '' : 'an2'; S._ds = true;
      const pend = rs.filter(r => r.status === 'pending').length, spent = rs.filter(r => r.paid).reduce((x, r) => x + (+r.amount || 0), 0);
      const up = rs.filter(r => r.type === 'inspection' && r.date && !['cancelled', 'completed'].includes(r.status) && new Date(r.date) >= new Date()).sort((x, y) => new Date(x.date) - new Date(y.date)), nx = up[0];
      const hr = new Date().getHours(), gr = hr < 12 ? 'Good morning' : hr < 17 ? 'Good afternoon' : 'Good evening', first = (me.name || S.user.email || '').split(' ')[0];
      const seen = new Set(rs.map(r => r.listingId)), liked = new Set(saved.concat(rs.map(r => S.listings.find(l => l.id === r.listingId)).filter(Boolean)).map(l => l.type));
      const rec = S.listings.filter(l => l.status === 'available' && !seen.has(l.id) && !sv.includes(l.id)).sort((x, y) => (liked.has(y.type) ? 1 : 0) - (liked.has(x.type) ? 1 : 0)).slice(0, 6);
      const list = rs.filter(r => S.mf === 'all' || r.type === S.mf);
      const days = nx ? Math.max(0, Math.ceil((new Date(nx.date) - new Date()) / 864e5)) : 0, nd = nx ? new Date(nx.date) : null;
      const st = (i, n, l, go, m, d) => `<div class="dstat ${an}" style="--d:${d}" onclick="${go}"><i>${i}</i><b data-count="${n}" ${m ? 'data-fmt="money"' : ''}>0</b><span>${l}</span></div>`;
      const act = r => { const l = S.listings.find(x => x.id === r.listingId); return `<div class="act">${l?.cover ? `<img src="${l.cover}" onclick="openListing('${l.id}')" alt="">` : '<div class="th">🏠</div>'}<div class="f1"><div class="fx jb g2"><b class="tr">${esc(r.listingTitle)}</b><span class="badge b-${r.type}">${RL[r.type]}</span></div>${prog(r)}<p class="small muted">${r.type === 'offer' ? `Your offer: ${money(r.amount)} · ` : r.amount ? `Paid ${money(r.amount)}${r.verified ? ' ✓' : ''} · ` : ''}${r.date ? `Inspection ${esc(r.date.replace('T', ' '))} · ` : ''}${dstr(r.createdAt)}</p><button class="lnk" onclick="askAdmin('${r.listingId}')">💬 Ask about this</button></div></div>` };
      $('main').innerHTML = `<div class="wrap dash">
      <div class="dh ${an}"><h1>${gr}, ${esc(first)} 👋</h1><p>${rs.length ? `You have ${pend} pending request${pend === 1 ? '' : 's'} and ${saved.length} saved propert${saved.length === 1 ? 'y' : 'ies'}.` : 'Welcome! Save properties, book inspections and track everything from here.'}</p>
      ${nx ? `<div class="nxt" onclick="openListing('${nx.listingId}')"><div class="big">${days === 0 ? 'Today' : days}<small>${days === 0 ? '' : days === 1 ? 'day' : 'days'}</small></div><div class="f1 tr"><small>Next inspection</small><b class="tr">${esc(nx.listingTitle)}</b><small>${dstr(nd)} · ${tstr(nd)}</small></div><span>›</span></div>` : ''}</div>
      <div class="dstats">${st('📋', rs.length, 'Requests', "setMF('all')", 0, 1)}${st('⏳', pend, 'Pending', "setMF('all')", 0, 2)}${st('♥', saved.length, 'Saved', "go('saved')", 0, 3)}${st('💳', spent, 'Total paid', "setMF('all')", 1, 4)}</div>
      <div class="qa ${an}" style="--d:5"><button onclick="go('home')"><b>🔍</b>Browse</button><button onclick="go('chat')"><b>💬</b>Message us</button><button onclick="go('saved')"><b>♥</b>Saved</button><button onclick="openNotes()"><b>🔔</b>Alerts</button><button onclick="profile()"><b>👤</b>Profile</button></div>
      <div class="dcols"><div><div class="sech"><h2>My activity</h2></div><div class="chipf">${[['all', 'All'], ['inspection', 'Inspections'], ['rent', 'Rent'], ['buy', 'Purchase'], ['offer', 'Offers']].map(([k, l]) => `<button class="${S.mf === k ? 'on' : ''}" onclick="setMF('${k}')">${l}</button>`).join('')}</div>
      ${list.map(act).join('') || `<div class="empty"><b>🗂</b>Nothing here yet.<br><button class="btn" style="margin-top:.8rem" onclick="go('home')">Browse properties</button></div>`}</div>
      <div class="side"><div class="panel"><h3 style="margin-bottom:.4rem">Upcoming inspections</h3>${up.slice(0, 4).map(r => { const d = new Date(r.date); return `<div class="up"><div class="d"><b>${d.getDate()}</b><span>${d.toLocaleDateString([], { month: 'short' })}</span></div><div class="f1"><b class="tr">${esc(r.listingTitle)}</b><div class="small muted">${tstr(d)}</div></div>${statusBadge(r.status)}</div>` }).join('') || '<p class="muted small">None booked.</p>'}</div>
      <div class="panel"><h3 style="margin-bottom:.4rem">Latest alerts</h3>${S.notes.slice(0, 4).map(n => `<div class="note-i ${n.read ? '' : 'un'}"><i>${n.icon || '🔔'}</i><div class="f1 small">${esc(n.text)}</div></div>`).join('') || '<p class="muted small">No alerts yet.</p>'}</div>
      <div class="panel"><h3 style="margin-bottom:.4rem">Saved</h3>${saved.slice(0, 4).map(l => `<div class="mrow" onclick="openListing('${l.id}')">${l.cover ? `<img src="${l.cover}" alt="">` : '<div class="th">🏠</div>'}<div class="f1"><b class="tr">${esc(l.title)}</b><div class="small" style="color:var(--accent);font-weight:700">${money(l.price)}</div></div></div>`).join('') || '<p class="muted small">Tap ♡ on any property.</p>'}</div></div></div>
      ${rec.length ? `<section class="sec"><div class="sech"><h2>Picked for you</h2></div><div class="row">${rec.map((l, i) => card(l, i)).join('')}</div></section>` : ''}</div>`;
      if (an) animateCounts($('main')); else $('main').querySelectorAll('[data-count]').forEach(el => { const t = +el.dataset.count; el.textContent = el.dataset.fmt === 'money' ? money(t) : t.toLocaleString() });
    }
    '''
h = h[:a] + NEW + h[b:]

open('index.upgraded.html', 'w', encoding='utf-8').write(h)
print('Done -> index.upgraded.html')
