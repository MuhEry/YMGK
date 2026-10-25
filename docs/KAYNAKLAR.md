# Kaynak ve kanıt kaydı

Erişim/inceleme: 25.10.2026. Kamuya açık belge incelemesi; gerçek makinede kontrol yapılmadı.

| Kod | Kaynak | Kullanım |
|---|---|---|
| K1 | [Karabudak ürün sayfası](https://karabudakmakine.com/kr-kzm-3-speedy-kenar-zimparalama-makinesi/) | Makine işlevleri ve kamuya açıklanan özellikler |
| K2 | [Pilz, Functional Safety and Risk Assessment](https://www.pilz.com/download/open/Pos_Functional_safety_1003920-EN-06.pdf) | PLr/SIL risk temelli değerlendirme yaklaşımı |
| K3 | [Rockwell, Safety-AT196A-EN-P](https://literature.rockwellautomation.com/idc/groups/literature/documents/at/safety-at196_-en-p.pdf), s. 5 | STO, serbest duruş ve ayrı başlatma ilkesi; bu marka makinede var demek değildir |
| K4 | [ISA/IEC 62443 genel çerçeve](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards) | OT güvenlik ve risk yaklaşımı |
| K5 | [ISASecure/ISAGCA IIoT rehberi](https://isagca.org/hubfs/2022%20ISA%20Website%20Redesigns/ISASecure/PDFs/IIoT%20System%20Certification%2062443%20Paper_ISASecure_ISAGCA.pdf?hsLang=en), Ek A.2 | Zone/conduit ve risk süreci |
| K6 | [NIST SP 800-82 Rev.3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) | OT güvenlik rehberi; yayın sayfasında Rev.4 taslağı ayrıca duyurulmuş, bu çalışma Rev.3'ü esas alır |
| F1 | Kullanıcının sağladığı laboratuvar PDF'si, s. 2-5 | LAB 1-4 görevleri; kapak laboratuvar sayılmaz |

PDF içindeki [1], [2], [3], [4] sırasıyla K1, K2, K3, K4/K5'e karşılık gelir.

## Makineye ilişkin kanıtlar

K1: Ahşap kenarlarında ham/astar zımparası; bir disk fırça, iki orbital motor; dokunmatik ekrandan hız ayarı; manuel ünite/üst baskı konumları. İlerleme 1-10 m/dk; emiş ihtiyacı 1000 m³/sa. Bu bilgilerden kapılma, sıkışma ve toz tehlikesi analitik olarak çıkarılmıştır; ölçülmüş saha riski değildir.

## Bilgi eksikleri

| ID | Bilinmeyen | Gerekli kanıt |
|---|---|---|
| B01 | Kontrolör/sürücü modeli, firmware | Üretici bileşen listesi ve sürüm envanteri |
| B02 | Emniyet devresi ve koruyucu tipi | Elektrik şeması, koruyucu listesi, işlev testi |
| B03 | Durma süresi, erişim ve yeniden başlatma | Ölçüm ve validasyon kaydı |
| B04 | Ağ, port, uzak bakım, Wi-Fi/USB/bulut | Gerçek varlık/bağlantı envanteri ve erişim politikası |
| B05 | PLr/SIL, CE dosyası ve mevzuat kapsamı | Risk değerlendirmesi, teknik dosya ve yetkili inceleme |
| B06 | Toz emiş izleme ve arıza davranışı | Emiş sistemi ve kontrol senaryosu |

Kanıt gelene kadar bu alanlara model, sürüm, açık veya uygunluk sonucu yazılmaz.
