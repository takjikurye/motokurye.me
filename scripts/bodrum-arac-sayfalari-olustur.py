#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bodrum arac parkuru hizmet sayfalarini (hafif nakliye, parsiyel yuk, moloz
dokumu, insaat malzemesi, ev esyasi, forklift, manitou, cekici) mevcut
bodrum-doblo-nakliye.html sayfasindan STATIC header/footer/script bloklarini
aynen alarak uretir. Sadece head meta/json-ld ve body icerigi (hero+content)
sayfaya ozgudur.
"""
import json
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_PATH = ROOT / "bodrum-doblo-nakliye.html"

text = TEMPLATE_PATH.read_text(encoding="utf-8")

body_idx = text.index("<body>")
main_idx = text.index("<main><article>") + len("<main><article>")
STATIC_HEADER = text[body_idx:main_idx]

tail_start = text.index("</article></main>")
STATIC_TAIL = text[tail_start:]
# WhatsApp mesaj metnini placeholder yap
old_wa = "text=Merhaba%2C%20Bodrum%20Doblo%20ile%20Nakliye%20i%C3%A7in%20bilgi%20almak%20istiyorum"
assert old_wa in STATIC_TAIL, "wa.me metni bulunamadi, sablon degismis olabilir"
STATIC_TAIL = STATIC_TAIL.replace(old_wa, "text=__WA_TEXT_PLACEHOLDER__")

def build_head(title, desc, slug, css_block, jsonld):
    return (
        '<!DOCTYPE html>\n<html lang="tr">\n<head>\n'
        f'<title>{title}</title>\n'
        f'<meta name="description" content="{desc}">\n'
        f'<link rel="canonical" href="https://motokurye.me/{slug}.html">\n'
        f'<meta property="og:title" content="{title}">\n'
        f'<meta property="og:description" content="{desc}">\n'
        f'<meta property="og:url" content="https://motokurye.me/{slug}.html">\n'
        '<meta property="og:type" content="website">\n'
        '<meta property="og:site_name" content="MotoKurye.me">\n'
        '<meta name="robots" content="index,follow">\n'
        '<link rel="sitemap" href="/sitemap-index.xml">\n'
        '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        '<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Outfit:wght@700;800&family=DM+Sans:wght@400;500&display=swap" onload="this.onload=null;this.rel=\'stylesheet\'">\n'
        '<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Outfit:wght@700;800&family=DM+Sans:wght@400;500&display=swap"></noscript>\n'
        '<style>\n/* Sistem font fallback — font yüklenene kadar görünür metin */\n:root{\n'
        "  --fh: 'Outfit', -apple-system, 'Segoe UI', Arial, sans-serif;\n"
        "  --fb: 'DM Sans', -apple-system, 'Segoe UI', Arial, sans-serif;\n"
        '}\n</style>\n'
        "<!-- Google Tag Manager -->\n"
        "<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':\n"
        "new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],\n"
        "j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=\n"
        "'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);\n"
        "})(window,document,'script','dataLayer','GTM-KM26MWSV');</script>\n"
        "<!-- End Google Tag Manager -->\n"
        + css_block + "\n"
        '<script type="application/ld+json">\n' + jsonld + '\n</script>\n'
        '<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n'
        '<link rel="icon" href="/favicon.ico" sizes="any">\n'
        '<link rel="apple-touch-icon" href="/favicon.svg">\n'
        '<link rel="manifest" href="/manifest.json">\n'
        '<meta name="theme-color" content="#16A34A">\n'
        '<meta name="twitter:card" content="summary_large_image">\n'
        '<meta name="twitter:site" content="@motokurye">\n'
        f'<meta name="twitter:title" content="{title}">\n'
        f'<meta name="twitter:description" content="{desc}">\n'
        f'<link rel="alternate" hreflang="tr" href="https://motokurye.me/{slug}.html">\n'
        f'<link rel="alternate" hreflang="x-default" href="https://motokurye.me/{slug}.html">\n'
        '<meta property="og:image" content="https://motokurye.me/og-image.jpg">\n'
        '<meta property="og:image:width" content="1200">\n'
        '<meta property="og:image:height" content="630">\n'
        '<meta name="twitter:image" content="https://motokurye.me/og-image.jpg">\n'
        '</head>\n'
    )

# CSS blogu doblo sayfasindan aynen al (ikinci <style> bloku, iki script arasinda)
css_start = text.index("<style>\n:root{\n  --gr:")
css_end = text.index("</style>\n<script type=\"application/ld+json\">") + len("</style>")
CSS_BLOCK = text[css_start:css_end]

PAGES = [
    dict(
        slug="bodrum-hafif-nakliye",
        title="Bodrum Hafif Nakliye | MotoKurye.me",
        desc="Bodrum'da Doblo ile hafif nakliye hizmeti. Az sayıda parça eşya ve küçük hacimli yükler için hızlı, sigortalı taşıma — MotoKurye.me.",
        h1="Bodrum Hafif Nakliye",
        sub="Doblo ile az sayıda parça eşya ve küçük hacimli yüklerin hızlı, pratik taşınması.",
        vehicle="Doblo",
        vehicle_desc="Doblo, hafif nakliye için ideal bir araçtır: dar sokaklara ve site girişlerine kolay erişir, az sayıda parça eşya veya küçük hacimli yükleri hızlı şekilde taşır.",
        capacity_v="~4 m³", capacity_w="~750 kg",
        service_desc="Az sayıda parça eşya ve küçük hacimli yükler için Doblo ile hafif nakliye hizmeti.",
        ne_tasiyoruz=["Az sayıda parça eşya", "Küçük ofis/ev eşyası", "Esnaf/e-ticaret malı (küçük-orta hacim)"],
        fiyat_not="Hafif nakliyede fiyat; mesafe, eşya sayısı/hacmi ve kat/asansör durumuna göre belirlenir. Doblo'nun düşük işletme maliyeti, küçük hacimli işlerde fiyatı olumlu etkileyebilir.",
        faq=[
            ("Hafif nakliye ile hangi büyüklükte eşya taşınır?", "Az sayıda parça eşya ve küçük hacimli yükler Doblo ile taşınır; daha büyük hacimler için kamyonet veya diğer araç seçeneklerimizi öneririz."),
            ("Doblo dar sokaklara girebiliyor mu?", "Evet, Doblo diğer araçlara göre dar sokaklara ve site girişlerine daha kolay erişebilir."),
            ("Hafif nakliye sigortalı mı?", "Evet, sigortalı taşıma yapıyoruz."),
            ("Eşyam Doblo'ya sığmazsa ne olur?", "Değerlendirme aşamasında eşya hacmi uygun değilse kamyonet veya transit seçeneğimizi öneririz."),
        ],
        related=["bodrum-doblo-nakliye", "bodrum-parsiyel-yuk", "bodrum-ev-esyasi-tasima"],
    ),
    dict(
        slug="bodrum-parsiyel-yuk",
        title="Bodrum Parsiyel Yük Taşıma | MotoKurye.me",
        desc="Bodrum'da Transit minibüs ile parsiyel (kısmi) yük taşıma. Orta hacimli yükler için hızlı, sigortalı nakliye — MotoKurye.me.",
        h1="Bodrum Parsiyel Yük Taşıma",
        sub="Transit minibüs ile orta hacimli parsiyel yüklerin güvenli ve hızlı taşınması.",
        vehicle="Transit Minibüs",
        vehicle_desc="Transit minibüs, Doblo'dan daha fazla hacim ve ağırlık taşıyabilen, ancak büyük kamyondan daha esnek manevra kabiliyetine sahip bir araçtır; parsiyel (kısmi/parçalı) yük taşımalarında tercih edilir.",
        capacity_v="~10 m³", capacity_w="~1.200 kg",
        service_desc="Transit minibüs ile orta hacimli parsiyel yük taşıma hizmeti.",
        ne_tasiyoruz=["Parsiyel (kısmi) ticari yük", "Birden fazla adrese dağıtılacak orta hacimli koliler", "Esnaf/e-ticaret toplu sevkiyatları"],
        fiyat_not="Parsiyel yük taşımada fiyat; mesafe, yük hacmi/ağırlığı ve durak sayısına göre belirlenir. Net fiyat için WhatsApp'tan iletişime geçebilirsiniz.",
        faq=[
            ("Parsiyel yük nedir?", "Parsiyel yük, tek bir aracı tam doldurmayan, kısmi/parçalı ticari yüklerin taşınmasıdır."),
            ("Transit minibüs ile kaç duraklı dağıtım yapılıyor?", "Yükün hacmine ve adrese göre değişir; talebinizi ilettiğinizde size uygun planlama yapılır."),
            ("Parsiyel yük taşıma sigortalı mı?", "Evet, sigortalı taşıma yapıyoruz."),
            ("Parsiyel yük ile aynı gün teslimat mümkün mü?", "Uygunluğa göre mümkündür; aciliyet durumunda acil nakliye hizmetimizi de değerlendirebiliriz."),
        ],
        related=["bodrum-hafif-nakliye", "bodrum-kamyonet-nakliye", "bodrum-sehirlerarasi-nakliye"],
    ),
    dict(
        slug="bodrum-moloz-dokum",
        title="Bodrum Moloz Dökümü | MotoKurye.me",
        desc="Bodrum'da açık kasa kamyonet ile moloz dökümü ve inşaat atığı taşıma hizmeti. Hızlı, güvenli nakliye — MotoKurye.me.",
        h1="Bodrum Moloz Dökümü",
        sub="Açık kasa kamyonet ile inşaat/tadilat molozunun toplanıp taşınması.",
        vehicle="Açık Kasa Kamyonet",
        vehicle_desc="Açık kasa kamyonet, moloz ve inşaat atığı gibi yoğunluğu yüksek yüklerin taşınması için uygundur; tadilat ve yıkım sonrası atıkların hızlı tahliyesinde kullanılır.",
        capacity_v="~7 m³", capacity_w="~3.000 kg",
        service_desc="Açık kasa kamyonet ile moloz ve inşaat atığı taşıma/döküm hizmeti.",
        ne_tasiyoruz=["İnşaat/tadilat molozu", "Yıkım atığı", "Hafriyat artığı (küçük-orta hacim)"],
        ne_tasimiyoruz_ek="Tehlikeli/zararlı atık (asbest, kimyasal madde vb.) taşımıyoruz.",
        fiyat_not="Moloz dökümünde fiyat; moloz hacmi/ağırlığı, mesafe ve döküm sahasına erişime göre belirlenir. Net fiyat için WhatsApp'tan iletişime geçebilirsiniz.",
        faq=[
            ("Moloz dökümü için izin gerekiyor mu?", "Döküm sahasıyla ilgili yasal izin ve yönlendirmeler müşteriye aittir; biz taşıma hizmetini sağlarız."),
            ("Ne kadar moloz taşıyabiliyorsunuz?", "Açık kasa kamyonetimiz ortalama 7 m³ / 3.000 kg kapasitelidir; daha fazla hacim için birden fazla sefer planlanabilir."),
            ("Moloz dökümü sigortalı mı?", "Evet, sigortalı taşıma yapıyoruz."),
            ("Aynı gün moloz alımı yapılıyor mu?", "Uygunluğa göre mümkündür; talebinizi ilettiğinizde en yakın uygun zamanı paylaşırız."),
        ],
        related=["bodrum-insaat-malzeme-tasima", "bodrum-kamyonet-nakliye", "bodrum-acil-nakliye"],
    ),
    dict(
        slug="bodrum-insaat-malzeme-tasima",
        title="Bodrum İnşaat Malzemesi Taşıma | MotoKurye.me",
        desc="Bodrum'da kamyonet ile inşaat malzemesi taşıma hizmeti. Tuğla, çimento, demir ve diğer yapı malzemeleri için güvenli nakliye — MotoKurye.me.",
        h1="Bodrum İnşaat Malzemesi Taşıma",
        sub="Kamyonet ile tuğla, çimento, demir ve diğer yapı malzemelerinin şantiyeye/adrese taşınması.",
        vehicle="Açık/Kapalı Kasa Kamyonet",
        vehicle_desc="Açık veya kapalı kasa kamyonet, inşaat malzemelerinin ağırlığına ve hava koşullarına göre (çimento, alçı gibi nem hassasiyeti olan malzemeler kapalı kasada) taşınmasına uygundur.",
        capacity_v="~15 m³", capacity_w="~2.500 kg",
        service_desc="Kamyonet ile inşaat malzemesi (tuğla, çimento, demir vb.) taşıma hizmeti.",
        ne_tasiyoruz=["Tuğla, kiremit, blok", "Çimento, alçı, harç torbaları", "Demir, profil, yapı iskeleti parçaları"],
        fiyat_not="İnşaat malzemesi taşımada fiyat; malzeme ağırlığı/hacmi, mesafe ve şantiye erişim koşullarına göre belirlenir. Net fiyat için WhatsApp'tan iletişime geçebilirsiniz.",
        faq=[
            ("Hangi inşaat malzemelerini taşıyorsunuz?", "Tuğla, çimento, demir, alçı ve benzeri genel yapı malzemelerini taşıyoruz."),
            ("Şantiyeye kadar teslimat yapılıyor mu?", "Araç trafiğine açık olan şantiye sahalarına kadar teslimat yapılır."),
            ("İnşaat malzemesi taşıma sigortalı mı?", "Evet, sigortalı taşıma yapıyoruz."),
            ("Büyük hacimli malzeme siparişlerinde ne yapmalıyım?", "Malzeme miktarını ilettiğinizde kamyonet yeterli olup olmadığını, gerekirse büyük kamyon seçeneğini değerlendiririz."),
        ],
        related=["bodrum-moloz-dokum", "bodrum-ev-esyasi-tasima", "bodrum-kamyonet-nakliye"],
    ),
    dict(
        slug="bodrum-ev-esyasi-tasima",
        title="Bodrum Ev Eşyası Taşıma | MotoKurye.me",
        desc="Bodrum'da kapalı kasa kamyonet ile ev eşyası taşıma (evden eve nakliyat) hizmeti. Güvenli, sigortalı taşıma — MotoKurye.me.",
        h1="Bodrum Ev Eşyası Taşıma",
        sub="Kapalı kasa kamyonet ile evden eve nakliyat; mobilya ve ev eşyalarının güvenli taşınması.",
        vehicle="Kapalı Kasa Kamyonet",
        vehicle_desc="Kapalı kasa kamyonet, ev eşyalarını hava koşullarından ve taşıma sırasında oluşabilecek hasarlardan koruyarak taşımaya uygundur.",
        capacity_v="~20 m³", capacity_w="~2.500 kg",
        service_desc="Kapalı kasa kamyonet ile ev eşyası taşıma (evden eve nakliyat) hizmeti.",
        ne_tasiyoruz=["Mobilya (koltuk, yatak, dolap vb.)", "Beyaz eşya", "Kutulanmış ev eşyaları"],
        fiyat_not="Ev eşyası taşımada fiyat; eşya miktarı/hacmi, kat/asansör durumu ve mesafeye göre belirlenir. Sabit bir rakam paylaşmıyoruz; net fiyat için WhatsApp'tan iletişime geçebilirsiniz.",
        ek_hizmetler=["<strong>Paketleme:</strong> Eşyaların taşıma öncesi güvenli şekilde paketlenmesi.",
                      "<strong>Montaj/Demontaj:</strong> Mobilya ve büyük eşyaların sökülüp yeniden kurulması.",
                      "<strong>Hamal (Yükleme-Boşaltma):</strong> Eşyaların araca yüklenmesi ve indirilmesi için hamal desteği."],
        faq=[
            ("Ev eşyası taşımada montaj/demontaj dahil mi?", "Talep edilmesi halinde montaj/demontaj ve paketleme ek hizmet olarak sağlanır."),
            ("Kat/asansör durumu fiyatı etkiler mi?", "Evet, kat sayısı ve asansör durumu fiyatlandırmada dikkate alınır."),
            ("Ev eşyası taşıma sigortalı mı?", "Evet, sigortalı taşıma yapıyoruz."),
            ("Aynı gün ev taşıma mümkün mü?", "Uygunluğa göre mümkündür; aciliyet durumunda acil nakliye hizmetimizi de değerlendirebiliriz."),
        ],
        related=["bodrum-ofis-isyeri-tasima", "bodrum-yazlik-esya-tasima", "bodrum-insaat-malzeme-tasima"],
    ),
    dict(
        slug="bodrum-forklift-kiralama",
        title="Bodrum Forklift ile Yük Taşıma | MotoKurye.me",
        desc="Bodrum'da forklift ile yük taşıma ve elleçleme hizmeti. Palet, ağır malzeme ve ticari yüklerin güvenli taşınması — MotoKurye.me.",
        h1="Bodrum Forklift ile Yük Taşıma",
        sub="Forklift ile palet, ağır malzeme ve ticari yüklerin yükleme-boşaltma ve kısa mesafe taşıması.",
        vehicle="Forklift",
        vehicle_desc="Forklift, palet üzerindeki yüklerin ve ağır/hacimli malzemelerin depo, şantiye veya marina sahalarında kısa mesafeli taşınması ile yükleme-boşaltma işlemlerinde kullanılır.",
        capacity_v="~3-4,5 m yük. yüksekliği", capacity_w="~2.500-3.000 kg kaldırma kapasitesi",
        service_desc="Forklift ile palet ve ağır yüklerin taşınması, yükleme-boşaltma hizmeti.",
        ne_tasiyoruz=["Palet üzerindeki ticari yükler", "Ağır/hacimli malzemeler", "İnşaat malzemesi yükleme-boşaltma"],
        fiyat_not="Forklift hizmetinde fiyat; çalışma süresi, yük ağırlığı ve lokasyona göre belirlenir. Net fiyat için WhatsApp'tan iletişime geçebilirsiniz.",
        faq=[
            ("Forklift hangi işler için kullanılır?", "Palet üzerindeki yüklerin yükleme-boşaltılması ve kısa mesafeli taşınması için kullanılır."),
            ("Forklift kaç kg kaldırabiliyor?", "Ortalama kaldırma kapasitemiz 2.500-3.000 kg aralığındadır; talebinize göre uygunluk teyit edilir."),
            ("Forklift hizmeti operatörlü mü?", "Evet, forklift operatörümüzle birlikte hizmet verilir."),
            ("Forklift hizmeti sigortalı mı?", "Evet, sigortalı hizmet veriyoruz."),
        ],
        related=["bodrum-manitou-kiralama", "bodrum-insaat-malzeme-tasima", "bodrum-tekne-yat-malzeme-tasima"],
    ),
    dict(
        slug="bodrum-manitou-kiralama",
        title="Bodrum Manitou ile Yük Taşıma | MotoKurye.me",
        desc="Bodrum'da Manitou (teleskopik yükleyici) ile yük taşıma ve yükseğe kaldırma hizmeti. Şantiye ve inşaat sahaları için — MotoKurye.me.",
        h1="Bodrum Manitou ile Yük Taşıma",
        sub="Manitou (teleskopik yükleyici) ile yüksek erişimli yük taşıma ve kaldırma hizmeti.",
        vehicle="Manitou",
        vehicle_desc="Manitou (teleskopik yükleyici), forklifte göre daha yüksek ve uzak noktalara erişebilen, şantiye ve inşaat sahalarında ağır yüklerin kaldırılıp taşınmasında kullanılan bir araçtır.",
        capacity_v="~9 m erişim yüksekliği", capacity_w="~3.000-4.000 kg kaldırma kapasitesi",
        service_desc="Manitou (teleskopik yükleyici) ile yüksek erişimli yük taşıma ve kaldırma hizmeti.",
        ne_tasiyoruz=["İnşaat malzemesi (yükseğe kaldırma)", "Ağır paletli yükler", "Şantiye ekipmanı"],
        fiyat_not="Manitou hizmetinde fiyat; çalışma süresi, yük ağırlığı/yüksekliği ve lokasyona göre belirlenir. Net fiyat için WhatsApp'tan iletişime geçebilirsiniz.",
        faq=[
            ("Manitou ile forklift arasındaki fark nedir?", "Manitou, teleskopik kolu sayesinde forklifte göre daha yüksek ve uzak noktalara erişebilir."),
            ("Manitou hangi sahalarda kullanılıyor?", "Şantiye, inşaat ve geniş depo sahalarında ağır yüklerin kaldırılıp taşınmasında kullanılır."),
            ("Manitou hizmeti operatörlü mü?", "Evet, Manitou operatörümüzle birlikte hizmet verilir."),
            ("Manitou hizmeti sigortalı mı?", "Evet, sigortalı hizmet veriyoruz."),
        ],
        related=["bodrum-forklift-kiralama", "bodrum-insaat-malzeme-tasima", "bodrum-moloz-dokum"],
    ),
    dict(
        slug="bodrum-cekici-hizmeti",
        title="Bodrum Çekici Hizmeti | MotoKurye.me",
        desc="Bodrum'da platformlu çekici ile araç ve ağır ekipman taşıma hizmeti. Hızlı, güvenli çekici desteği — MotoKurye.me.",
        h1="Bodrum Çekici Hizmeti",
        sub="Platformlu çekici ile araç ve ağır ekipmanın güvenli şekilde taşınması.",
        vehicle="Çekici (Platformlu)",
        vehicle_desc="Platformlu çekici, arızalı/kazalı araçların veya tekerlekli ağır ekipmanın bir noktadan diğerine güvenli şekilde taşınmasında kullanılır.",
        capacity_v="1 araç/ekipman", capacity_w="~3.000-3.500 kg taşıma kapasitesi",
        service_desc="Platformlu çekici ile araç ve ağır ekipman taşıma hizmeti.",
        ne_tasiyoruz=["Arızalı/kazalı araçlar", "Tekerlekli ağır ekipman", "Küçük iş makineleri"],
        fiyat_not="Çekici hizmetinde fiyat; mesafe, araç/ekipman ağırlığı ve erişim koşullarına göre belirlenir. Net fiyat için WhatsApp'tan iletişime geçebilirsiniz.",
        faq=[
            ("Çekici hangi tür araçları taşıyabilir?", "Otomobil, hafif ticari araç ve tekerlekli küçük iş makinelerini taşıyabiliriz; ağırlık sınırını talep anında teyit ederiz."),
            ("Çekici hizmeti 7/24 mü?", "Evet, çekici hizmetimiz de 7/24 aktiftir."),
            ("Çekici hizmeti sigortalı mı?", "Evet, sigortalı taşıma yapıyoruz."),
            ("Acil çekici talebi yapabilir miyim?", "Evet, acil durumlarda da çekici talebinizi telefon veya WhatsApp üzerinden iletebilirsiniz."),
        ],
        related=["bodrum-acil-nakliye", "bodrum-sehirlerarasi-nakliye", "bodrum-forklift-kiralama"],
    ),
]

SLUG_TITLE = {
    "bodrum-doblo-nakliye": "Bodrum Doblo ile Nakliye",
    "bodrum-kamyonet-nakliye": "Bodrum Kamyonet ile Nakliye",
    "bodrum-parca-esya-tasima": "Bodrum Parça Eşya Taşıma",
    "bodrum-tekne-yat-malzeme-tasima": "Bodrum Tekne ve Yat Malzemesi Taşıma",
    "bodrum-ofis-isyeri-tasima": "Bodrum Ofis ve İşyeri Taşıma",
    "bodrum-yazlik-esya-tasima": "Bodrum Yazlık Eşya Taşıma",
    "bodrum-esnaf-eticaret-mal-tasima": "Bodrum Esnaf ve E-Ticaret Mal Taşıma",
    "bodrum-acil-nakliye": "Bodrum Acil Nakliye",
    "bodrum-sehirlerarasi-nakliye": "Bodrum Şehirlerarası Nakliye",
    "bodrum-hafif-nakliye": "Bodrum Hafif Nakliye",
    "bodrum-parsiyel-yuk": "Bodrum Parsiyel Yük Taşıma",
    "bodrum-moloz-dokum": "Bodrum Moloz Dökümü",
    "bodrum-insaat-malzeme-tasima": "Bodrum İnşaat Malzemesi Taşıma",
    "bodrum-ev-esyasi-tasima": "Bodrum Ev Eşyası Taşıma",
    "bodrum-forklift-kiralama": "Bodrum Forklift ile Yük Taşıma",
    "bodrum-manitou-kiralama": "Bodrum Manitou ile Yük Taşıma",
    "bodrum-cekici-hizmeti": "Bodrum Çekici Hizmeti",
}


def jsonld_for(p):
    faq_items = [
        {
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a},
        }
        for q, a in p["faq"]
    ]
    graph = [
        {
            "@type": "LocalBusiness",
            "@id": "https://motokurye.me/#business",
            "name": "MotoKurye.me",
            "url": "https://motokurye.me/",
            "telephone": "+905446018815",
            "image": "https://motokurye.me/logo.png",
            "logo": {"@type": "ImageObject", "url": "https://motokurye.me/logo.png", "width": 512, "height": 512},
            "priceRange": "₺₺",
            "address": {"@type": "PostalAddress", "addressLocality": "İstanbul", "addressRegion": "İstanbul", "addressCountry": "TR"},
            "openingHoursSpecification": {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"], "opens": "00:00", "closes": "23:59"},
            "areaServed": {"@type": "City", "name": "İstanbul", "sameAs": "https://www.wikidata.org/wiki/Q406"},
        },
        {
            "@type": "Service",
            "@id": f"https://motokurye.me/{p['slug']}.html#service",
            "name": p["h1"],
            "description": p["service_desc"],
            "provider": {"@id": "https://motokurye.me/#business"},
            "areaServed": {
                "@type": "AdministrativeArea",
                "name": "Bodrum",
                "geo": {"@type": "GeoCoordinates", "latitude": 37.0344, "longitude": 27.4305},
                "containedIn": {"@type": "AdministrativeArea", "name": "Muğla"},
            },
            "serviceType": "Nakliye",
            "vehicleType": p["vehicle"],
            "hoursAvailable": {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"], "opens": "00:00", "closes": "23:59"},
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Ana Sayfa", "item": "https://motokurye.me"},
                {"@type": "ListItem", "position": 2, "name": "Nakliye", "item": "https://motokurye.me/bodrum-nakliye.html"},
                {"@type": "ListItem", "position": 3, "name": p["h1"], "item": f"https://motokurye.me/{p['slug']}.html"},
            ],
        },
        {"@type": "FAQPage", "mainEntity": faq_items},
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)


def content_for(p):
    ne_tasiyoruz_html = "\n".join(f"      <li>{x}</li>" for x in p["ne_tasiyoruz"])
    ne_tasimiyoruz = p.get("ne_tasimiyoruz_ek", "")
    faq_visible = "\n".join(
        f'      <details>\n        <summary>{q}</summary>\n        <p>{a}</p>\n      </details>'
        for q, a in p["faq"]
    )
    ek_hizmetler = p.get("ek_hizmetler")
    ek_hizmetler_block = ""
    if ek_hizmetler:
        items = "\n".join(f"      <li>{x}</li>" for x in ek_hizmetler)
        ek_hizmetler_block = f"""
    <h2>Ek Hizmetler</h2>
    <ul>
{items}
    </ul>
"""
    related_links = " · ".join(
        f'<a href="/{slug}.html" style="color:var(--gr);font-size:.82rem;">{SLUG_TITLE[slug]}</a>'
        for slug in p["related"]
    )

    return f"""  <div class="mah-hero">
    <div class="mah-hero-inner">
      <div>
        <nav class="bc-nav" aria-label="Breadcrumb">
          <a href="/">Ana Sayfa</a><span>›</span>
          <a href="/bodrum-nakliye.html">Nakliye</a><span>›</span>
          <span>{p['h1']}</span>
        </nav>
        <h1>{p['h1']}</h1>
        <p class="hd-sub">{p['sub']}</p>
        <div class="mah-hero-btns">
          <a href="tel:+905446018815" class="bp" style="padding:12px 22px;font-size:.88rem;">📞 Nakliye Talep Et</a>
          <a href="https://wa.me/905446018815" class="bor" style="padding:12px 22px;font-size:.88rem;">💬 WhatsApp</a>
        </div>
      </div>
      <div class="mah-info-card">
        <div class="mic-row">
          <div class="mic-ic">📍</div>
          <div><div class="mic-t">Bölge</div><div class="mic-v">Bodrum</div></div>
        </div>
        <div class="mic-row">
          <div class="mic-ic">🚐</div>
          <div><div class="mic-t">Araç</div><div class="mic-v">{p['vehicle']}</div></div>
        </div>
        <div class="mic-row">
          <div class="mic-ic">📐</div>
          <div><div class="mic-t">Ortalama hacim</div><div class="mic-v">{p['capacity_v']}</div></div>
        </div>
        <div class="mic-row">
          <div class="mic-ic">⚖️</div>
          <div><div class="mic-t">Ortalama kapasite</div><div class="mic-v">{p['capacity_w']}</div></div>
        </div>
        <div class="mic-row">
          <div class="mic-ic">🛡️</div>
          <div><div class="mic-t">Taşıma</div><div class="mic-v">Sigortalı</div></div>
        </div>
      </div>
    </div>
  </div>

  <div class="mah-content">
    <h2>{p['h1']} Hizmetimiz</h2>
    <p>{p['vehicle_desc']}</p>
    <p>MotoKurye.me olarak Bodrum'da {p['h1'].lower()} hizmetini profesyonel şekilde sunuyoruz. Talebinizi ilettiğinizde ihtiyacınıza uygun aracı ve ekibi planlıyoruz.</p>

    <h2>Araç Özellikleri (Ortalama)</h2>
    <p><strong>{p['vehicle']}</strong> — ortalama hacim: <strong>{p['capacity_v']}</strong>, ortalama taşıma kapasitesi: <strong>{p['capacity_w']}</strong>. Bu değerler genel ortalamalardır; kesin kapasite, o anki uygun aracın özelliklerine göre değişebilir.</p>

    <h2>Ne Taşıyoruz</h2>
    <ul>
{ne_tasiyoruz_html}
    </ul>

    <h2>Ne Taşımıyoruz</h2>
    <ul>
      <li>Yasal olmayan veya tehlikeli madde taşımıyoruz.{(' ' + ne_tasimiyoruz) if ne_tasimiyoruz else ''}</li>
    </ul>

    <h2>Nasıl Çalışır</h2>
    <div class="ft" style="margin-bottom:14px;"><div class="fi">1️⃣</div><div><h3>Talep</h3><p>Taşınacak yükün türünü, miktarını ve adresleri paylaşırsınız.</p></div></div>
    <div class="ft" style="margin-bottom:14px;"><div class="fi">2️⃣</div><div><h3>Değerlendirme</h3><p>Yükün {p['vehicle'].lower()} için uygun olup olmadığı değerlendirilir, gerekirse alternatif araç önerilir.</p></div></div>
    <div class="ft" style="margin-bottom:14px;"><div class="fi">3️⃣</div><div><h3>Taşıma</h3><p>Yük güvenli şekilde yüklenir ve belirlenen adrese/sahaya taşınır.</p></div></div>
    <div class="ft" style="margin-bottom:14px;"><div class="fi">4️⃣</div><div><h3>Teslim</h3><p>Yük teslim edilir, talep edilmişse ek destek sağlanır.</p></div></div>

    <h2>Fiyatlandırma</h2>
    <p>{p['fiyat_not']}</p>
{ek_hizmetler_block}
    <h2>Bodrum'a Özgü Notlar</h2>
    <p>Mayıs-Eylül döneminde Bodrum'da nakliye talebi belirgin şekilde artar; bu dönemde erken planlama yapmanızı öneririz.</p>
    <p>Araç trafiğine kapalı alanlarda (yaya bölgeleri vb.) hizmet veremiyoruz; taşıma kapıdan kapıya/sahadan sahaya olmak zorundadır. Sigortalı taşıma yapıyoruz.</p>

    <h2>Sıkça Sorulan Sorular</h2>
{faq_visible}

    <h2>İlgili Hizmetler</h2>
    <div style="line-height:2.4;"><a href="/bodrum-nakliye.html" style="color:var(--gr);font-size:.82rem;font-weight:700;">← Tüm Nakliye Hizmetleri</a> · {related_links}</div>

    <div style="background:var(--g50);border:1px solid var(--g100);border-radius:16px;padding:32px;margin-top:36px;display:flex;align-items:center;justify-content:space-between;gap:20px;flex-wrap:wrap;">
      <div>
        <h2 style="margin-bottom:6px;font-size:1.2rem;">{p['h1']} için Talep Oluşturun</h2>
        <p style="color:var(--g500);font-size:.88rem;">7/24 aktif · Sigortalı taşıma</p>
      </div>
      <div style="display:flex;gap:10px;flex-wrap:wrap;">
        <a href="tel:+905446018815" class="bp" style="font-size:.88rem;padding:12px 22px;">📞 0544 601 88 15</a>
        <a href="https://wa.me/905446018815" class="bor" style="font-size:.88rem;padding:12px 22px;">💬 WhatsApp</a>
      </div>
    </div>
  </div>
"""


count = 0
for p in PAGES:
    head = build_head(
        title=p["title"],
        desc=p["desc"],
        slug=p["slug"],
        css_block=CSS_BLOCK,
        jsonld=jsonld_for(p),
    )
    content = content_for(p)
    wa_text = urllib.parse.quote(f"Merhaba, {p['h1']} için bilgi almak istiyorum", safe="")
    tail = STATIC_TAIL.replace("__WA_TEXT_PLACEHOLDER__", wa_text)
    full = head + STATIC_HEADER + "\n" + content + tail

    out_path = ROOT / f"{p['slug']}.html"
    out_path.write_text(full, encoding="utf-8")
    count += 1
    print("yazildi:", out_path.name)

print(f"\nToplam {count} sayfa olusturuldu.")
