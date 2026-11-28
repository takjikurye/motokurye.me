#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bodrum Nakliye ve Bodrum Moto Kurye icin EN/RU/DE/FR dil sayfalarini
uretir. Tasarim, moto-kurye-en.html vb. sayfalarda kullanilan sade/odakli
landing page sablonunu (mega-menu degil) temel alir."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PHONE = "+905446018815"

CSS = """<style>
:root{
  --gr:#16A34A;--grd:#15803D;--grl:rgba(22,163,74,0.09);
  --bk:#111827;--wh:#fff;
  --g50:#F3F4F6;--g100:#E5E7EB;--g200:#D1D5DB;--g400:#9CA3AF;--g500:#6B7280;--g700:#374151;
  --or:#EA580C;--ord:#C2410C;
  --fh:'Outfit',-apple-system,'Segoe UI',Arial,sans-serif;--fb:'DM Sans',-apple-system,'Segoe UI',Arial,sans-serif;
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;}
body{font-family:var(--fb);color:var(--bk);background:#fff;overflow-x:hidden;}
a{text-decoration:none;color:inherit;}
header{position:fixed;top:0;left:0;right:0;z-index:100;background:rgba(17,24,39,0.97);backdrop-filter:blur(12px);height:64px;display:flex;align-items:center;justify-content:space-between;padding:0 5%;}
.logo{font-family:var(--fh);font-weight:800;font-size:1.35rem;color:#fff;letter-spacing:-.02em;}
.logo span{color:var(--gr);}
.hd-cta{display:flex;gap:8px;}
.bp,.bor{font-family:var(--fh);font-weight:700;font-size:.82rem;padding:9px 16px;border-radius:8px;display:inline-flex;align-items:center;gap:6px;transition:all .15s;}
.bp{background:var(--gr);color:#fff;}
.bp:hover{background:var(--grd);}
.bor{background:transparent;color:#fff;border:1px solid rgba(255,255,255,.25);}
.bor:hover{border-color:var(--gr);color:var(--gr);}
main{padding-top:64px;}
.hero{background:linear-gradient(180deg,var(--bk) 0%,#1c2532 100%);color:#fff;padding:64px 5% 56px;}
.hero-inner{max-width:900px;margin:0 auto;text-align:center;}
.hero h1{font-family:var(--fh);font-weight:800;font-size:clamp(1.8rem,4vw,3rem);line-height:1.2;margin-bottom:16px;}
.hero h1 em{color:var(--gr);font-style:normal;}
.hero .sub{color:var(--g200);font-size:1.05rem;line-height:1.7;max-width:640px;margin:0 auto 28px;}
.hero-btns{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;}
.hero-btns a{font-size:.95rem;padding:13px 26px;}
.info-strip{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:14px;max-width:900px;margin:36px auto 0;}
.info-card{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);border-radius:12px;padding:16px;text-align:center;}
.info-card .ic{font-size:1.3rem;margin-bottom:6px;}
.info-card .it{font-size:.74rem;color:var(--g400);text-transform:uppercase;letter-spacing:.04em;}
.info-card .iv{font-family:var(--fh);font-weight:700;font-size:.95rem;margin-top:2px;}
.sec{max-width:980px;margin:0 auto;padding:56px 5%;}
.sec h2{font-family:var(--fh);font-weight:800;font-size:clamp(1.4rem,2.6vw,2rem);margin-bottom:22px;}
.svc-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:14px;}
.svc-kart{background:var(--g50);border:1px solid var(--g100);border-radius:12px;padding:18px;transition:border-color .15s;}
.svc-kart:hover{border-color:var(--gr);}
.svc-kart .ic{font-size:1.4rem;margin-bottom:8px;}
.svc-kart h3{font-family:var(--fh);font-weight:700;font-size:.98rem;margin-bottom:6px;}
.svc-kart p{font-size:.85rem;color:var(--g500);line-height:1.55;}
.svc-kart a.more{font-size:.78rem;font-weight:700;color:var(--gr);}
.steps{display:flex;flex-direction:column;gap:18px;margin-top:10px;}
.step{display:flex;gap:16px;align-items:flex-start;}
.step .n{width:40px;height:40px;background:var(--grl);color:var(--gr);border-radius:10px;display:flex;align-items:center;justify-content:center;font-family:var(--fh);font-weight:800;flex-shrink:0;}
.step h3{font-family:var(--fh);font-weight:700;font-size:1rem;margin-bottom:4px;}
.step p{font-size:.88rem;color:var(--g500);line-height:1.6;}
details{background:var(--g50);border:1px solid var(--g100);border-radius:10px;padding:14px 18px;margin-bottom:10px;}
summary{font-family:var(--fh);font-weight:700;font-size:.95rem;cursor:pointer;}
details p{margin-top:10px;font-size:.88rem;color:var(--g500);line-height:1.6;}
.cta-box{background:var(--g50);border:1px solid var(--g100);border-radius:16px;padding:32px;margin-top:10px;display:flex;align-items:center;justify-content:space-between;gap:20px;flex-wrap:wrap;}
.cta-box h2{font-size:1.2rem;margin-bottom:6px;}
.cta-box p{color:var(--g500);font-size:.88rem;}
.regions{display:flex;flex-wrap:wrap;gap:8px;}
.regions a{background:var(--g50);border:1px solid var(--g100);border-radius:8px;padding:8px 14px;font-size:.82rem;color:var(--bk);}
.regions a:hover{border-color:var(--gr);color:var(--gr);}
footer{background:var(--bk);color:var(--g400);padding:40px 5% 24px;text-align:center;}
footer .logo{display:inline-block;margin-bottom:10px;}
footer a{color:var(--g400);}
footer a:hover{color:var(--gr);}
footer .flinks{display:flex;gap:16px;justify-content:center;flex-wrap:wrap;margin:14px 0;font-size:.82rem;}
footer .fbot{font-size:.76rem;margin-top:14px;opacity:.7;}
@media(max-width:640px){.hero{padding:48px 5% 40px;}.sec{padding:40px 5%;}.cta-box{flex-direction:column;text-align:center;}}
</style>"""

GTM = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-18016419258">
</script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'AW-18016419258');
</script>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-KM26MWSV');</script>
<!-- End Google Tag Manager -->"""

NOSCRIPT_GTM = """<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-KM26MWSV"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->"""

LANGS = ["en", "ru", "de", "fr"]
LOCALE = {"en": "en_US", "ru": "ru_RU", "de": "de_DE", "fr": "fr_FR"}


def hreflang_block(slug_base, turkish_url):
    lines = [f'<link rel="alternate" hreflang="tr" href="https://motokurye.me/{turkish_url}">']
    for l in LANGS:
        lines.append(f'<link rel="alternate" hreflang="{l}" href="https://motokurye.me/{slug_base}-{l}.html">')
    lines.append(f'<link rel="alternate" hreflang="x-default" href="https://motokurye.me/{turkish_url}">')
    return "\n".join(lines)


def build_page(lang, slug, title, desc, h1, sub, info, services, services_h2, steps, steps_h2, faq, faq_h2, cta_h2, cta_p, footer_p, footer_priv, breadcrumb_home, breadcrumb_name, page_name_jsonld, service_desc_jsonld, slug_base, turkish_url, regions=None, regions_label=None):
    canonical = f"https://motokurye.me/{slug}.html"
    faq_items = [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]
    graph = [
        {
            "@type": "LocalBusiness", "@id": "https://motokurye.me/#business", "name": "MotoKurye.me",
            "url": "https://motokurye.me/", "telephone": PHONE, "image": "https://motokurye.me/logo.png",
            "logo": {"@type": "ImageObject", "url": "https://motokurye.me/logo.png", "width": 512, "height": 512},
            "priceRange": "₺₺",
            "address": {"@type": "PostalAddress", "addressLocality": "Istanbul", "addressRegion": "Istanbul", "addressCountry": "TR"},
            "openingHoursSpecification": {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"], "opens": "00:00", "closes": "23:59"},
            "areaServed": {"@type": "City", "name": "Istanbul", "sameAs": "https://www.wikidata.org/wiki/Q406"}
        },
        {
            "@type": "Service", "@id": f"{canonical}#service", "name": page_name_jsonld,
            "description": service_desc_jsonld, "provider": {"@id": "https://motokurye.me/#business"},
            "areaServed": {"@type": "AdministrativeArea", "name": "Bodrum", "geo": {"@type": "GeoCoordinates", "latitude": 37.0344, "longitude": 27.4305}, "containedIn": {"@type": "AdministrativeArea", "name": "Muğla"}},
            "serviceType": "Nakliye", "inLanguage": lang,
            "hoursAvailable": {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"], "opens": "00:00", "closes": "23:59"}
        },
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": breadcrumb_home, "item": "https://motokurye.me/"},
            {"@type": "ListItem", "position": 2, "name": breadcrumb_name, "item": canonical}
        ]},
        {"@type": "FAQPage", "mainEntity": faq_items}
    ]
    jsonld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)

    def _svc_card(ic, name, desc_, url, more):
        link = f'<a class="more" href="/{url}">{more}</a>' if url else ""
        return f'      <div class="svc-kart"><div class="ic">{ic}</div><h3>{name}</h3><p>{desc_}</p>{link}</div>'
    svc_html = "\n".join(_svc_card(*s) for s in services)
    steps_html = "\n".join(
        f'      <div class="step"><div class="n">{i+1}</div><div><h3>{t}</h3><p>{p}</p></div></div>'
        for i, (t, p) in enumerate(steps)
    )
    faq_html = "\n".join(
        f'    <details><summary>{q}</summary><p>{a}</p></details>' for q, a in faq
    )
    info_html = "\n".join(
        f'        <div class="info-card"><div class="ic">{ic}</div><div class="it">{label}</div><div class="iv">{val}</div></div>'
        for ic, label, val in info
    )
    regions_html = ""
    if regions:
        items = "".join(f'<a href="/{url}">{name}</a>' for name, url in regions)
        regions_html = f'  <section class="sec"><h2>{regions_label}</h2><div class="regions">{items}</div></section>\n'

    html = f"""<!DOCTYPE html>
<html lang="{lang}"{' dir="rtl"' if lang == 'ar' else ''}>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
{hreflang_block(slug_base, turkish_url)}
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="MotoKurye.me">
<meta property="og:locale" content="{LOCALE[lang]}">
<meta name="robots" content="index,follow">
<link rel="sitemap" href="/sitemap-index.xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Outfit:wght@700;800&family=DM+Sans:wght@400;500&display=swap" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Outfit:wght@700;800&family=DM+Sans:wght@400;500&display=swap"></noscript>
{GTM}
{CSS}
<script type="application/ld+json">
{jsonld}
</script>
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/favicon.svg">
<link rel="manifest" href="/manifest.json">
<meta name="theme-color" content="#16A34A">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@motokurye">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta property="og:image" content="https://motokurye.me/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:image" content="https://motokurye.me/og-image.jpg">
</head>
<body>
{NOSCRIPT_GTM}
<header>
  <a href="/" class="logo">MotoKurye<span>.me</span></a>
  <div class="hd-cta">
    <a href="tel:{PHONE}" class="bor">📞</a>
    <a href="https://wa.me/{PHONE.lstrip('+')}" class="bp">💬 WhatsApp</a>
  </div>
</header>
<main>
  <div class="hero">
    <div class="hero-inner">
      <h1>{h1}</h1>
      <p class="sub">{sub}</p>
      <div class="hero-btns">
        <a href="tel:{PHONE}" class="bp">📞 {PHONE}</a>
        <a href="https://wa.me/{PHONE.lstrip('+')}" class="bor">💬 WhatsApp</a>
      </div>
      <div class="info-strip">
{info_html}
      </div>
    </div>
  </div>

  <section class="sec">
    <h2>{services_h2}</h2>
    <div class="svc-grid">
{svc_html}
    </div>
  </section>

  <section class="sec" style="background:var(--g50);">
    <h2>{steps_h2}</h2>
    <div class="steps">
{steps_html}
    </div>
  </section>

{regions_html}
  <section class="sec">
    <h2>{faq_h2}</h2>
{faq_html}
  </section>

  <section class="sec">
    <div class="cta-box">
      <div><h2>{cta_h2}</h2><p>{cta_p}</p></div>
      <div style="display:flex;gap:10px;flex-wrap:wrap;">
        <a href="tel:{PHONE}" class="bp">📞 {PHONE}</a>
        <a href="https://wa.me/{PHONE.lstrip('+')}" class="bor" style="border-color:var(--g200);color:var(--bk);">💬 WhatsApp</a>
      </div>
    </div>
  </section>
</main>
<footer>
  <a href="/" class="logo">MotoKurye<span>.me</span></a>
  <p>{footer_p}</p>
  <div class="flinks">
    <a href="tel:{PHONE}">📞 {PHONE}</a>
    <a href="https://wa.me/{PHONE.lstrip('+')}">💬 WhatsApp</a>
    <a href="/{turkish_url}">Türkçe sayfa</a>
    <a href="/gizlilik-politikasi.html">{footer_priv}</a>
  </div>
  <div class="fbot">© 2026 MotoKurye.me</div>
</footer>
</body>
</html>
"""
    return html


# ─────────────────────────────────────────────────────────
# BODRUM NAKLIYE (hub) — EN/RU/DE/FR
# ─────────────────────────────────────────────────────────
NAKLIYE_SERVICES = {
    "en": [
        ("🪶", "Light Transport (Doblo)", "Small and medium-sized loads, fast transport with the Doblo.", "bodrum-hafif-nakliye.html", "More →"),
        ("📋", "Partial Load (Transit)", "Medium-volume partial commercial loads with the Transit minibus.", "bodrum-parsiyel-yuk.html", "More →"),
        ("🧱", "Debris Removal", "Construction/renovation debris transport and disposal with an open-bed truck.", "bodrum-moloz-dokum.html", "More →"),
        ("🏗️", "Construction Material", "Bricks, cement, steel and other building materials delivered to the site.", "bodrum-insaat-malzeme-tasima.html", "More →"),
        ("🏠", "Household Goods", "Home-to-home moving with a closed-bed truck — furniture and appliances.", "bodrum-ev-esyasi-tasima.html", "More →"),
        ("🏢", "Office/Workplace Relocation", "Equipment and furniture transport for office and workplace moves.", "bodrum-ofis-isyeri-tasima.html", "More →"),
        ("🚜", "Forklift Rental", "Loading and unloading of pallets and heavy loads with a forklift.", "bodrum-forklift-kiralama.html", "More →"),
        ("🏭", "Manitou (Telehandler) Rental", "High-reach loading on construction sites with a telehandler.", "bodrum-manitou-kiralama.html", "More →"),
        ("🚚", "Tow Truck Service", "Flatbed tow truck for vehicle and heavy equipment transport.", "bodrum-cekici-hizmeti.html", "More →"),
        ("🗺️", "Intercity Transport", "Transport from Bodrum to any province in Turkey, and back.", "bodrum-sehirlerarasi-nakliye.html", "More →"),
    ],
    "ru": [
        ("🪶", "Лёгкая перевозка (Doblo)", "Малые и средние грузы, быстрая перевозка на Doblo.", "bodrum-hafif-nakliye.html", "Подробнее →"),
        ("📋", "Частичный груз (Transit)", "Коммерческие частичные грузы среднего объёма на микроавтобусе Transit.", "bodrum-parsiyel-yuk.html", "Подробнее →"),
        ("🧱", "Вывоз строительного мусора", "Перевозка и вывоз строительного/ремонтного мусора открытым грузовиком.", "bodrum-moloz-dokum.html", "Подробнее →"),
        ("🏗️", "Перевозка стройматериалов", "Доставка кирпича, цемента, металла и других материалов на объект.", "bodrum-insaat-malzeme-tasima.html", "Подробнее →"),
        ("🏠", "Перевозка домашних вещей", "Переезд квартиры закрытым грузовиком — мебель и бытовая техника.", "bodrum-ev-esyasi-tasima.html", "Подробнее →"),
        ("🏢", "Переезд офиса/предприятия", "Перевозка оборудования и мебели при переезде офиса или предприятия.", "bodrum-ofis-isyeri-tasima.html", "Подробнее →"),
        ("🚜", "Аренда вилочного погрузчика", "Погрузка и разгрузка паллет и тяжёлых грузов погрузчиком.", "bodrum-forklift-kiralama.html", "Подробнее →"),
        ("🏭", "Аренда телескопического погрузчика", "Высотная погрузка на стройплощадках телескопическим погрузчиком Manitou.", "bodrum-manitou-kiralama.html", "Подробнее →"),
        ("🚚", "Услуга эвакуатора", "Платформенный эвакуатор для перевозки техники и тяжёлого оборудования.", "bodrum-cekici-hizmeti.html", "Подробнее →"),
        ("🗺️", "Междугородняя перевозка", "Перевозка из Бодрума в любую провинцию Турции и обратно.", "bodrum-sehirlerarasi-nakliye.html", "Подробнее →"),
    ],
    "de": [
        ("🪶", "Leichttransport (Doblo)", "Kleine bis mittlere Lasten, schneller Transport mit dem Doblo.", "bodrum-hafif-nakliye.html", "Mehr →"),
        ("📋", "Teilladung (Transit)", "Gewerbliche Teilladungen mittleren Volumens mit dem Transit-Kleinbus.", "bodrum-parsiyel-yuk.html", "Mehr →"),
        ("🧱", "Bauschuttentsorgung", "Transport und Entsorgung von Bau-/Renovierungsschutt mit offenem Pritschenwagen.", "bodrum-moloz-dokum.html", "Mehr →"),
        ("🏗️", "Baumaterialtransport", "Ziegel, Zement, Stahl und weitere Baumaterialien zur Baustelle.", "bodrum-insaat-malzeme-tasima.html", "Mehr →"),
        ("🏠", "Hausratumzug", "Umzug von Wohnung zu Wohnung mit geschlossenem Pritschenwagen — Möbel und Haushaltsgeräte.", "bodrum-ev-esyasi-tasima.html", "Mehr →"),
        ("🏢", "Büro-/Betriebsumzug", "Transport von Ausstattung und Möbeln bei Büro- oder Betriebsumzügen.", "bodrum-ofis-isyeri-tasima.html", "Mehr →"),
        ("🚜", "Gabelstapler-Vermietung", "Be- und Entladen von Paletten und schweren Lasten mit dem Gabelstapler.", "bodrum-forklift-kiralama.html", "Mehr →"),
        ("🏭", "Teleskoplader-Vermietung (Manitou)", "Hochregal-Beladung auf Baustellen mit dem Teleskoplader.", "bodrum-manitou-kiralama.html", "Mehr →"),
        ("🚚", "Abschleppdienst", "Tieflader-Abschleppwagen für Fahrzeug- und Schwerlasttransport.", "bodrum-cekici-hizmeti.html", "Mehr →"),
        ("🗺️", "Ferntransport", "Transport von Bodrum in jede türkische Provinz und zurück.", "bodrum-sehirlerarasi-nakliye.html", "Mehr →"),
    ],
    "fr": [
        ("🪶", "Transport léger (Doblo)", "Charges petites et moyennes, transport rapide avec le Doblo.", "bodrum-hafif-nakliye.html", "Plus →"),
        ("📋", "Charge partielle (Transit)", "Charges commerciales partielles de volume moyen avec le minibus Transit.", "bodrum-parsiyel-yuk.html", "Plus →"),
        ("🧱", "Évacuation de gravats", "Transport et évacuation de gravats de chantier/rénovation avec camion benne ouverte.", "bodrum-moloz-dokum.html", "Plus →"),
        ("🏗️", "Transport de matériaux", "Briques, ciment, acier et autres matériaux livrés sur le chantier.", "bodrum-insaat-malzeme-tasima.html", "Plus →"),
        ("🏠", "Déménagement de mobilier", "Déménagement d'appartement avec camion benne fermée — meubles et électroménager.", "bodrum-ev-esyasi-tasima.html", "Plus →"),
        ("🏢", "Déménagement de bureau/entreprise", "Transport d'équipement et de mobilier pour les déménagements de bureau.", "bodrum-ofis-isyeri-tasima.html", "Plus →"),
        ("🚜", "Location de chariot élévateur", "Chargement et déchargement de palettes et charges lourdes.", "bodrum-forklift-kiralama.html", "Plus →"),
        ("🏭", "Location de chariot télescopique (Manitou)", "Chargement en hauteur sur les chantiers avec le chariot télescopique.", "bodrum-manitou-kiralama.html", "Plus →"),
        ("🚚", "Service de remorquage", "Dépanneuse à plateau pour le transport de véhicules et d'équipements lourds.", "bodrum-cekici-hizmeti.html", "Plus →"),
        ("🗺️", "Transport interurbain", "Transport depuis Bodrum vers toute province turque, et retour.", "bodrum-sehirlerarasi-nakliye.html", "Plus →"),
    ],
}

NAKLIYE_STEPS = {
    "en": [
        ("Request", "Call or message us on WhatsApp with the type and quantity of items to be moved."),
        ("Assessment", "We plan the right vehicle and crew based on quantity, floor/elevator access and distance."),
        ("Transport", "Items are loaded and transported safely on the agreed date."),
        ("Delivery", "Items are unloaded at the destination; assembly is done on request."),
    ],
    "ru": [
        ("Заявка", "Позвоните или напишите в WhatsApp, указав тип и количество груза."),
        ("Оценка", "Подбираем подходящий транспорт и бригаду по объёму, наличию этажа/лифта и расстоянию."),
        ("Перевозка", "Груз загружается и безопасно перевозится в согласованную дату."),
        ("Доставка", "Груз выгружается по адресу назначения; по запросу выполняется сборка."),
    ],
    "de": [
        ("Anfrage", "Rufen Sie an oder schreiben Sie per WhatsApp mit Art und Menge der zu transportierenden Güter."),
        ("Bewertung", "Wir planen Fahrzeug und Team passend zu Menge, Etage/Aufzug und Entfernung."),
        ("Transport", "Die Güter werden am vereinbarten Termin sicher beladen und transportiert."),
        ("Lieferung", "Entladung am Zielort; auf Wunsch erfolgt die Montage."),
    ],
    "fr": [
        ("Demande", "Appelez-nous ou écrivez sur WhatsApp en précisant le type et la quantité des objets à déplacer."),
        ("Évaluation", "Nous planifions le véhicule et l'équipe adaptés selon la quantité, l'étage/ascenseur et la distance."),
        ("Transport", "Chargement et transport sécurisé à la date convenue."),
        ("Livraison", "Déchargement à destination ; montage sur demande."),
    ],
}

NAKLIYE_FAQ = {
    "en": [
        ("Which moving/transport services do you offer in Bodrum?", "We offer household goods, holiday-home goods, single-item, office/workplace, boat/yacht equipment, tradesman/e-commerce goods, urgent and intercity transport services."),
        ("Can you give a fixed price for transport?", "No, the price depends on distance, floor/elevator access, quantity of items and seasonal demand; message us on WhatsApp for an exact quote."),
        ("Is your transport insured?", "Yes, we provide insured transport."),
        ("Can you move items on streets closed to vehicle traffic?", "No, we cannot serve areas closed to vehicle traffic (pedestrian zones, etc.); transport has to be door-to-door."),
        ("Which areas of Bodrum do you serve?", "We serve the whole Bodrum peninsula; check our region-based courier pages for your specific area."),
        ("I'm not sure which transport page I need — what should I do?", "Just tell us your situation by phone or WhatsApp; we'll work out the right service and vehicle together."),
    ],
    "ru": [
        ("Какие услуги перевозки вы предлагаете в Бодруме?", "Домашние вещи, вещи для летнего дома, отдельные предметы, офисное/коммерческое имущество, оборудование для яхт/катеров, товары для торговли и интернет-магазинов, срочная и междугородняя перевозка."),
        ("Можете назвать фиксированную цену за перевозку?", "Нет, цена зависит от расстояния, этажа/наличия лифта, объёма груза и сезонного спроса; напишите нам в WhatsApp для точного расчёта."),
        ("Ваши перевозки застрахованы?", "Да, мы осуществляем застрахованную перевозку."),
        ("Можете перевозить груз на улицах, закрытых для автотранспорта?", "Нет, мы не обслуживаем зоны, закрытые для автотранспорта (пешеходные зоны и т.п.); перевозка должна быть «от двери до двери»."),
        ("В какие районы Бодрума вы предоставляете услуги?", "Мы обслуживаем весь полуостров Бодрум; страницы курьерской доставки по районам помогут найти информацию по вашему району."),
        ("Не уверен, какую страницу перевозки мне нужно посмотреть — что делать?", "Просто расскажите о своей ситуации по телефону или в WhatsApp — мы вместе определим подходящую услугу и транспорт."),
    ],
    "de": [
        ("Welche Transportdienste bieten Sie in Bodrum an?", "Hausrat, Ferienhaus-Gegenstände, Einzelstücke, Büro-/Betriebsgüter, Boots-/Yachtausstattung, Waren für Gewerbe und E-Commerce, Eiltransport und Ferntransport."),
        ("Können Sie einen Festpreis für den Transport nennen?", "Nein, der Preis richtet sich nach Entfernung, Etage/Aufzug, Menge der Güter und saisonaler Nachfrage; schreiben Sie uns für ein genaues Angebot per WhatsApp."),
        ("Ist Ihr Transport versichert?", "Ja, wir führen versicherten Transport durch."),
        ("Können Sie in für den Fahrzeugverkehr gesperrten Straßen transportieren?", "Nein, wir können keine für den Fahrzeugverkehr gesperrten Bereiche (Fußgängerzonen usw.) bedienen; der Transport muss von Tür zu Tür erfolgen."),
        ("Welche Gebiete in Bodrum bedienen Sie?", "Wir bedienen die gesamte Halbinsel Bodrum; unsere regionalen Kurierseiten geben Auskunft zu Ihrem Gebiet."),
        ("Ich bin mir nicht sicher, welche Transportseite ich ansehen soll — was soll ich tun?", "Schildern Sie uns einfach Ihre Situation per Telefon oder WhatsApp; gemeinsam ermitteln wir den passenden Service und das passende Fahrzeug."),
    ],
    "fr": [
        ("Quels services de transport proposez-vous à Bodrum ?", "Mobilier, affaires de maison de vacances, objets uniques, biens de bureau/entreprise, équipement de bateau/yacht, marchandises pour commerçants et e-commerce, transport urgent et interurbain."),
        ("Pouvez-vous donner un prix fixe pour le transport ?", "Non, le prix dépend de la distance, de l'étage/ascenseur, de la quantité d'objets et de la demande saisonnière ; écrivez-nous sur WhatsApp pour un devis exact."),
        ("Votre transport est-il assuré ?", "Oui, nous effectuons un transport assuré."),
        ("Pouvez-vous transporter dans des rues fermées à la circulation ?", "Non, nous ne pouvons pas desservir les zones fermées à la circulation (zones piétonnes, etc.) ; le transport doit se faire de porte à porte."),
        ("Quelles zones de Bodrum desservez-vous ?", "Nous desservons toute la péninsule de Bodrum ; nos pages de coursier par région donnent les informations pour votre zone."),
        ("Je ne sais pas quelle page de transport consulter, que faire ?", "Expliquez-nous simplement votre situation par téléphone ou WhatsApp ; nous déterminerons ensemble le service et le véhicule adaptés."),
    ],
}

NAKLIYE_TXT = {
    "en": dict(
        title="Bodrum Moving & Transport Services | MotoKurye.me",
        desc="Reliable moving and transport in Bodrum: household goods, office relocation, construction material, debris removal, forklift/Manitou rental and intercity transport.",
        h1="Bodrum Moving &amp; Transport <em>Services</em>",
        sub="Reliable transport in Bodrum — from household goods to office relocation, from single items to intercity moving.",
        info=[("📍","Region","Bodrum"),("🚐","Vehicles","Doblo / Van / Truck"),("⏰","Service hours","24/7 — 365 days"),("🛡️","Transport","Insured")],
        services_h2="Our Services", steps_h2="How It Works", faq_h2="Frequently Asked Questions",
        cta_h2="Request Bodrum Moving &amp; Transport Service", cta_p="Available 24/7 · Insured transport",
        footer_p="Professional moving and transport services across the Bodrum peninsula.", footer_priv="Privacy Policy",
        breadcrumb_home="Home", breadcrumb_name="Bodrum Moving and Transport Service",
        page_name_jsonld="Bodrum Moving and Transport Service",
        service_desc_jsonld="Moving and transport service covering household goods, office relocation, construction material, debris removal, forklift/Manitou rental, tow truck and intercity transport across the Bodrum peninsula.",
        regions_label="Bodrum Area Courier Pages",
    ),
    "ru": dict(
        title="Перевозки и транспортировка в Бодруме | MotoKurye.me",
        desc="Надёжные услуги перевозки в Бодруме: домашние вещи, переезд офиса, стройматериалы, вывоз мусора, аренда погрузчика/Manitou и междугородние перевозки.",
        h1="Услуги перевозки и транспортировки <em>в Бодруме</em>",
        sub="Надёжные транспортные услуги в Бодруме — от перевозки домашних вещей до переезда офиса, от доставки одного предмета до междугородних перевозок.",
        info=[("📍","Регион","Бодрум"),("🚐","Транспорт","Doblo / Фургон / Грузовик"),("⏰","Режим работы","24/7 — 365 дней"),("🛡️","Перевозка","Застрахована")],
        services_h2="Наши услуги", steps_h2="Как это работает", faq_h2="Часто задаваемые вопросы",
        cta_h2="Оставить заявку на перевозку в Бодруме", cta_p="Доступно 24/7 · Застрахованная перевозка",
        footer_p="Профессиональные услуги перевозки по всему полуострову Бодрум.", footer_priv="Политика конфиденциальности",
        breadcrumb_home="Главная", breadcrumb_name="Услуга перевозки и транспортировки в Бодруме",
        page_name_jsonld="Услуга перевозки и транспортировки в Бодруме",
        service_desc_jsonld="Услуга перевозки, включающая домашние вещи, переезд офиса, стройматериалы, вывоз мусора, аренду погрузчика/Manitou, эвакуатор и междугородние перевозки по всему полуострову Бодрум.",
        regions_label="Страницы курьерской доставки по районам Бодрума",
    ),
    "de": dict(
        title="Umzugs- und Transportservice in Bodrum | MotoKurye.me",
        desc="Zuverlässiger Umzugs- und Transportservice in Bodrum: Hausrat, Büroumzug, Baumaterial, Bauschuttentsorgung, Gabelstapler-/Manitou-Vermietung und Ferntransport.",
        h1="Umzugs- und Transportservice <em>in Bodrum</em>",
        sub="Zuverlässiger Transportservice in Bodrum — von Hausratsumzug bis Büroumzug, von Einzelstücken bis zum Ferntransport.",
        info=[("📍","Region","Bodrum"),("🚐","Fahrzeuge","Doblo / Transporter / LKW"),("⏰","Servicezeiten","24/7 — 365 Tage"),("🛡️","Transport","Versichert")],
        services_h2="Unsere Leistungen", steps_h2="So funktioniert's", faq_h2="Häufig gestellte Fragen",
        cta_h2="Umzugs- und Transportservice in Bodrum anfragen", cta_p="24/7 verfügbar · Versicherter Transport",
        footer_p="Professioneller Umzugs- und Transportservice auf der gesamten Halbinsel Bodrum.", footer_priv="Datenschutzerklärung",
        breadcrumb_home="Startseite", breadcrumb_name="Umzugs- und Transportservice in Bodrum",
        page_name_jsonld="Umzugs- und Transportservice in Bodrum",
        service_desc_jsonld="Umzugs- und Transportservice mit Hausrat, Büroumzug, Baumaterialtransport, Bauschuttentsorgung, Gabelstapler-/Manitou-Vermietung, Abschleppdienst und Ferntransport auf der Halbinsel Bodrum.",
        regions_label="Kurierseiten für Bodrum-Gebiete",
    ),
    "fr": dict(
        title="Service de déménagement et transport à Bodrum | MotoKurye.me",
        desc="Service de déménagement et transport fiable à Bodrum : mobilier, déménagement de bureau, matériaux de construction, évacuation de gravats, location de chariot/Manitou et transport interurbain.",
        h1="Service de déménagement et transport <em>à Bodrum</em>",
        sub="Service de transport fiable à Bodrum — du déménagement de mobilier au déménagement de bureau, d'un objet unique au transport interurbain.",
        info=[("📍","Région","Bodrum"),("🚐","Véhicules","Doblo / Fourgon / Camion"),("⏰","Horaires","24/7 — 365 jours"),("🛡️","Transport","Assuré")],
        services_h2="Nos services", steps_h2="Comment ça marche", faq_h2="Questions fréquentes",
        cta_h2="Demander un service de déménagement à Bodrum", cta_p="Disponible 24/7 · Transport assuré",
        footer_p="Service professionnel de déménagement et transport sur toute la péninsule de Bodrum.", footer_priv="Politique de confidentialité",
        breadcrumb_home="Accueil", breadcrumb_name="Service de déménagement et transport à Bodrum",
        page_name_jsonld="Service de déménagement et transport à Bodrum",
        service_desc_jsonld="Service de déménagement et transport couvrant le mobilier, le déménagement de bureau, les matériaux de construction, l'évacuation de gravats, la location de chariot/Manitou, le remorquage et le transport interurbain sur la péninsule de Bodrum.",
        regions_label="Pages de coursier par zone de Bodrum",
    ),
}

for lang in LANGS:
    t = NAKLIYE_TXT[lang]
    html = build_page(
        lang=lang, slug=f"bodrum-nakliye-{lang}",
        title=t["title"], desc=t["desc"], h1=t["h1"], sub=t["sub"], info=t["info"],
        services=NAKLIYE_SERVICES[lang], services_h2=t["services_h2"],
        steps=NAKLIYE_STEPS[lang], steps_h2=t["steps_h2"],
        faq=NAKLIYE_FAQ[lang], faq_h2=t["faq_h2"],
        cta_h2=t["cta_h2"], cta_p=t["cta_p"],
        footer_p=t["footer_p"], footer_priv=t["footer_priv"],
        breadcrumb_home=t["breadcrumb_home"], breadcrumb_name=t["breadcrumb_name"],
        page_name_jsonld=t["page_name_jsonld"], service_desc_jsonld=t["service_desc_jsonld"],
        slug_base="bodrum-nakliye", turkish_url="bodrum-nakliye.html",
    )
    (ROOT / f"bodrum-nakliye-{lang}.html").write_text(html, encoding="utf-8")
    print(f"wrote bodrum-nakliye-{lang}.html")


# ─────────────────────────────────────────────────────────
# BODRUM MOTO KURYE — EN/RU/DE/FR
# ─────────────────────────────────────────────────────────
MK_SERVICES = {
    "en": [
        ("🏨","Hotels, Pensions & Restaurants","Missing supplies, documents and urgent procurement for hospitality businesses.",None,None),
        ("⛵","Yacht & Marina Businesses","Spare parts, documents and small packages to Milta Bodrum, Yalıkavak and D-Marin Turgutreis marinas.","bodrum-tekne-yat-malzeme-tasima.html","More →"),
        ("🛍️","Shops & E-commerce Sellers","Order delivery with cash or card payment collected on delivery.","kapida-odeme-kurye.html","More →"),
        ("💊","Pharmacy & Medical Delivery","Medicine and medical supplies picked up and delivered across Bodrum.","eczane-medikal-kurye.html","More →"),
        ("💐","Flowers, Gifts & Documents","Flowers, gifts and official documents for individual customers.",None,None),
        ("🏠","Villa & Holiday-Home Owners","Keys, documents, invoices and seasonal items delivered to villas and holiday homes.",None,None),
    ],
    "ru": [
        ("🏨","Отели, пансионы и рестораны","Недостающие товары, документы и срочное снабжение для гостиничного бизнеса.",None,None),
        ("⛵","Яхты и бизнес на маринах","Запчасти, документы и небольшие посылки на марины Milta Bodrum, Yalıkavak и D-Marin Turgutreis.","bodrum-tekne-yat-malzeme-tasima.html","Подробнее →"),
        ("🛍️","Магазины и интернет-продавцы","Доставка заказов с оплатой наличными или картой при получении.","kapida-odeme-kurye.html","Подробнее →"),
        ("💊","Аптечная и медицинская доставка","Получение и доставка лекарств и медицинских товаров по всему Бодруму.","eczane-medikal-kurye.html","Подробнее →"),
        ("💐","Цветы, подарки и документы","Цветы, подарки и официальные документы для частных клиентов.",None,None),
        ("🏠","Владельцы вилл и летних домов","Доставка ключей, документов, счетов и сезонных вещей на виллы и в летние дома.",None,None),
    ],
    "de": [
        ("🏨","Hotels, Pensionen & Restaurants","Fehlende Vorräte, Dokumente und dringende Beschaffung für das Gastgewerbe.",None,None),
        ("⛵","Yacht- und Marina-Betriebe","Ersatzteile, Dokumente und kleine Pakete zu den Marinas Milta Bodrum, Yalıkavak und D-Marin Turgutreis.","bodrum-tekne-yat-malzeme-tasima.html","Mehr →"),
        ("🛍️","Geschäfte & Onlinehändler","Bestelllieferung mit Bar- oder Kartenzahlung bei Zustellung.","kapida-odeme-kurye.html","Mehr →"),
        ("💊","Apotheken- und Medizinlieferung","Abholung und Zustellung von Medikamenten und medizinischem Bedarf in ganz Bodrum.","eczane-medikal-kurye.html","Mehr →"),
        ("💐","Blumen, Geschenke & Dokumente","Blumen, Geschenke und offizielle Dokumente für Privatkunden.",None,None),
        ("🏠","Villa- und Ferienhausbesitzer","Zustellung von Schlüsseln, Dokumenten, Rechnungen und saisonalen Gegenständen an Villen und Ferienhäuser.",None,None),
    ],
    "fr": [
        ("🏨","Hôtels, pensions & restaurants","Fournitures manquantes, documents et approvisionnement urgent pour l'hôtellerie.",None,None),
        ("⛵","Yachts & entreprises de marina","Pièces détachées, documents et petits colis vers les marinas Milta Bodrum, Yalıkavak et D-Marin Turgutreis.","bodrum-tekne-yat-malzeme-tasima.html","Plus →"),
        ("🛍️","Boutiques & vendeurs e-commerce","Livraison de commandes avec paiement en espèces ou par carte à la livraison.","kapida-odeme-kurye.html","Plus →"),
        ("💊","Livraison pharmacie & médicale","Récupération et livraison de médicaments et de matériel médical dans tout Bodrum.","eczane-medikal-kurye.html","Plus →"),
        ("💐","Fleurs, cadeaux & documents","Fleurs, cadeaux et documents officiels pour les particuliers.",None,None),
        ("🏠","Propriétaires de villas & maisons de vacances","Clés, documents, factures et effets saisonniers livrés aux villas et maisons de vacances.",None,None),
    ],
}

MK_STEPS = {
    "en": [
        ("Request", "Call or WhatsApp us with the pickup address, delivery address and the type of item (document, package, flower, medicine, etc.)."),
        ("Address Details", "Add the neighborhood name and, if possible, a location pin — street names can repeat in Bodrum, so this speeds up delivery."),
        ("Pickup & Delivery", "Our courier picks up and delivers the same day across the Bodrum peninsula."),
    ],
    "ru": [
        ("Заявка", "Позвоните или напишите в WhatsApp, указав адрес получения, адрес доставки и тип отправления (документ, посылка, цветы, лекарства и т.д.)."),
        ("Детали адреса", "Укажите название района и, если возможно, геометку — названия улиц в Бодруме могут повторяться, это ускорит доставку."),
        ("Получение и доставка", "Наш курьер забирает и доставляет отправление в тот же день по всему полуострову Бодрум."),
    ],
    "de": [
        ("Anfrage", "Rufen Sie an oder schreiben Sie per WhatsApp mit Abhol- und Zustelladresse sowie der Art der Sendung (Dokument, Paket, Blumen, Medikamente usw.)."),
        ("Adressdetails", "Geben Sie den Stadtteilnamen und möglichst einen Standort-Pin an — Straßennamen können sich in Bodrum wiederholen, das beschleunigt die Zustellung."),
        ("Abholung & Zustellung", "Unser Kurier holt ab und liefert noch am selben Tag auf der gesamten Halbinsel Bodrum."),
    ],
    "fr": [
        ("Demande", "Appelez-nous ou écrivez sur WhatsApp avec l'adresse de départ, l'adresse de livraison et le type d'envoi (document, colis, fleurs, médicaments, etc.)."),
        ("Détails d'adresse", "Indiquez le nom du quartier et, si possible, une position GPS — les noms de rues peuvent se répéter à Bodrum, ce qui accélère la livraison."),
        ("Collecte & livraison", "Notre coursier collecte et livre le jour même sur toute la péninsule de Bodrum."),
    ],
}

MK_FAQ = {
    "en": [
        ("How do I request a courier in Bodrum?", "Reach us by phone or WhatsApp with the pickup address, delivery address and the type of item. Adding the neighborhood name and a location pin speeds things up, since street names can repeat in Bodrum."),
        ("Which areas of Bodrum do you serve?", "Bodrum Merkez, Gümbet, Bitez, Akyarlar, Ortakent, Müskebi, Yahşi, Turgutreis, Gümüşlük, Yalıkavak, Gündoğan, Gölköy, Türkbükü, Torba, Güvercinlik, Konacık and Çırkan, among others. Message us for an address not listed and we'll confirm availability."),
        ("Do you deliver to areas far from the center, like Yalıkavak or Türkbükü?", "Yes. Yalıkavak is about 18 km from the district center and Türkbükü about 15 km; price and time depend on the distance between the pickup and delivery addresses, so share both for an exact answer."),
        ("Can you deliver to a marina, yacht or boat?", "Yes — share the marina name (Milta Bodrum, Yalıkavak Marina, D-Marin Turgutreis, etc.), the pier/pontoon, the boat name and the recipient's phone number."),
        ("How are price and delivery time determined?", "Both depend on the distance between the pickup and delivery addresses, the priority (urgent or standard) and the type of item; message the addresses on WhatsApp for an exact quote."),
        ("Is cash on delivery available?", "Yes, cash or card payment can be collected at the moment of delivery — see our cash-on-delivery courier page for details."),
    ],
    "ru": [
        ("Как заказать курьера в Бодруме?", "Свяжитесь с нами по телефону или WhatsApp, указав адрес получения, адрес доставки и тип отправления. Указание названия района и геометки ускоряет доставку, так как названия улиц в Бодруме могут повторяться."),
        ("В какие районы Бодрума вы предоставляете услуги?", "Bodrum Merkez, Gümbet, Bitez, Akyarlar, Ortakent, Müskebi, Yahşi, Turgutreis, Gümüşlük, Yalıkavak, Gündoğan, Gölköy, Türkbükü, Torba, Güvercinlik, Konacık, Çırkan и другие. Напишите нам для адреса не из списка — уточним возможность доставки."),
        ("Доставляете ли вы в отдалённые от центра районы, такие как Yalıkavak или Türkbükü?", "Да. Yalıkavak находится примерно в 18 км от центра района, Türkbükü — примерно в 15 км; цена и время зависят от расстояния между адресами получения и доставки, поэтому укажите оба адреса для точного ответа."),
        ("Можете доставить на марину, яхту или катер?", "Да — укажите название марины (Milta Bodrum, Yalıkavak Marina, D-Marin Turgutreis и т.д.), причал/понтон, название судна и телефон получателя."),
        ("Как определяются цена и время доставки?", "Оба параметра зависят от расстояния между адресами получения и доставки, приоритета (срочно или стандарт) и типа отправления; напишите адреса в WhatsApp для точного расчёта."),
        ("Доступна ли оплата при получении?", "Да, при доставке можно оплатить наличными или картой — подробности на нашей странице курьерской доставки с оплатой при получении."),
    ],
    "de": [
        ("Wie bestelle ich einen Kurier in Bodrum?", "Kontaktieren Sie uns per Telefon oder WhatsApp mit Abholadresse, Zustelladresse und Art der Sendung. Die Angabe des Stadtteilnamens und eines Standort-Pins beschleunigt die Zustellung, da sich Straßennamen in Bodrum wiederholen können."),
        ("Welche Gebiete in Bodrum bedienen Sie?", "Unter anderem Bodrum Merkez, Gümbet, Bitez, Akyarlar, Ortakent, Müskebi, Yahşi, Turgutreis, Gümüşlük, Yalıkavak, Gündoğan, Gölköy, Türkbükü, Torba, Güvercinlik, Konacık und Çırkan. Schreiben Sie uns für eine nicht gelistete Adresse — wir bestätigen die Verfügbarkeit."),
        ("Liefern Sie auch in zentrumsferne Gebiete wie Yalıkavak oder Türkbükü?", "Ja. Yalıkavak liegt etwa 18 km, Türkbükü etwa 15 km vom Bezirkszentrum entfernt; Preis und Zeit richten sich nach der Entfernung zwischen Abhol- und Zustelladresse — teilen Sie beide für eine genaue Auskunft mit."),
        ("Können Sie zu einer Marina, Yacht oder einem Boot liefern?", "Ja — teilen Sie den Namen der Marina (Milta Bodrum, Yalıkavak Marina, D-Marin Turgutreis usw.), Steg/Ponton, den Namen des Boots und die Telefonnummer des Empfängers mit."),
        ("Wie werden Preis und Lieferzeit bestimmt?", "Beides richtet sich nach der Entfernung zwischen Abhol- und Zustelladresse, der Priorität (dringend oder standard) und der Art der Sendung; schreiben Sie die Adressen für ein genaues Angebot per WhatsApp."),
        ("Ist Nachnahme (Zahlung bei Zustellung) möglich?", "Ja, bei der Zustellung kann bar oder mit Karte bezahlt werden — Details auf unserer Seite zum Nachnahme-Kurierdienst."),
    ],
    "fr": [
        ("Comment demander un coursier à Bodrum ?", "Contactez-nous par téléphone ou WhatsApp avec l'adresse de départ, l'adresse de livraison et le type d'envoi. Indiquer le nom du quartier et une position GPS accélère la livraison, car les noms de rues peuvent se répéter à Bodrum."),
        ("Quelles zones de Bodrum desservez-vous ?", "Notamment Bodrum Merkez, Gümbet, Bitez, Akyarlar, Ortakent, Müskebi, Yahşi, Turgutreis, Gümüşlük, Yalıkavak, Gündoğan, Gölköy, Türkbükü, Torba, Güvercinlik, Konacık et Çırkan. Écrivez-nous pour une adresse non listée, nous confirmerons la disponibilité."),
        ("Livrez-vous dans des zones éloignées du centre comme Yalıkavak ou Türkbükü ?", "Oui. Yalıkavak se trouve à environ 18 km du centre du district, Türkbükü à environ 15 km ; le prix et le délai dépendent de la distance entre les adresses de départ et de livraison — indiquez les deux pour une réponse exacte."),
        ("Pouvez-vous livrer à une marina, un yacht ou un bateau ?", "Oui — indiquez le nom de la marina (Milta Bodrum, Yalıkavak Marina, D-Marin Turgutreis, etc.), le quai/ponton, le nom du bateau et le téléphone du destinataire."),
        ("Comment sont déterminés le prix et le délai de livraison ?", "Les deux dépendent de la distance entre les adresses de départ et de livraison, de la priorité (urgent ou standard) et du type d'envoi ; écrivez les adresses sur WhatsApp pour un devis exact."),
        ("Le paiement à la livraison est-il possible ?", "Oui, le paiement en espèces ou par carte peut être collecté au moment de la livraison — voir notre page de coursier avec paiement à la livraison pour plus de détails."),
    ],
}

MK_TXT = {
    "en": dict(
        title="Bodrum Motorcycle Courier | MotoKurye.me",
        desc="Motorcycle courier across the whole Bodrum peninsula: documents, packages, flowers and medicine to Merkez, Gümbet, Bitez, Ortakent, Turgutreis, Yalıkavak, Türkbükü and more.",
        h1="Bodrum Motorcycle <em>Courier</em>",
        sub="Document, package, flower and medicine delivery across the whole Bodrum peninsula — Merkez, Gümbet, Bitez, Ortakent, Turgutreis, Yalıkavak, Türkbükü and more.",
        info=[("📍","Coverage","Whole Bodrum peninsula"),("🏍️","Delivery","Documents, packages, flowers, medicine"),("⏰","Service hours","24/7"),("💳","Payment","Cash/card on delivery available")],
        services_h2="Who Uses Our Bodrum Courier", steps_h2="How It Works", faq_h2="Frequently Asked Questions",
        cta_h2="Request Bodrum Motorcycle Courier", cta_p="24/7 across the whole Bodrum peninsula",
        footer_p="Fast motorcycle courier service across the whole Bodrum peninsula.", footer_priv="Privacy Policy",
        breadcrumb_home="Home", breadcrumb_name="Bodrum Motorcycle Courier",
        page_name_jsonld="Bodrum Motorcycle Courier Service",
        service_desc_jsonld="Motorcycle courier service for documents, packages, flowers and medicine across the whole Bodrum peninsula, including Merkez, Gümbet, Bitez, Ortakent, Turgutreis, Yalıkavak and Türkbükü.",
        regions_label="Bodrum Area Courier Pages",
    ),
    "ru": dict(
        title="Мотокурьер в Бодруме | MotoKurye.me",
        desc="Мотокурьерская доставка по всему полуострову Бодрум: документы, посылки, цветы и лекарства в Merkez, Gümbet, Bitez, Ortakent, Turgutreis, Yalıkavak, Türkbükü и другие районы.",
        h1="Мотокурьер <em>в Бодруме</em>",
        sub="Доставка документов, посылок, цветов и лекарств по всему полуострову Бодрум — Merkez, Gümbet, Bitez, Ortakent, Turgutreis, Yalıkavak, Türkbükü и другие районы.",
        info=[("📍","Зона покрытия","Весь полуостров Бодрум"),("🏍️","Доставка","Документы, посылки, цветы, лекарства"),("⏰","Режим работы","24/7"),("💳","Оплата","Наличные/карта при получении")],
        services_h2="Кто пользуется нашей курьерской службой в Бодруме", steps_h2="Как это работает", faq_h2="Часто задаваемые вопросы",
        cta_h2="Заказать мотокурьера в Бодруме", cta_p="24/7 по всему полуострову Бодрум",
        footer_p="Быстрая мотокурьерская доставка по всему полуострову Бодрум.", footer_priv="Политика конфиденциальности",
        breadcrumb_home="Главная", breadcrumb_name="Мотокурьер в Бодруме",
        page_name_jsonld="Услуга мотокурьерской доставки в Бодруме",
        service_desc_jsonld="Мотокурьерская доставка документов, посылок, цветов и лекарств по всему полуострову Бодрум, включая Merkez, Gümbet, Bitez, Ortakent, Turgutreis, Yalıkavak и Türkbükü.",
        regions_label="Страницы курьерской доставки по районам Бодрума",
    ),
    "de": dict(
        title="Motorrad-Kurier Bodrum | MotoKurye.me",
        desc="Motorrad-Kurierdienst auf der gesamten Halbinsel Bodrum: Dokumente, Pakete, Blumen und Medikamente nach Merkez, Gümbet, Bitez, Ortakent, Turgutreis, Yalıkavak, Türkbükü und mehr.",
        h1="Motorrad-Kurier <em>Bodrum</em>",
        sub="Zustellung von Dokumenten, Paketen, Blumen und Medikamenten auf der gesamten Halbinsel Bodrum — Merkez, Gümbet, Bitez, Ortakent, Turgutreis, Yalıkavak, Türkbükü und mehr.",
        info=[("📍","Abdeckung","Gesamte Halbinsel Bodrum"),("🏍️","Zustellung","Dokumente, Pakete, Blumen, Medikamente"),("⏰","Servicezeiten","24/7"),("💳","Zahlung","Bar/Karte bei Zustellung möglich")],
        services_h2="Wer unseren Kurierdienst in Bodrum nutzt", steps_h2="So funktioniert's", faq_h2="Häufig gestellte Fragen",
        cta_h2="Motorrad-Kurier in Bodrum anfragen", cta_p="24/7 auf der gesamten Halbinsel Bodrum",
        footer_p="Schneller Motorrad-Kurierdienst auf der gesamten Halbinsel Bodrum.", footer_priv="Datenschutzerklärung",
        breadcrumb_home="Startseite", breadcrumb_name="Motorrad-Kurier Bodrum",
        page_name_jsonld="Motorrad-Kurierdienst Bodrum",
        service_desc_jsonld="Motorrad-Kurierdienst für Dokumente, Pakete, Blumen und Medikamente auf der gesamten Halbinsel Bodrum, einschließlich Merkez, Gümbet, Bitez, Ortakent, Turgutreis, Yalıkavak und Türkbükü.",
        regions_label="Kurierseiten für Bodrum-Gebiete",
    ),
    "fr": dict(
        title="Coursier moto Bodrum | MotoKurye.me",
        desc="Service de coursier moto sur toute la péninsule de Bodrum : documents, colis, fleurs et médicaments vers Merkez, Gümbet, Bitez, Ortakent, Turgutreis, Yalıkavak, Türkbükü et plus.",
        h1="Coursier moto <em>à Bodrum</em>",
        sub="Livraison de documents, colis, fleurs et médicaments sur toute la péninsule de Bodrum — Merkez, Gümbet, Bitez, Ortakent, Turgutreis, Yalıkavak, Türkbükü et plus.",
        info=[("📍","Couverture","Toute la péninsule de Bodrum"),("🏍️","Livraison","Documents, colis, fleurs, médicaments"),("⏰","Horaires","24/7"),("💳","Paiement","Espèces/carte à la livraison possible")],
        services_h2="Qui utilise notre coursier à Bodrum", steps_h2="Comment ça marche", faq_h2="Questions fréquentes",
        cta_h2="Demander un coursier moto à Bodrum", cta_p="24/7 sur toute la péninsule de Bodrum",
        footer_p="Service de coursier moto rapide sur toute la péninsule de Bodrum.", footer_priv="Politique de confidentialité",
        breadcrumb_home="Accueil", breadcrumb_name="Coursier moto Bodrum",
        page_name_jsonld="Service de coursier moto Bodrum",
        service_desc_jsonld="Service de coursier moto pour documents, colis, fleurs et médicaments sur toute la péninsule de Bodrum, incluant Merkez, Gümbet, Bitez, Ortakent, Turgutreis, Yalıkavak et Türkbükü.",
        regions_label="Pages de coursier par zone de Bodrum",
    ),
}

MK_REGIONS = [
    ("Bodrum Merkez", "bodrum-merkez-moto-kurye.html"),
    ("Gümbet", "bodrum-gumbet-moto-kurye.html"),
    ("Bitez", "bodrum-bitez-moto-kurye.html"),
    ("Akyarlar", "bodrum-akyarlar-moto-kurye.html"),
    ("Ortakent", "bodrum-ortakent-moto-kurye.html"),
    ("Yahşi", "bodrum-yahsi-moto-kurye.html"),
    ("Turgutreis", "bodrum-turgutreis-moto-kurye.html"),
    ("Gümüşlük", "bodrum-gumusluk-moto-kurye.html"),
    ("Yalıkavak", "bodrum-yalikavak-moto-kurye.html"),
    ("Gündoğan", "bodrum-gundogan-moto-kurye.html"),
    ("Gölköy", "bodrum-golkoy-moto-kurye.html"),
    ("Türkbükü", "bodrum-turkbuku-moto-kurye.html"),
    ("Torba", "bodrum-torba-moto-kurye.html"),
    ("Güvercinlik", "bodrum-guvercinlik-moto-kurye.html"),
    ("Konacık", "bodrum-konacik-moto-kurye.html"),
    ("Çiftlik", "bodrum-ciftlik-moto-kurye.html"),
]

for lang in LANGS:
    t = MK_TXT[lang]
    html = build_page(
        lang=lang, slug=f"bodrum-moto-kurye-{lang}",
        title=t["title"], desc=t["desc"], h1=t["h1"], sub=t["sub"], info=t["info"],
        services=MK_SERVICES[lang], services_h2=t["services_h2"],
        steps=MK_STEPS[lang], steps_h2=t["steps_h2"],
        faq=MK_FAQ[lang], faq_h2=t["faq_h2"],
        cta_h2=t["cta_h2"], cta_p=t["cta_p"],
        footer_p=t["footer_p"], footer_priv=t["footer_priv"],
        breadcrumb_home=t["breadcrumb_home"], breadcrumb_name=t["breadcrumb_name"],
        page_name_jsonld=t["page_name_jsonld"], service_desc_jsonld=t["service_desc_jsonld"],
        slug_base="bodrum-moto-kurye", turkish_url="bodrum-moto-kurye.html",
        regions=MK_REGIONS, regions_label=t["regions_label"],
    )
    (ROOT / f"bodrum-moto-kurye-{lang}.html").write_text(html, encoding="utf-8")
    print(f"wrote bodrum-moto-kurye-{lang}.html")
