# Çoklu Kültür (Polyculture)
Bazen bitkilerin birlikte ekildiğinde daha fazla verim verdiğini zaten fark etmiş olabilirsiniz.
Çim, çalılar, ağaçlar ve havuçlar doğru bitki arkadaşına sahip olduklarında daha fazla verim verirler. Arkadaş (kardeş bitki) tercihi her bitki için farklıdır ve tahmin edilemez. Neyse ki, drone'un altındaki bitkinin arkadaş tercihi `get_companion()` kullanılarak ölçülebilir. İlk elemanın arkadaşı olarak istediği bitki türü ve ikinci elemanın arkadaşını istediği konum olduğu bir demet (tuple) döndürür.

`plant_type, (x, y) = get_companion()`

Örneğin bir çalı ekerseniz ve ardından `get_companion()` çağırırsanız `(Entities.Carrot, (3, 5))` gibi bir şey döndürecektir. Bu, bu çalının `(3,5)` konumunda havuç olmasını istediği anlamına gelir. Yani `(3,5)` konumuna havuç ekerseniz ve ardından çalıyı hasat ederseniz, daha fazla odun verecektir. Havucun büyüme aşaması önemli değildir.

Bir bitkinin arkadaş tercihi `Entities.Grass` (Çim), `Entities.Bush` (Çalı), `Entities.Tree` (Ağaç) veya `Entities.Carrot` (Havuç) olabilir. Her bitki bunu rastgele seçer, ancak her zaman kendisinden farklı bir bitki seçecektir. Konum ayrıca, bitkinin kendi konumu hariç, bitkinin 3 hareket mesafesi içindeki herhangi bir konum olabilir.

Drone'un altında arkadaş tercihi olan bir bitki yoksa `get_companion()` `None` döndürür.

Çoklu kültürün kilidi açılmadan önce verim çarpanı `5`'tir. Her yükselttiğinizde ikiye katlanır.