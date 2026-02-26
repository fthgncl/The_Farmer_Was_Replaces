# While Döngüsü
`while` döngüsünün ve `True` (Doğru) ile `False` (Yanlış) değerlerinin kilidini açtınız. `while` döngüsü, koşul `True` olduğu sürece döngü gövdesini yürütmeye devam eder.

`while kosul:
	#döngü gövdesi`

Sonsuz döngüler oluşturma konusunda endişelenmeyin. Yürütmedeki gecikmeler programın donmasını önleyecektir.

## Yeni Başlayanlar İçin
Belki de arka arkaya birkaç `harvest()` çağrısı koymayı denemişsinizdir:

`harvest()
harvest()
harvest()`

Bu, bir program çalışmasında birkaç kez hasat yapmanızı sağlar.
Ancak, üçten fazla kez hasat yapmak daha iyi olurdu ve aynı kodu birden fazla kez yazmak kötü bir uygulamadır.
Çözüm bir döngüdür.
Bir döngü, aynı kodu birden fazla kez çalıştırmanıza olanak tanır.

`while` döngüsü bir koşul alır; bu koşul yalnızca iki durumdan birinde olabilen mantıksal bir değerdir: `True` veya `False`.
Böyle bir değere Boolean (Mantıksal) değeri denir.

Döngü daha sonra koşul `False` olana kadar döngü içindeki kodu yürütür.
`while` döngüsü şöyle görünür:

`while kosul:
	#döngü gövdesi
	#döngü gövdesi
	#...`

Burada "kosul"u bir boolean değeriyle ve `#döngü gövdesi`ni döngüde yapmak istediğiniz şeyle değiştirmelisiniz.

Kullanılabilir iki sabit boolean değeri vardır. Sabitler, program sırasında asla değişmeyen değerlerdir.

Her zaman `True` olan sabit bir boolean değeri oluşturmak için sadece `True` yazabilirsiniz. Her zaman `False` olacak sabit bir boolean değeri olarak `False` yazın.
Yani ya şöyle yazabilirsiniz:

`while False:
	do_a_flip()`

ya da

`while True:
	do_a_flip()`

Birincisi asla takla atmaz, ikincisi ise sonsuza kadar takla atar (sonsuz döngü).

Normalde sonsuz bir döngü oluşturmak kötü bir fikirdir çünkü programı dondurur, ancak bu oyunda döngünün her yinelemesi arasında gecikmeler vardır, bu yüzden siz tekrar çalıştır düğmesine basarak manuel olarak durdurana kadar drone'un takla atmaya devam etmesine neden olur.

İki nokta üst üste işaretinden sonraki satırın nasıl girintilendiğine dikkat edin. Bunun gibi girintiler kod bloklarını ayırmak için kullanılır.
Girinti eklemek için Tab tuşuna, kaldırmak için Shift + Tab (veya Backspace) tuşuna basın.

Döngü, iki nokta üst üste işaretinden sonraki tüm girintili ifadeleri tekrarlayacaktır.
Girintili bloktan sonraki ifadeler, döngü bittikten sonra yürütülecektir.
