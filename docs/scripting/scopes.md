# İsim Kapsamları (Scopes)
Kapsamlar, hangi değişkenlere nereden erişilebileceğini belirler. Bir kapsam temel olarak isimlerden değerlere bir eşlemedir.
Temelde Python'daki gibi çalışırlar.

Bir global (genel) kapsam vardır ve her fonksiyonun bir yerel (local) kapsamı vardır.
Bir değişken tanımladığınızda, mevcut kapsama eklenir.
Bir fonksiyon tanımının dışındaki her şey global kapsamın bir parçası olarak kabul edilir.

`x = 1`
Global kapsamdaki `x` ismine `1` değerini atar.

Bu `def` ifadesi, global kapsamdaki `f` ismine bir fonksiyon atar.
`def f():
    `f'nin yerel kapsamında y ismine 1 değerini atar.`
    y = 1

    `f'nin yerel kapsamında g ismine bir fonksiyon atar.`
    def g():
        pass`

`f()`
Global kapsamdan `f` içinde saklanan fonksiyonu alır ve çağırır.

`print(y)`
Global kapsamdaki bu yazdırma ifadesi bir hata verir çünkü `y` global kapsamda hiç bildirilmemiştir, bu yüzden onu buradan okuyamayız.
Sadece `f`'nin yerel kapsamında mevcuttu.

## Global Anahtar Kelimesi
Varsayılan olarak, fonksiyonlardaki tüm değişkenler, global kapsamda aynı isme sahip bir değişken olsa bile yerel kapsama bağlanır.

`x = 0

def f():
    x = 1
f()
print(x)`

Bu kod `0` yazdırır çünkü `f` içindeki yerel `x`, global `x` ile aynı değişken değildir, bu yüzden global `x` değişmeden kalır. Bu önemlidir çünkü aksi takdirde bir fonksiyon çağrısı, yanlışlıkla o fonksiyonun yerel değişkeniyle aynı isme sahip olan bir global değişkenin üzerine yazabilir.

Global bir değişkene yazmak istiyorsanız, bunu `global` anahtar kelimesini kullanarak açıkça yapmalısınız.

`x = 0

def f():
    global x
    x = 1
f()
print(x)`

Bu örnekte, `global x`, `x`'i yukarıda tanımlanan global `x` değişkenine bağlar. Bu şimdi `1` yazdıracaktır.
Global değişkenleri değiştirmenin genellikle spagetti koda (programın her parçasının programın diğer her parçasını etkilediği durum) doğru atılan ilk adım olduğunu unutmayın, bu yüzden aşırı kullanmayın.

## Döngüler ve Dallar
Döngüler ve dallar kendi kapsamlarını oluşturmazlar, bu nedenle içlerinde bildirilen herhangi bir şey dışarıda da kullanılabilir.

`for i in range(3):
    pass
print(i)`

Bu `2` yazdıracaktır çünkü `for` döngüsünün son yinelemesi `i`'ye `2` atamıştır.