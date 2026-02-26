# Simülasyon

Simülasyonlar, gerçek çiftliğin durumunu değiştirmeden kodu hızlı bir şekilde test etmenizi sağlar.
Simülasyonun başlangıç durumu serbestçe seçilebilir ve simülasyon sona erdiğinde, gerçek çiftlik simülasyon başlamadan önceki durumun aynısında olacaktır.

`simulate()` fonksiyonu bir simülasyon başlatmak için kullanılır.

yürütmenin başlaması gereken dosya
`filename = "f1"`

her şeyin kilidi açık ve tamamen yükseltilmiş olarak başlayın
`sim_unlocks = Unlocks`

10000 havuç ve 50 saman ile başlayın
`sim_items = {Items.Carrot : 10000, Items.Hay : 50}`

değeri 13 olan "a" global değişkeni ile başlayın
`sim_globals = {"a" : 13}`

sabit bir rastgele tohum (seed) kullanın
`seed = 0`

simülasyonu 64 kat hızlandırın
`speedup = 64`

simülasyonu çalıştırın
`run_time = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)`

`simulate()` fonksiyonu, verilen başlangıç dosyasını simüle etmenin ne kadar sürdüğünü saniye cinsinden döndürür.

### Dosya Adı
Simulate fonksiyonunun ilk argümanı dosya adıdır. Bu, kod pencresinin en üstünde görüntülenen addır. Simülasyon, belirtilen dosyayı sanki üzerindeki Çalıştır düğmesine tıklamışsınız gibi çalıştıracaktır.

### Başlangıç Kilitleri
Döngüler, if ifadeleri, listeler, sözlükler gibi tüm programlama özellikleri her zaman açık kalacaktır.

İkinci argüman, programlama özelliklerine ek olarak simülasyonun hangi kilitlerle/yükseltmelerle başlaması gerektiğini belirtmenize olanak tanır. Bu bir kilitler dizisi olmalıdır. Simülasyon, dizideki tüm kilitler maksimum seviyeye yükseltilmiş olarak başlayacaktır.

Maksimum dışında bir yükseltme seviyesi belirtmek istiyorsanız, kilitleri kilit seviyeleriyle eşleştiren bir sözlük geçirebilirsiniz. Bu durumda, negatif değerler maksimum kilit seviyesine karşılık gelir.

### Başlangıç Eşyaları
Üçüncü argüman, eşyaları sayılarla eşleştiren bir sözlük geçirmenize olanak tanır. Simülasyonun hangi eşyalarla başlayacağını belirtir.

### Başlangıç Globalleri (Değişkenleri)
Simülasyon tamamen yeni bir program yürütmesi başlattığından, simülasyonu başlatan programdaki değişkenlere erişemezsiniz.
Ancak, dördüncü argümanı kullanarak simülasyona değerler geçirmek mümkündür. Bu, dize (string) biçimindeki değişken adlarını değerlerle eşleştiren bir sözlüktür. Bu değişkenler daha sonra simülasyon içindeki yürütmenin global kapsamına eklenir.

Bunun tüm değerleri kopyaladığını unutmayın, bu nedenle simülasyon içinde bunları değiştirmek simülasyon dışındaki orijinal değerleri etkilemeyecektir. Simülasyondan çalışması için geçen süre dışında değerler döndürmek mümkün değildir.

### Rastgele Tohum (Random Seed)
Beşinci argüman, simülasyonda kullanılan rastgele tohumu belirtmenize olanak tanır. Bu pozitif bir tamsayı olmalıdır. Negatif değerler rastgele bir tohum kullanılmasına neden olacaktır.

Rastgele tohum, bitki büyüme sürelerinden labirent düzenlerine ve suyun azalma sürelerine kadar her şeyi etkiler. Aynı simülasyonu aynı rastgele tohum ve aynı başlangıç koşullarıyla birden çok kez başlatırsanız, sonuç her zaman aynı olmalıdır.

### Hızlandırma (Speedup)
Altıncı argüman, simülasyonun başlangıç hızıdır. Bu, her şeyi hızlı bir şekilde test etmenizi sağlar. Oyun ayarlanan hıza yetişemezse otomatik olarak yavaşlayacaktır.

Hızlandırma simülasyonun sonucunu hiçbir şekilde etkilemez. Sadece bekleme süresini azaltmak için vardır.