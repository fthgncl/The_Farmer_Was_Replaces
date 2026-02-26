# Ağaçlar (Trees)
[Ağaçlar](objects/tree) odun elde etmek için çalılardan daha iyi bir yoldur. Her biri 5 odun verir. Çalılar gibi çim veya toprak üzerine ekilebilirler.

Ağaçlar biraz alana sahip olmayı severler ve onları birbirinin hemen yanına dikmek büyümelerini yavaşlatır. Büyüme süresi, kuzeyinde, doğusunda, batısında veya güneyinde doğrudan bir karede bulunan her ağaç için iki katına çıkar. Yani her kareye ağaç dikerseniz, büyümeleri `2*2*2*2 = 16` kat daha uzun sürer.

<spoiler=göster> `%` operatörü burada yararlı olabilir. `%` operatörünün bölme işleminin kalanını döndürdüğünü unutmayın. `2`'ye bölünen çift sayıların kalanı `0`, `2`'ye bölünen tek sayıların kalanı `1`'dir.
Yani bir sayının çift olup olmadığını şu şekilde kontrol edebilirsiniz:

`def is_even(n):
	return n % 2 == 0`

Bu, n çift ise `True`, değilse `False` döndürür.
</spoiler>