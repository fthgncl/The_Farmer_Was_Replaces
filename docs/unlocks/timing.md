# Zamanlama (Timing)
Yöntemlerinizi (metotlarınızı) gerçekten optimize etmek istiyorsanız, bu oyunda zamanın nasıl ölçüldüğünü anlamanız gerekir. Bu kilit tamamen bununla ilgilidir.

## Yeni Fonksiyonlar
Bir şeylerin ne kadar sürdüğünü ölçmek için yararlı iki fonksiyon vardır:

`get_time()`, oyunun başlangıcından bu yana geçen süreyi saniye cinsinden döndürür.

`get_tick_count()`, yürütmenin başlangıcından bu yana gerçekleştirilen tik (tick) sayısını döndürür.

Bu iki fonksiyon ve `quick_print()` tamamen ücretsizdir (maliyetsizdir). Çağrı (call) işlemi bile onlar için ücretsizdir.

## Çalışma Zamanı Ayrıntıları

### Uyarı
Gerçek dünyada performans böyle çalışmaz. Bunlar sadece bu oyunun tutarlı ve anlaşılır bir zamanlama modeline sahip olması için uydurulmuş kurallardır.
Muhtemelen sadece kodunuzu aşırı optimize etmek (hyper-optimize) istiyorsanız bunu önemseyeceksiniz.

Kod yürütme için temel zaman birimine "tik" denir. Hız yükseltmeleri ve güç olmadan, yürütme saniyede `400` tik hızında ilerler.

Genel olarak, `+, -, *, /, //, %, and, or, ...` gibi iki değeri birleştiren işlemlerin çalışması bir tik sürer.
Tek değer alan `-` ve `not` ücretsizdir.
Bir `if` dalının çalışması da bir tik sürer (koşul ifadesini değerlendirmek için gereken süreye ek olarak).
Fonksiyon çağrıları ve değişken okuma/yazma işlemleri ücretsizdir ancak fonksiyon tanımları 1 tik sürer.
`import` ifadeleri ücretsizdir.
İçe aktarılan bir modüle `.` operatörü ile erişmek ücretsizdir.
Bir fonksiyon veya modül argümanlar veya değişken atamaları yoluyla geçirilmişse, onu kullanmak 0 yerine 1 tik maliyetli olacaktır.
`for` ve `while` döngülerinin başlaması bir tik sürer, ancak yinelemeler ücretsizdir (koşul/dizi ifadelerini değerlendirmek için gereken süre sayılmaz).
`return`, `break` ve `continue` ifadelerinin hepsi ücretsizdir.
`pass` bir tik sürer, bu nedenle hassas gecikmeler oluşturmak için kullanılabilir.
Bir veri yapısını indekslemek, indeks operatörü için bir tik ve sözlük veya küme durumunda anahtarın boyutuna bağlı olarak ek tikler sürer.

Yerleşik (builtin) fonksiyonların çalışması için gereken tik sayısı, her fonksiyonun kendi belgelerinde ayrı ayrı belgelenmiştir.