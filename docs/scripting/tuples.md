# Demetler (Tuples)
Demetler, birden çok değeri tek bir değerde birleştirmenin harika bir yoludur.
Bir demet oluşturmak için değerleri virgülle ayırmanız yeterlidir:

`tuple = 1, 2`

Bunları tekrar birkaç değişkene de açabilirsiniz (unpack). Aşağıdaki kodda, `(1,2)` demeti `a` ve `b` adlı iki değişkene açılır.

`a, b = 1, 2`

Demetler listeler gibi indekslenebilir, ancak değiştirilemezler (immutable) ve oluşturulduktan sonra değiştirilemezler.

`tuple = 1, 2`

`print(tuple[1])`
`2` yazdırır

`tuple[0] = 3`
hata verir

<unlock=dicts>
Listelerin aksine demetler sözlüklerde anahtar olarak kullanılabilir.

`d = {(1,2):(4,5)}

print(d[(1,2)])`
`(4,5)` yazdırır</unlock>

Bir fonksiyonda birden fazla değer döndürmek için de yararlı olabilirler.

`def f():
    return 1, 2

a, b = f()`