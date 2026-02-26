# Sözlükler (Dictionaries)
Sözlükler, anahtarları değerlerle eşleştirmenizi sağlayan bir veri yapısıdır; tıpkı gerçek bir sözlüğün kelimeleri tanımlarıyla eşleştirmesi gibi ve onlara çok hızlı bir şekilde bakabilirsiniz.

Bir sözlük şu şekilde oluşturulabilir:
`right_of = {North:East, East:South, South:West, West:North}`

İki nokta üst üste işaretinden önceki ifade anahtar (key) ve sonraki ifade, anahtarın eşleştiği değerdir (value).
Yukarıdaki sözlük, her bir yönü onun sağındaki yönle eşleştirir.

İşte drone'un konumunu üzerinde bulunduğu varlıkla eşleştiren bir başka örnek:
`x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}`

Bir anahtarla eşleşen değere erişmek, bir listedeki öğeye erişmeye benzer:
`value = dict[key]`

Örnek:
`orientation = right_of[South]`
Bu, `orientation` değişkenini `West` olarak ayarlar.

Bir sözlüğe şu şekilde yeni bir anahtar-değer çifti ekleyebilirsiniz:
`dict[key] = value`

Örnek:
`entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()`
Bu, mevcut konum için saklanan varlığı günceller.

Anahtarlar benzersizdir, bu nedenle sözlükte zaten var olan bir anahtarı eklemek önceki değerin üzerine yazacaktır.

`dict` sözlüğünden bir anahtar-değer çiftini kaldırmak için `dict.pop(key)` kullanın.

`key in dict`, eğer `key` sözlükte bir anahtarsa `True`, aksi takdirde `False` sonucunu verir.
Bu nedenle `dict` sözlüğünün anahtarı içerip içermediğini kontrol etmek için `if key in dict:` kullanabilirsiniz.

Bir sözlüğü bir for döngüsüne koymak, tüm anahtarlar üzerinde gezinmenizi sağlar:
`for key in dict:
	value = dict[key]`

Anahtarların yinelenme sırası hakkında hiçbir garanti yoktur.

Ayrıca bakınız [Kümeler (Sets)](docs/scripting/sets.md)