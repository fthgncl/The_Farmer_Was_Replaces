# Kümeler (Sets)
Kümeler [sözlükler](docs/scripting/dicts.md) gibidir, ancak değerleri yoktur. Sadece sırasız bir anahtarlar kümesidir.

Sözlükler gibi oluşturulurlar, ancak değerler olmadan.
`set = {North, East, West}`

Boş bir küme oluşturmak için `set()` kullanın. `{}` ifadesinin boş bir sözlük oluşturduğuna dikkat edin.

Kümeye yeni bir öğe eklemek için `set.add(elem)` kullanın.

Kümeden bir öğeyi kaldırmak için `set.remove(elem)` kullanın.

Kümenin bir öğeyi içerip içermediğini kontrol etmek için `if elem in set:` kullanın.

Kümedeki tüm öğeleri yinelemek için `for elem in set:` kullanın.
Daha büyük kümeler için `in` operatörü bir listede olacağından çok daha hızlı çalışır.

Tıpkı sözlükler gibi, kümeler de sırasızdır, bu nedenle öğelerin yinelenme sırası hakkında hiçbir garanti yoktur.

Ayrıca, kümelerdeki öğeler benzersizdir, bu nedenle kümede zaten bulunan bir öğeyi eklemek kümeyi değiştirmeyecektir.