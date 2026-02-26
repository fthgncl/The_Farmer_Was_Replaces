# Listeler
Listeler, tek bir değişkende birden fazla değer saklamanın kolay bir yoludur.
Şu şekilde yeni listeler oluşturabilirsiniz:

`list = [2, True, Items.Hay]`

Liste şimdi `2`, `True` ve `Items.Hay` değerlerini içerir.
Bir liste boş da olabilir:

`empty_list = []`

Bir listenin öğesine dizini (indeksi) ile erişebilirsiniz. Dizin ilk öğe için `0`, ikinci öğe için `1`, üçüncü için `2`'dir...

havuç eker
`list = [Entities.Tree, Entities.Carrot, Entities.Pumpkin]
plant(list[1])`

Bir `for` döngüsü kullanarak bir liste üzerinde gezinebilirsiniz. Aşağıdaki örnek listedeki tüm öğeleri toplar.

`list = [4, 7, 2, 5]
sum = 0
for number in list:
	sum += number`
`sum` (toplam) şimdi `18` olur

Aşağıdaki liste yöntemleri (metodları) öğe eklemenize ve kaldırmanıza olanak tanır:

`list.append(elem)` listenin sonuna bir öğe ekler:

`list = [2, 6, 12]
list.append(7)`
`list` şimdi `[2, 6, 12, 7]`

`list.remove(elem)` bir listeden bir öğenin ilk oluşumunu kaldırır:

`list = [1, 2, 4, 2]
list.remove(2)`
`list` şimdi `[1, 4, 2]`

`list.insert(index, elem)` verilen dizine bir öğe ekler:

`list = [Entities.Tree, Items.Hay]
list.insert(1, Items.Wood)`
`list` şimdi `[Entities.Tree, Items.Wood, Items.Hay]`

`list.pop(index)` belirtilen dizindeki öğeyi kaldırır.
Hiçbir dizin belirtilmezse, son öğe kaldırılır.

`list = [3, 5, 8, 25]
list.pop()`
`list` şimdi `[3, 5, 8]`
`list.pop(1)`
`list` şimdi `[3, 8]`

`len()` fonksiyonu listenin uzunluğunu döndürür.
`list = [3, 2, 1]
x = len(list)`
`x` şimdi `3`

Listeler referans anlambilimine (semantics) sahiptir. Bu, bir listeyi bir değişkene atamanın, listenin bir kopyasını oluşturmak yerine aynı liste nesnesini o değişkene atadığı anlamına gelir.
İki değişken aynı listeye başvuruyorsa, listedeki değişiklikler her ikisi tarafından da görülür.

`a = [1,2]
b = a
b.pop()`
`a` ve `b`'nin her ikisi de şimdi `[1]` olur
