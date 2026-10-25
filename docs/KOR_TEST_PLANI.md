# Kör masa başı test planı

Durum: planlandı, uygulanmadı. Bu, belgeler üzerinden karar verme alıştırmasıdır; makine testi değildir.

1. Uygulayıcı dört yeni kurgusal vaka ve ayrı cevap anahtarı hazırlar. Anahtar cevap öncesinde katılımcıya verilmez ve açık repoya yüklenmez.
2. Makinede doğrulanmayan özellikler her vakada varsayım olarak yazılır. Vaka sırası karıştırılır.
3. Öğrenci ilk karar, fiziksel sonuç, eksik kanıt ve gerekçeyi kaydeder; cevap sonrası anahtar açılır.
4. Önceden anahtarı görülen vaka kör sayılmaz; yeni vaka hazırlanır.

| Vaka kategorisi | Ölçülecek karar |
|---|---|
| KT1 - Duruş | Artık dönüş, erişim ve güvenli durum ayrımı |
| KT2 - Bölgeler | Uzak bakımın kontrol ve emniyet sınırları |
| KT3 - Risk | L×S×E ve düşük skorda S=3 inceleme kuralı |
| KT4 - İhlal | Kontrol ele geçirilse de emniyetin korunması için gereken kanıt |

Her vaka için dört ölçüt 0/1 puandır: karar, fiziksel sonuç, kanıt ayrımı, gerekçe. Toplam 16; önerilen eğitim hedefi 12/16. Bu eşik makine kabul kriteri değildir. Kanıtsız “emniyet etkilenmez” cevabı ayrıca öğrenme hatası olarak kaydedilir.

Kayıt: `Vaka ID | Sürüm | İlk cevap zamanı | Karar | Fiziksel sonuç | Eksik kanıt | Gerekçe | Puan | Anahtar açılma zamanı | Düzeltme`.

Sonuçlar oturum gerçekleşmeden doldurulmaz.
