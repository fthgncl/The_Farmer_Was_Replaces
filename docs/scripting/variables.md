# Değişkenler
Değişkenler, bir değeri tutabilen isimlendirilmiş kaplar olarak düşünülebilir.
`=` operatörü bir değişken bildirmek ve içinde bir değer saklamak için kullanılır.

`degisken_adi = deger`

Operatörün sol tarafı değişken ismidir. Ona istediğiniz herhangi bir ismi verebilirsiniz.
Sağ taraf ise sonucu değişkende saklanacak olan bir ifadedir.

`a` adında bir değişken bildirin ve içinde `5` değerini saklayın:
`a = 5`
`b` adında bir değişken bildirin ve içinde `can_harvest()` fonksiyonunun dönüş değerini saklayın:
`b = can_harvest()`

`=` operatörünü `==` operatörü ile karıştırmayın.
`==` operatörü iki değerin eşit olup olmadığını kontrol eder ve `True` (Doğru) veya `False` (Yanlış) döndürür.
`=` operatörü sağdaki değeri soldaki isme atar.

Bir değişkene atama yapıldıktan sonra, içerdiği değeri almak için kodda kullanabilirsiniz.

`a = 5
for i in range(a):
	do_a_flip()`

Yukarıdaki döngü 5 kez çalıştırılır çünkü `a` `5` olarak ayarlanmıştır.
`for` döngüsündeki `i` de, döngünün her yinelemesinde (iterasyon) sıranın mevcut değerinin otomatik olarak atandığı bir değişkendir. (Adı `i` olmak zorunda değildir, herhangi bir geçerli değişken ismini verebilirsiniz.)

Değişkenler ayrıca `while` döngüsüyle de aynı şeyi yapmanızı sağlar:

`a = 5
i = 0
while i < a:
	do_a_flip()
	i = i + 1`

Bu, yukarıdaki `for` döngüsüyle aynı şeyi yapar. Sadece `i`'yi manuel olarak artırmamız gerekir.
`i`'yi artırmak için, onu kendi değeri artı `1` olacak şekilde ayarladığımıza dikkat edin. Bir değişkenin değerini önceki değerine göre değiştirmek çok yaygın bir durumdur.
Bu operatörler kullanılarak kısaltılabilir: `+=, -=, *=, /=, %=`

`i = i + 1` ile `i += 1` aynıdır.
`a = a / 3` ile `a /= 3` aynıdır.
