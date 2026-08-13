# -*- coding: utf-8 -*-
"""Kronos Publications — static generator.
Index (Complete Volume + 5 part cards) + one detail page per part, each wired to its
DOI, the interactive 3D model, and the live verification/simulator page.
Regenerate:  python3 build_publications.py
"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://www.kronosfusionenergy.com"
MODEL = SITE + "/3D_Model"                        # verified live 2026-08-13
VERIFY = SITE + "/Physics_Validation_Simulation"  # site's canonical validation/live-sim route
COMMUNITY = "https://zenodo.org/communities/kronos_fusion_energy"
BUILD_DATE = "2026-08-13"

# ---- The complete volume (6th document; final PDF supplied by founder) ----
COMPLETE = dict(
    file="papers/Kronos_Combined_Editorial_2026.pdf",   
    title="The Kronos 2026 Publication — Complete Volume",
    blurb=("All five studies in one bound volume: the compact fusion isotope-and-energy "
           "platform, front to back — breeder, generator, magnets, direct energy conversion, "
           "and AI/quantum control — with the shared methodology, notation, and reproducibility "
           "manifest that ties them together."),
)

# ---- The five parts (order = reading order) ----
PAPERS = [
 dict(slug="breeder", tag="Breeder · Spherical Tokamak", pages="49 pp",
   title="Hyperion: A Spherical-Tokamak Helium-3 and Tritium Breeder Sized to a National Requirement",
   authors=["P. I. Ford", "G. L. Kulcinski"],
   pdf="papers/Kronos_Breeder_Hyperion_Editorial_2026.pdf",
   doi="10.5281/zenodo.21746157", doi2="10.5281/zenodo.21795620",
   venue="Under review · Nuclear Fusion (IOP)", sim=True,
   abstract=("A compact spherical-tokamak breeder whose size is set by an isotope-supply "
     "requirement rather than by electrical output. Across 25,200 configurations the minimum "
     "plasma current meeting a national tritium duty falls to 4.93 MA — a third of ITER's — and "
     "tritium breeding is presented as an openly-shown blanket lever (demonstrated beryllium-"
     "multiplied TBR &approx; 1.34, with an advanced-blanket development target above it). "
     "Helium-3, the strategic product, is bred independently of the blanket.")),
 dict(slug="generator", tag="Generator · D&ndash;&sup3;He Tandem Mirror", pages="48 pp",
   title="A Deuterium–Helium-3 Tandem-Mirror Generator with Direct Energy Conversion: Closure and Named Extrapolations",
   authors=["P. I. Ford", "G. L. Kulcinski"],
   pdf="papers/Kronos_Burner_TandemMirror_Editorial_2026.pdf",
   doi="10.5281/zenodo.21746479", doi2=None,
   venue="Under review · Nuclear Fusion (IOP)", sim=True,
   abstract=("A low-neutron D&ndash;&sup3;He generator that closes its power balance on "
     "<em>measured</em> component efficiencies, with every extrapolation beyond demonstrated "
     "hardware named rather than hidden. Introduces a new physics result &mdash; the synchrotron "
     "effective harmonic cutoff scales with machine size &mdash; and states its single largest "
     "open requirement (end-plug density) plainly, including a companion structural gate on the "
     "plug winding.")),
 dict(slug="magnets", tag="Magnets · REBCO", pages="24 pp",
   title="An Integrated High-Field REBCO Conductor and Winding System for Compact Fusion Magnets",
   authors=["P. I. Ford", "R. J. Weggel", "C. Weggel"],
   pdf="papers/Kronos_REBCO_MagnetTape_Editorial_2026.pdf",
   doi="10.5281/zenodo.21842514", doi2=None,
   venue="Open on Zenodo · in preparation", sim=False,
   abstract=("A strain-first REBCO conductor architecture and a bore-resolved winding method, "
     "applied across two dissimilar machines. The central result is an honest negative: the "
     "binding constraint flips between a stress-comfortable spherical-tokamak centrepost and a "
     "stress-bound mirror plug, with the field a conductor <em>enables</em> kept rigorously "
     "separate from what a coil can <em>realise</em>. Kronos has fabricated and measured nothing; "
     "every number is a design target, model output, or literature inference.")),
 dict(slug="direct-energy-conversion", tag="Power Conversion · DEC", pages="23 pp",
   title="Direct Energy Conversion for a D–³He Magnetic-Mirror Burner: The Electron Channel is the Larger Axial Stream",
   authors=["P. I. Ford", "G. L. Kulcinski"],
   pdf="papers/Kronos_DEC_QuasineutralExpander_Editorial_2026.pdf",
   doi="10.5281/zenodo.21842864", doi2=None,
   venue="Open on Zenodo · in preparation", sim=False,
   abstract=("Shows that the conventional framing of advanced-fuel direct energy conversion "
     "describes the birth spectrum, not the axial loss channel: at reactor temperatures the "
     "recoverable stream is a directed <em>electron</em> flow that no published converter "
     "recovers. Proposes a quasineutral two-species expander &mdash; the ambipolar magnetic "
     "nozzle run backward &mdash; with a pre-registered bench program to test it.")),
 dict(slug="ai-quantum-control", tag="Control · AI &amp; Quantum", pages="26 pp",
   title="Physics-Informed AI and Quantum Technologies for Certifiable Real-Time Control of Compact Fusion Generators",
   authors=["P. I. Ford"],
   pdf="papers/Kronos_AI_Quantum_Control_Editorial_2026.pdf",
   doi="10.5281/zenodo.21842371", doi2=None,
   venue="Under review · Fusion Engineering &amp; Design (Elsevier)", sim=False,
   abstract=("A layered, AI-native digital-twin control architecture evaluated as a methods-and-"
     "certification study, holding three technology-readiness tiers strictly apart. Demonstrates "
     "a deterministic safety clamp (3000/3000 injected violations caught, zero escapes), a "
     "certified control-barrier guarantee preserved through calibration, and a quantum-inspired "
     "kinetic solver &mdash; while reporting every missed target rather than reframing it.")),
]

CSS = """
:root{--ink:#14181f;--muted:#5b6675;--line:#e2e5ea;--bg:#fbfbf9;--card:#fff;
  --accent:#7a1420;--accent2:#0b3d5c;--chip:#f1f0ec}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);
  font:16px/1.6 "Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;-webkit-font-smoothing:antialiased}
.sans{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
.wrap{max-width:940px;margin:0 auto;padding:0 22px}
header.masthead{border-bottom:1px solid var(--line);background:#fff}
.masthead .wrap{padding:30px 22px 26px}
.brand{font-size:13px;letter-spacing:.22em;text-transform:uppercase;color:var(--accent);font-weight:700;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
.crumb{font-size:12.5px;color:var(--muted);margin:0 0 6px;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
.crumb a{color:var(--accent2);text-decoration:none}
h1{font-size:33px;line-height:1.15;margin:12px 0 10px;letter-spacing:-.01em}
.lede{color:var(--muted);max-width:66ch;margin:0}
.status{margin:22px 0 0;padding:13px 16px;border:1px solid var(--line);border-left:3px solid var(--accent2);
  background:#fff;border-radius:6px;font-size:14.5px;color:#33404e;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
main{padding:34px 0 10px}
.intro{color:#37414d;max-width:70ch;margin:0 0 30px}
.volume{background:linear-gradient(180deg,#fff, #fbf7f4);border:1px solid #e7ddd6;border-left:4px solid var(--accent);
  border-radius:12px;padding:26px 26px 22px;margin:0 0 34px}
.volume .kk{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--accent);font-weight:800;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
.volume h2{font-size:24px;margin:6px 0 8px}
.volume p{font-size:15px;color:#37414d;margin:0 0 16px;max-width:74ch}
.paper{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:22px 24px 18px;
  margin:0 0 18px;box-shadow:0 1px 2px rgba(20,24,31,.03)}
.paper h2{font-size:20px;line-height:1.3;margin:2px 0 6px;letter-spacing:-.005em}
.paper h2 a{color:var(--ink);text-decoration:none}
.paper h2 a:hover{color:var(--accent)}
.authors{font-size:14px;color:var(--muted);margin:0 0 12px}
.abs{font-size:15px;color:#2c343d;margin:0 0 16px}
.tag{display:inline-block;font-size:11px;letter-spacing:.08em;text-transform:uppercase;font-weight:700;
  color:var(--accent);margin:0 0 8px;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
.meta{display:flex;flex-wrap:wrap;gap:9px;align-items:center;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
a.btn{display:inline-flex;align-items:center;gap:7px;text-decoration:none;font-size:13.5px;font-weight:600;
  padding:8px 14px;border-radius:7px;border:1px solid var(--line);color:var(--accent2);background:#fff}
a.btn:hover{border-color:var(--accent2)}
a.pdf{background:var(--accent);color:#fff;border-color:var(--accent)}
a.pdf:hover{background:#611019}
a.read{background:var(--accent2);color:#fff;border-color:var(--accent2)}
a.read:hover{background:#092d44}
.chip{font-size:12px;color:#6b7480;background:var(--chip);border-radius:20px;padding:5px 11px;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
.res{margin:22px 0 0;border:1px solid var(--line);border-radius:10px;overflow:hidden}
.res .rh{background:#f7f6f2;padding:10px 16px;font-size:12px;letter-spacing:.1em;text-transform:uppercase;
  font-weight:800;color:#55606e;border-bottom:1px solid var(--line);
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
.res .rb{display:flex;flex-wrap:wrap;gap:10px;padding:16px}
.note{font-size:13.5px;color:var(--muted);margin:26px 0 0;padding-top:20px;border-top:1px solid var(--line);
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
.prevnext{display:flex;justify-content:space-between;gap:12px;margin:28px 0 0;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;font-size:14px}
.prevnext a{color:var(--accent2);text-decoration:none}
footer{border-top:1px solid var(--line);margin-top:34px;background:#fff}
footer .wrap{padding:22px;font-size:13px;color:var(--muted);
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
footer a{color:var(--accent2)}
@media(max-width:560px){h1{font-size:26px}.paper{padding:18px}.volume{padding:20px 18px}}
"""

FOOTER = ('<footer><div class="wrap">&copy; 2026 Kronos Fusion Energy, Inc. &middot; '
  'Los Angeles, California &middot; <a href="https://www.kronosfusionenergy.com/">kronosfusionenergy.com</a> '
  '&middot; <a href="' + COMMUNITY + '">Zenodo community</a> &middot; '
  'Correspondence: p.ford@kronosfusionenergy.com</div></footer>')

def resources(p):
    """The connected-resources panel: PDF, DOI(s), community, 3D model, verification."""
    b = [f'<a class="btn pdf" href="{p["pdf"]}">Download PDF ({p["pages"]})</a>']
    b.append(f'<a class="btn" href="https://doi.org/{p["doi"]}">Data &amp; code &middot; doi:{p["doi"].split("/")[-1]}</a>')
    if p.get("doi2"):
        b.append(f'<a class="btn" href="https://doi.org/{p["doi2"]}">Version 2 &middot; doi:{p["doi2"].split("/")[-1]}</a>')
    b.append(f'<a class="btn" href="{COMMUNITY}">Zenodo community</a>')
    b.append(f'<a class="btn" href="{MODEL}">Interactive 3D model</a>')
    label = "Live simulator &amp; verification" if p.get("sim") else "Reproducibility &amp; verification"
    b.append(f'<a class="btn" href="{VERIFY}">{label}</a>')
    return ('<div class="res"><div class="rh">Connected resources</div>'
            '<div class="rb">' + "".join(b) + '</div></div>')

def citation_meta(p):
    m = [f'<meta name="citation_title" content="{p["title"].replace(chr(38)+"ndash;","-").replace(chr(38)+"sup3;","3").replace(chr(38)+"mdash;","-")}">']
    for a in p["authors"]:
        m.append(f'<meta name="citation_author" content="{a}">')
    m.append('<meta name="citation_publication_date" content="2026">')
    m.append(f'<meta name="citation_pdf_url" content="{SITE}/publications/{p["pdf"]}">')
    m.append(f'<meta name="citation_doi" content="{p["doi"]}">')
    m.append(f'<meta name="citation_abstract_html_url" content="{SITE}/publications/{p["slug"]}.html">')
    m.append('<meta name="citation_publisher" content="Kronos Fusion Energy">')
    return "\n".join(m)

def page(title, desc, body, head_extra=""):
    return (f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
      f'<meta name="viewport" content="width=device-width, initial-scale=1">'
      f'<title>{title}</title><meta name="description" content="{desc}">'
      f'<link rel="canonical" href="{SITE}/publications/">'
      f'{head_extra}<style>{CSS}</style></head><body>{body}{FOOTER}</body></html>')

# -------- index.html --------
def build_index():
    cards = []
    for p in PAPERS:
        cards.append(
          f'<article class="paper"><div class="tag">{p["tag"]}</div>'
          f'<h2><a href="{p["slug"]}.html">{p["title"]}</a></h2>'
          f'<p class="authors">{", ".join(p["authors"])} &middot; Kronos Fusion Energy</p>'
          f'<p class="abs">{p["abstract"]}</p>'
          f'<div class="meta"><a class="btn read" href="{p["slug"]}.html">Read the paper page &rarr;</a>'
          f'<a class="btn pdf" href="{p["pdf"]}">PDF ({p["pages"]})</a>'
          f'<a class="btn" href="https://doi.org/{p["doi"]}">doi:{p["doi"].split("/")[-1]}</a>'
          f'<span class="chip">{p["venue"]}</span></div></article>')
    volume = (
      '<div class="volume"><div class="kk">The complete volume</div>'
      f'<h2>{COMPLETE["title"]}</h2><p>{COMPLETE["blurb"]}</p>'
      f'<div class="meta"><a class="btn pdf" href="{COMPLETE["file"]}">Download the complete volume</a>'
      f'<a class="btn" href="complete.html">About this volume &rarr;</a>'
      f'<a class="btn" href="{MODEL}">Interactive 3D model</a>'
      f'<a class="btn" href="{VERIFY}">Live simulator &amp; verification</a></div></div>')
    body = (
      '<header class="masthead"><div class="wrap">'
      '<div class="brand">Kronos Fusion Energy</div>'
      '<h1>Research &amp; Publications</h1>'
      '<p class="lede">A five-paper 2026 design series on a compact fusion isotope and energy '
      'platform &mdash; each paper accompanied by a fully reproducible, openly archived simulation '
      'and data deposit, and available as one complete volume.</p>'
      '<div class="status"><strong>Status.</strong> All five papers are permanently archived and '
      'citable on Zenodo (DOIs below). The spherical-tokamak breeder and the tandem-mirror generator '
      'are under review at <em>Nuclear Fusion</em> (IOP); the AI and quantum control study is under '
      'review at <em>Fusion Engineering &amp; Design</em> (Elsevier). Live in-browser physics '
      'simulators accompany the breeder and generator papers.</div></div></header>'
      '<main class="wrap">'
      '<p class="intro">Every headline number regenerates from a named script and archived data under '
      'a fixed random seed; requirement-class assumptions and open risks are carried openly rather than '
      'absorbed into a single optimum. Each paper below has its own page, linking the manuscript to its '
      'data-and-code deposit, the interactive 3D model, and the live verification simulator.</p>'
      + volume + "".join(cards) +
      '<p class="note">Reproducibility. Each deposit is Open Access (CC BY 4.0) in the '
      f'<a href="{COMMUNITY}">Kronos Fusion Energy Zenodo community</a> and carries a run-all '
      'reproduction driver, pinned computing environment, and per-file checksums. The papers contain '
      'no financial or commercial information.</p></main>')
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(
      page("Publications — Papers, Preprints & Open Data · Kronos Fusion Energy",
           "The Kronos Fusion Energy 2026 design series — breeder, generator, REBCO magnets, direct "
           "energy conversion, and AI/quantum control — with reproducible open data and one complete volume.",
           body))

# -------- per-part detail pages --------
def build_details():
    n = len(PAPERS)
    for i, p in enumerate(PAPERS):
        prev = PAPERS[i-1] if i > 0 else None
        nxt = PAPERS[i+1] if i < n-1 else None
        pn = '<div class="prevnext">'
        pn += (f'<a href="{prev["slug"]}.html">&larr; {prev["tag"]}</a>' if prev else '<a href="index.html">&larr; All publications</a>')
        pn += (f'<a href="{nxt["slug"]}.html">{nxt["tag"]} &rarr;</a>' if nxt else '<a href="complete.html">Complete volume &rarr;</a>')
        pn += '</div>'
        body = (
          '<header class="masthead"><div class="wrap">'
          '<div class="crumb"><a href="index.html">Research &amp; Publications</a> &rsaquo; '
          f'{p["tag"]}</div>'
          '<div class="brand">Kronos Fusion Energy</div>'
          f'<h1>{p["title"]}</h1>'
          f'<p class="lede">{", ".join(p["authors"])} &middot; Kronos Fusion Energy &middot; 2026 '
          f'&middot; <span class="chip">{p["venue"]}</span></p></div></header>'
          '<main class="wrap">'
          f'<div class="tag">{p["tag"]}</div>'
          '<h2 style="font-size:18px;margin:0 0 8px">Abstract</h2>'
          f'<p class="abs">{p["abstract"]}</p>'
          + resources(p) +
          '<p class="note">This paper is Open Access (CC BY 4.0). Every headline number regenerates '
          'from the named script and archived data in the deposit above; requirement-class assumptions '
          'and open risks are stated in the manuscript rather than absorbed into a single optimum. '
          'No financial or commercial information appears in this work.</p>'
          + pn + '</main>')
        open(os.path.join(HERE, p["slug"] + ".html"), "w", encoding="utf-8").write(
          page(p["title"].replace("&ndash;","-").replace("&sup3;","3").replace("&mdash;","—").replace("&amp;","&") + " · Kronos Fusion Energy",
               ("Kronos Fusion Energy 2026 — " + p["tag"].replace("&amp;","&").replace("&ndash;","-").replace("&sup3;","3")
                + ". Open-access paper with reproducible data and code, interactive 3D model, and live verification."),
               body, head_extra=citation_meta(p)))

# -------- complete.html --------
def build_complete():
    parts = "".join(
      f'<li><a href="{p["slug"]}.html">{p["title"]}</a> &middot; '
      f'<a href="https://doi.org/{p["doi"]}">doi:{p["doi"].split("/")[-1]}</a></li>' for p in PAPERS)
    body = (
      '<header class="masthead"><div class="wrap">'
      '<div class="crumb"><a href="index.html">Research &amp; Publications</a> &rsaquo; Complete volume</div>'
      '<div class="brand">Kronos Fusion Energy</div>'
      f'<h1>{COMPLETE["title"]}</h1>'
      f'<p class="lede">{COMPLETE["blurb"]}</p></div></header>'
      '<main class="wrap">'
      f'<div class="meta"><a class="btn pdf" href="{COMPLETE["file"]}">Download the complete volume</a>'
      f'<a class="btn" href="{MODEL}">Interactive 3D model</a>'
      f'<a class="btn" href="{VERIFY}">Live simulator &amp; verification</a>'
      f'<a class="btn" href="{COMMUNITY}">Zenodo community</a></div>'
      '<h2 style="font-size:19px;margin:26px 0 10px">The five parts</h2><ol style="line-height:1.9">'
      + parts + '</ol>'
      '<p class="note">The complete volume collects the five open-access studies (CC BY 4.0) with a '
      'shared methodology and reproducibility manifest. Each part is also individually archived and '
      'citable on Zenodo. No financial or commercial information appears in this work.</p>'
      '<div class="prevnext"><a href="index.html">&larr; All publications</a>'
      f'<a href="{PAPERS[0]["slug"]}.html">Start with the breeder &rarr;</a></div></main>')
    open(os.path.join(HERE, "complete.html"), "w", encoding="utf-8").write(
      page("The Kronos 2026 Publication — Complete Volume · Kronos Fusion Energy",
           "The complete Kronos Fusion Energy 2026 design volume — all five studies in one bound "
           "document, with reproducible open data, interactive 3D model, and live verification.",
           body))

def verify():
    problems = []
    for p in PAPERS:
        fp = os.path.join(HERE, p["pdf"])
        if not os.path.exists(fp): problems.append("MISSING PDF: " + p["pdf"])
    cf = os.path.join(HERE, COMPLETE["file"])
    complete_pdf = "present" if os.path.exists(cf) else "NOT yet supplied (placeholder link)"
    # Firewall: the public repo must NEVER contain an internal/confidential PDF.
    pdir = os.path.join(HERE, "papers")
    if os.path.isdir(pdir):
        for fn in os.listdir(pdir):
            up = fn.upper()
            if "CONFIDENTIAL" in up or "INTERNAL" in up:
                problems.append("CONFIDENTIALITY BREACH: " + fn + " must not be in the public repo")
    return problems, complete_pdf

if __name__ == "__main__":
    build_index(); build_details(); build_complete()
    problems, complete_pdf = verify()
    pages = 1 + len(PAPERS) + 1
    print(f"Generated {pages} pages: index + {len(PAPERS)} part pages + complete.")
    print(f"Complete-volume PDF: {complete_pdf}")
    print("Verification:", "CLEAN" if not problems else problems)
