# For Döngüsü
`for` döngüsü Python'daki gibi çalışır. (Bazı dillerde buna foreach döngüsü denir, C tarzı for döngüsü ile karıştırılmamalıdır, o farklı bir şeydir).

`for i in dizi:
	#i ile bir şeyler yap`

`while` döngüsüne benzer şekilde, `for` döngüsü de bir kod bloğunu tekrar tekrar çağırır. Bir koşula dayalı döngü yapmak yerine, bir dizideki her öğe için döngü gövdesini bir kez yürütür.

## Sözdizimi (Syntax)
Bir for döngüsü şöyle görünür:

`for degisken_adi in dizi:
	#kod bloğu`

`degisken_adi` seçtiğiniz herhangi bir isim olabilir. Dizideki mevcut öğeyi saklayan bir değişkendir. `dizi` (sequence), bir sayı aralığı gibi yinelenebilen bir değer olmalıdır. Kod bloğu, her öğe için döngü değişkeni o öğeye atanmış olarak yürütülür.

## Diziler (Sequences)
[Aralıklar (Ranges)](functions/range)      <unlock=lists>[Listeler](docs/scripting/lists.md)      </unlock><unlock=functions>[Demetler (Tuples)](docs/scripting/tuples.md)      </unlock><unlock=dicts>[Sözlükler](docs/scripting/dicts.md)      </unlock><unlock=sets>[Kümeler](docs/scripting/sets.md)</unlock>

## Örnek
`for i in range(5):
    harvest()`

Bu döngü, gövdeyi sabit sayıda yürütür. Şunu yazmakla esasen aynıdır:

`i = 0
harvest()
i = 1
harvest()
i = 2
harvest()
i = 3
harvest()
i = 4
harvest()`

Yani `harvest()` fonksiyonunu 5 kez çağırır.

Ayrıca bakınız: [Break](docs/scripting/break.md) ve [Continue](docs/scripting/continue.md)