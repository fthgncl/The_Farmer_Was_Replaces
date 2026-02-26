# Fonksiyonlar
Yeni bir fonksiyon tanımlamak için `def` anahtar kelimesini kullanın:
`def f(arg1, arg2 = False):
	#fonksiyon kodu`

Fonksiyonu çağırmak için çağrı operatörü olan `()` kullanabilirsiniz:
`f(42)`

Ayrıca fonksiyonlardaki yerel ve genel değişkenler hakkında bilgi edinmek için [Kapsamlar (Scopes)](docs/scripting/scopes.md) konusuna bakın.

## Giriş
Zaten `harvest()` gibi yerleşik fonksiyonları gördünüz.
Ayrıca, kodunuzu modüler bir şekilde yapılandırmanıza olanak tanıyan kendi fonksiyonlarınızı da tanımlayabilirsiniz. Temel olarak bir kod bloğuna bir isim vermenizi sağlar, böylece onu istediğiniz yerden çağırabilirsiniz.

## Fonksiyon Tanımları
Örneğin, drone'u birkaç kez hareket ettiren bir fonksiyon tanımlayabilirsiniz.

`def move_n_dir(n, dir):
	for i in range(n):
		move(dir)`

`def` anahtar kelimesi bunun bir fonksiyon tanımı olduğunu bildirir.
`move_n_dir` fonksiyonun bağlandığı isimdir. Bu herhangi bir geçerli değişken ismi olabilir ve fonksiyonu çağırmak için kullanılacaktır.
`n` ve `dir` parametrelerdir. Bunlar fonksiyona geçirilen değerleri tutan değişkenlerdir (Bu değerlere argümanlar da denir). Bir fonksiyon tanımına istediğiniz kadar parametre ekleyebilirsiniz.
`:` işaretinden sonra, fonksiyon çağrıldığında çalışacak kod bloğu gelir.

Yukarıdaki tanımla birlikte aşağıdaki kod, drone'u `10` kare `North` (Kuzey) ve `2` kare `West` (Batı) yönüne hareket ettirir.

`move_n_dir(10, North)
move_n_dir(2, West)`

`def function():` gördüğünüzde bunu gerçekten şöyle bir değişken ataması olarak düşünmelisiniz:
`function = yeni_fonksiyon_nesnesi_olustur()`
Tüm atamalarda olduğu gibi, değişkeni atanmadan önce kullanamazsınız!
`def` ifadesi herhangi bir fonksiyon çağrısından önce çalışmalıdır.
Bu kod bir hata verecektir:

`func()
def func():
	pass`

## Dönüş Değerleri
Bir fonksiyonun bir değer döndürmesini sağlamak için `return` anahtar kelimesini kullanın.
Örneğin, aşağıdaki fonksiyon "özel veya" (exclusive or) işlemini tanımlar. Özel veya, bir değer `True` ve diğeri `False` ise `True` döndürür:

`def xor(a, b):
	return a != b

if xor(True, False):
	do_a_flip()`

[Demetler (Tuples)](docs/scripting/tuples.md) birden fazla değer döndürmeye izin verir.

## Varsayılan Argümanlar
Hiçbir argüman geçirilmezse kullanılacak varsayılan değerler de atayabilirsiniz.

`def f(a = False):
	if a:
		do_a_flip()

f()

f(True)`

Varsayılan değeri olan bir argümanı, varsayılan değeri olmayan bir argüman takip edemez.

## İleri Fonksiyon Kullanımı
Fonksiyonlar da diğer değerler gibi değerlerdir ve `def` ifadesi sadece bir atama ifadesi gibi davranarak fonksiyonu verdiğiniz isme atar.
Bu, şunun gibi şeyler yapmanıza olanak tanır:

`def f():
	def d():
		do_a_flip()
	return d

f()()`

Burada `f()`, yeni bir `d` fonksiyonu tanımlayan ve döndüren `f` fonksiyonunu çağırır. İkinci `()` daha sonra döndürülen fonksiyonu yürütür ve takla atar.
(Bu tür şeyler yapmak genellikle iyi bir fikir değildir çünkü ne olup bittiğini görmek zordur)

Diğer fonksiyonları argüman olarak alan fonksiyonlar gerçekten yaratıcı olmanızı sağlar:

`def f(g, arg):
	for _ in range(10):
		g(arg)

f(move, North)
f(use_item, Items.Fertilizer)`

Bu kod drone'u 10 kez `North` (Kuzey) yönüne hareket ettirir ve ardından 10 kez gübre kullanır.