# Kaktüs
Diğer bitkiler gibi [kaktüsler](objects/cactus) de toprakta yetiştirilebilir ve her zamanki gibi hasat edilebilir.

Ancak, çeşitli boyutlarda gelirler ve garip bir düzen anlayışına sahiptirler.

Tamamen büyümüş bir kaktüsü hasat ederseniz ve tüm komşu kaktüsler sıralı bir düzende ise, komşu kaktüsleri de özyinelemeli (rekürsif) olarak hasat edecektir.

Bir kaktüsün sıralı düzende olması için; `North` (Kuzey) ve `East` (Doğu)'daki komşu kaktüslerin tamamen büyümüş ve boyut olarak daha büyük veya eşit olması, `South` (Güney) ve `West` (Batı)'daki komşu kaktüslerin ise tamamen büyümüş ve boyut olarak daha küçük veya eşit olması gerekir.

Hasat yalnızca tüm bitişik kaktüsler tamamen büyümüşse ve sıralı düzendeyse yayılacaktır.
Bu, büyümüş kaktüslerden oluşan bir karenin boyuta göre sıralanmış olması durumunda, bir kaktüsü hasat ettiğinizde tüm kareyi hasat edeceği anlamına gelir.

Tamamen büyümüş bir kaktüs sıralanmamışsa kahverengi görünür. Sıralandığında tekrar yeşile dönecektir.

Hasat edilen kaktüs sayısının karesi kadar kaktüs elde edersiniz. Yani aynı anda `n` kaktüsü hasat ederseniz `n**2` adet `Items.Cactus` alırsınız.

Bir kaktüsün boyutu `measure()` ile ölçülebilir.
Her zaman şu sayılardan biridir: `0,1,2,3,4,5,6,7,8,9`.

Drone'un o yöndeki komşu karesini ölçmek için `measure(direction)` içine bir yön de verebilirsiniz.

`swap()` komutunu kullanarak bir kaktüsü herhangi bir yöndeki komşusuyla değiştirebilirsiniz.
`swap(direction)` drone'un altındaki nesneyi drone'un `direction` (yön) tarafındaki bir karedeki nesneyle değiştirir.

## Örnekler
Bu ızgaraların her birinde tüm kaktüsler sıralı düzendedir ve hasat tüm alana yayılacaktır:
`3 4 5    3 3 3    1 2 3    1 5 9
2 3 4    2 2 2    1 2 3    1 3 8
1 2 3    1 1 1    1 2 3    1 3 4`

Bu ızgarada, yalnızca sol alt kaktüs sıralı düzendedir, bu da yayılması için yeterli değildir:
`1 5 3
4 9 7
3 3 2`

<spoiler=1. ipucunu göster>
Satırlar zaten sıralanmışsa, sütunları sıralamak satırların sırasını bozmaz.
</spoiler>
<spoiler=2. ipucunu göster>
Sıralama algoritmalarına aşina değilseniz, internetten bakmak ve hangilerinin bu probleme uyarlanabileceğini düşünmek isteyebilirsiniz. Sadece komşu kaktüsleri değiştirebileceğiniz için hepsinin işe yaramayacağını unutmayın.
</spoiler>