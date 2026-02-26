# Sulama (Watering)
Bitkiler sulandıklarında daha hızlı büyürler. Toprağın `0` ile `1` arasında değişen bir su seviyesi vardır.
`get_water()` fonksiyonu, üzerindeki toprağın su seviyesini döndürür.

Bir bitkinin büyüme hızı, su seviyesi 0'da 1x hızdan, su seviyesi 1'de 5x hıza kadar doğrusal (lineer) olarak artar.

Zemin zamanla kurur: Ortalama olarak saniyede mevcut suyunun %1'ini kaybeder, ancak bunda rastgele bir varyans (sapma) vardır. Yüksek su seviyesini korumak, düşük su seviyesini korumaktan çok daha fazla su tüketecektir.

Bitkilerinizde su kullanabilirsiniz. Envanterinize her 10 saniyede bir otomatik olarak bir tank eklenir.
`Unlocks.Watering` yükseltmesi, her 10 saniyede bir aldığınız su miktarını ikiye katlayacaktır.

Bir tank `0.25` su tutar.

Zemini sulamak için herhangi bir zemin üzerinde `use_item(Items.Water)` çağrısı yapın.
