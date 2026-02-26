# Duyular (Senses)
Drone artık görebiliyor!

`get_pos_x()` ve `get_pos_y()` fonksiyonları drone'un mevcut x ve y konumunu döndürür. Başlangıç pozisyonunda ikisi de `0`'dır. x pozisyonu `East` (Doğu) yönünde her karede `1` artar ve y pozisyonu `North` (Kuzey) yönünde her karede `1` artar.

`num_items(item)` elinizde kaç tane eşya olduğunu döndürür.
Örneğin `num_items(Items.Hay)` ne kadar samanınız olduğunu döndürür.

`get_entity_type()` ve `get_ground_type()` drone'un altındaki varlığın veya zeminin türünü döndürür.

Bir çalının üzerindeyseniz takla atın:
`if get_entity_type() == Entities.Bush:
	do_a_flip()`

`None` (Hiç) anahtar kelimesinin de kilidi artık açıldı! `None`, hiçbir değer olmadığını temsil eden bir değerdir.
Örneğin, `return` ifadesi olmayan bir fonksiyon aslında `None` döndürür.

Drone'un altında bir varlık yoksa `get_entity_type()`, `None` döndürür.


Belirli bir kilitten kaç tane açtığınızı öğrenmek istiyorsanız `num_unlocked(unlock)` fonksiyonunu kullanın.

Örneğin, `num_unlocked(Unlocks.Speed)` sahip olduğunuz hız yükseltmelerinin sayısını döndürecektir.

`num_unlocked(Unlocks.Senses)`, duyular açık ise `1`, değilse `0` döndürür.

`num_unlocked()` fonksiyonunu Eşyalar (Items), Varlıklar (Entities) veya Zeminler (Grounds) üzerinde de kullanabilirsiniz. Bu, kilidi açıksa `1`, aksi takdirde `0` döndürür.

Dikkatli olun `num_unlocked(Unlocks.Carrots)`, kaç kez kilidinin açıldığını/yükseltildiğini döndürecektir.
`num_unlocked(Items.Carrot)` ise yalnızca `0` veya `1` döndürecektir. (Diğer bitkiler için de aynısı geçerlidir)