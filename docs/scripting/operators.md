# Operatörler
aritmetik operatörler: `+, -, *, /, //, %, **`
karşılaştırma operatörleri: `==, !=, <=, >=, <, >`
mantıksal operatörler: `not, and, or`

Not: Oyundaki tüm sayılar kayan noktalı (floating point) sayılardır. Yani tüm aritmetik operatörler kayan noktalı operatörlerdir.
`//`, bölme işleminden sonra sayıyı aşağı yuvarlamak (taban) için tanımlanmıştır.

Atama operatörleri için "Değişkenler" kilidini açmanız gerekir.

## Giriş
Operatörler değerleri karşılaştırmanızı, değiştirmenizi ve birleştirmenizi sağlar.
`+, -, *, /, //, %, **` aritmetik operatörleri sayılar üzerinde yaygın matematiksel işlemleri gerçekleştirmek için kullanılır.
`==, !=, <=, >=, <, >` karşılaştırma operatörleri değerleri karşılaştırmak için kullanılır. Sonuç her zaman ya `True` (Doğru) ya da `False` (Yanlış) olur.
Mantık operatörleri (aynı zamanda boolean operatörleri olarak da adlandırılır) `not, and, or` doğruluk değerlerini birleştirmek için kullanılır.

## Aritmetik Operatörler
`+` ve `-` toplama ve çıkarma için kullanılır.

`2 + 3` sonucu `5` olur
`3 - 2` sonucu `1` olur

`*`, `/` ve `//` çarpma ve bölme için kullanılır.

`2 * 3` sonucu `6` olur
`5 / 2` sonucu `2.5` olur

`//`, `/` ile aynı şeyi yapar ancak sonuç aşağı yuvarlanır (bir sonraki tamsayıya yuvarlanır).

`5 // 2` sonucu `2` olur

`%` mod operatörüdür, kalan operatörü olarak da bilinir. Esasen iki sayıyı böler ve ardından kalanı döndürür. Bunu, kalan sağdaki sayıdan küçük olana kadar sağdaki sayıyı soldaki sayıdan tekrar tekrar çıkarmak olarak da düşünebilirsiniz.

`4 % 2` sonucu `0` olur
`5 % 2` sonucu `1` olur
`6 % 2` sonucu `0` olur
`2 % 6` sonucu `2` olur
`1.5 % 1` sonucu `0.5` olur

`**` üs alma operatörüdür.

`2**2` sonucu `4` olur
`(-5)**3` sonucu `-125` olur

## Karşılaştırma Operatörleri
`==` ve `!=`, iki değerin "eşit" (`==`) veya "eşit değil" (`!=`) olup olmadığını kontrol etmek için kullanılır. Her türlü değer üzerinde kullanılabilirler.

`2 == 2` sonucu `True` olur
`Entities.Bush != Entities.Bush` sonucu `False` olur
`3 != 3 + 1` sonucu `True` olur

`<=, >=, <, >` sadece sayılar üzerinde kullanılabilir. Soldaki sayının sağdaki sayıdan "küçük veya eşit" (`<=`), "büyük veya eşit" (`>=`), "küçük" (`<`) veya "büyük" (`>`) olup olmadığını kontrol ederler.

`1 <= 1` sonucu `True` olur
`2 >= 3` sonucu `False` olur
`-2 < -1` sonucu `True` olur
`6 > 6` sonucu `False` olur

## Mantık Operatörleri
`not` sadece değeri tersine çevirir:

`not False` sonucu `True` olur
`not True` sonucu `False` olur

`and` yalnızca her iki değer de `True` ise `True` sonucunu verir

`True and True` sonucu `True` olur
`True and False` sonucu `False` olur
`False and False` sonucu `False` olur

`or` değerlerden en az biri `True` ise `True` sonucunu verir

`True or True` sonucu `True` olur
`True or False` sonucu `True` olur
`False or False` sonucu `False` olur