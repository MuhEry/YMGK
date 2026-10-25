# KR KZM 3 Speedy - Endüstriyel Siber Güvenlik Projesi

Karabudak Makine **KR KZM 3 Speedy Kenar Zımparalama Makinesi** için ilk dört laboratuvarın makineye uyarlanmış eğitim çalışmasıdır. Kamuya açık üretici bilgileriyle hazırlanmıştır; gerçek makineye bağlantı veya saha testi yapılmamıştır.

| Laboratuvar | Teslim | Evidence Pack |
|---|---|---|
| 1 | [Safety Architecture](output/pdf/Lab1_Safety_Architecture.pdf) | EP 03 |
| 2 | [IEC 62443 Mini Workshop](output/pdf/Lab2_IEC62443_Zone_Conduit.pdf) | EP 05 |
| 3 | [Threat & Risk + Risk Matrix](output/pdf/Lab3_Threat_Risk_Matrix.pdf) | EP 04 |
| 4 | [Secure Remote Access](output/pdf/Lab4_Secure_Remote_Access.pdf) | EP 02 + EP 06 |

[Birleşik dört sayfalık PDF](output/pdf/KR_KZM_3_Speedy_LAB_1-4_Doldurulmus.pdf) de eklenmiştir. Ad Soyad ve Grup alanları doldurulabilirdir; kişisel bilgi tahmin edilmemiştir. Tarih hazırlama tarihidir: 25.10.2026.

## Kanıt ve varsayım ayrımı

- **Doğrulanan:** Üreticinin kamuya açık sayfasında belirtilen özellik; saha doğrulaması değildir.
- **Bilinmiyor:** Kamuya açık kaynakta açıklanmayan ayrıntı; özelliğin bulunmadığını göstermez.
- **Varsayım:** Koşullu eğitim senaryosu; tespit edilmiş güvenlik açığı değildir.
- **Öneri:** Hedef emniyet/siber güvenlik gereksinimi; uygulanmış kontrol değildir.
- **Çıkarım:** Makinenin hareket ve işlevlerinden yapılan tehlike yorumu.

PLC modeli, firmware, emniyet rölesi/PLC, STO, ışık perdesi, ağ portları, Wi-Fi, USB, bulut ve uzak erişim bilinmiyor. PaketPro föyündeki açık modem veya admin/admin örnekleri bu makineye ait bulgu sayılmamıştır. PLr/SIL veya CVE atanmamıştır.

## Depo düzeni

- `data/labs.json`: Dört föyün düzenlenebilir içerikleri ve tabloları.
- `tools/build_labs.py`: Bu veriden dört ayrı ve bir birleşik PDF üretir; taşmayı denetler.
- `output/pdf/`: Teslim dosyaları.
- [Kaynaklar ve bilgi eksikleri](docs/KAYNAKLAR.md)
- [Mevzuat ve uygunluk bilgi eksikleri](docs/MEVZUAT_BOSLUK_ANALIZI.md)
- [SWOT, SMART ve görev takibi](docs/PROJE_YONETIMI.md)
- [Kör masa başı test planı](docs/KOR_TEST_PLANI.md)
- [Kalite kontrol kaydı](docs/KALITE_KONTROL.md)

## Yeniden üretme

Python 3.10+ ve Windows Arial yazı tipleri gerekir. Depo kökünde:

```powershell
python -m pip install -r requirements.txt
python tools/build_labs.py
```

Metin değişiklikleri `data/labs.json` üzerinde yapılır. Üretim aracı ağ veya makine bağlantısı kurmaz. Çıktı değişikliklerinden sonra sayfa yerleşimi tekrar kontrol edilmelidir.

## Kapsam ve durum

LAB 1-4 hazırdır. LAB 5-7, gerçek bileşen envanteri, sınıf içi makine çakışma kontrolü ve kör test oturumu tamamlanmış değildir. Canlı Trello panosu açılmamıştır. Bu çalışma uygunluk belgesi veya üreticinin onayladığı tasarım değildir.

Depo düzeni, kullanıcının gösterdiği [Karmetal örnek reposu](https://github.com/huseyineneserturk/karmetal-OSA-350x450-PLC) incelenerek oluşturulmuştur (incelenen commit: `1607fdc987ab83320e0ffd9e89640a0a7ce7b0be`). Örnek kod/metin kopyalanmamış; içerikler KR KZM 3 Speedy için hazırlanmıştır. Kullanıcının kaynak PDF'si yeniden dağıtılmamıştır.
