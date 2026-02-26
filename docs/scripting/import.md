# İçe Aktarma (Import)
Tüm kodunuzu tek bir dosyaya koymak hızla yönetilemez hale gelir.
`import` ifadeleri, başka bir dosyadan fonksiyonları ve global değişkenleri içe aktarmanıza olanak tanır.
Tek bir ekran görüntüsünde nasıl çalıştığı:
![](ImportsInOnePicture400)

Burada `import module2`, `module2` adlı dosyayı çalıştırır ve tüm globallerine erişmenizi sağlar.
Daha sonra `.` operatörünü kullanarak içe aktarılan modüldeki değişkenlere ve fonksiyonlara erişebilirsiniz.
Yani bu örnekte, `module2.print_x()`, `module2` içindeki `print_x()` fonksiyonunu çağırır.

### Daha fazla okumanıza gerek yok

Ayrıca `from` sözdizimini kullanarak içe aktarılan modüldeki globalleri, import ifadesinin çalıştırıldığı geçerli kapsama taşıyabilirsiniz.

`from module2 import print_x
print_x()`
`module2`'den yalnızca belirtilen globalleri içe aktarır.

veya

`from module2 import *
print_x()`
`module2`'den tüm globalleri içe aktarır.

Bu aynı zamanda `module2` dosyasını da içe aktarır, ancak ona `module2` adlı bir değişken aracılığıyla erişmek yerine, `module2`'deki globalleri paketinden çıkarır ve bunları doğrudan yerel kapsama atar.

Bu içe aktarma biçimi genellikle önerilmez çünkü iki dosya birbirini içe aktardığında iyi çalışmaz ve isim çakışmaları nedeniyle içe aktaran dosyadaki değişkenlerin üzerine yanlışlıkla yazabilirsiniz. Ne yaptığınızı bilmiyorsanız `from` sözdiziminden kaçınmak daha güvenlidir.

# Gerçekte nasıl çalışır

## Özet (TLDR)
İçe aktarmalar oldukça sezgisel olmayabilir, ancak `from file import` yerine `import file` sözdizimine bağlı kalarak ve global tanım olmayan her şeyi şunun içine sararak çoğu sorundan kaçınılabilir:
`if __name__ == "__main__":`

## İçe Aktarma Yan Etkileri
Bir dosyayı ilk kez içe aktardığınızda, dosyanın tamamını çalıştırır ve ardından yürütme sırasında tanımlanmış tüm değişkenlere erişmenizi sağlar.
Aynı dosyayı tekrar içe aktarırsanız, yalnızca ilk seferki önbelleğe alınmış modülü tekrar döndürür.

Bu, içe aktarma ifadelerinin yan etkileri olabileceği anlamına gelir. `harvest()` çağıran bir dosyayı içe aktarırsanız, içe aktarma sırasında aslında hasat yapacaktır. Ancak tekrar içe aktardığınızda, tekrar hasat yapmaz çünkü dosya yalnızca bir kez çalıştırılır.

`__name__` değişkenini kullanarak bu tür yan etkilerden kaçınmanın bir yolu vardır. Bu, bir dosya doğrudan çalıştırıldığında `"__main__"` olarak ve `import` yoluyla çalıştırıldığında dosyanın adına otomatik olarak ayarlanan bir değişkendir.
Dosya içe aktarıldığında çalışmasını istemediğiniz herhangi bir kodu bir `if __name__ == "__main__":` bloğunun içine koymak iyi bir uygulama olarak kabul edilir.

Python'da yaygın bir dosya yapısı, dosya çalıştırıldığında yürütülmesi gereken kodu bir `main()` fonksiyonuna koymaktır. Bu sayede yerel değişkenler (`main()` içinde tanımlanan) ile içe aktarılabilen global değişkenler (`main()` dışında tanımlanan) arasında net bir ayrım yaparsınız.

`a_global_variable = "global"

def main():
    a_local_variable = "local"
    # bir şeyler yap

if __name__ == "__main__":
    main()`

## İçe Aktarma Döngüleri
`a` dosyası `b` dosyasını ve `b` dosyası `a` dosyasını içe aktarırsa ne olur?

`a` dosyası:
`import b
x = 0`

`b` dosyası:
`import a
def f():
    print(a.x)`

Bu gayet iyi çalışacaktır. Diyelim ki iki dosya da henüz yüklenmedi ve başka biri `import a` komutunu çalıştırdı.

-`a`, `import b` satırına kadar çalışır.
-`b`, `import a` satırına kadar çalışır.
-`a` modülü zaten mevcuttur, ancak henüz sadece `import b` satırına ulaştığı için `x`'i içermez.
-`b`, yarı yüklenmiş `a` modülüne bir referansı `a` adlı bir değişkende saklar.
-`b`, `def` ifadesini çalıştırır ve `f()` fonksiyonunu saklar.
-`a` çalışmaya devam eder ve `x`'i başlatır.

Biri `b.f()` çağırdığında, doğru bir şekilde `0` yazdırır çünkü `b`'nin referansına sahip olduğu `a` modülü artık tamamen yüklenmiştir.

Şimdi aynı kodu `from` sözdizimini kullanarak düşünün.

`a` dosyası:
`from b import *
x = 0`

`b` dosyası:
`from a import *
def f():
    print(x)`

-`a`, `from b import *` satırına kadar çalışır.
-`b`, `from a import *` satırına kadar çalışır.
-`a` modülü zaten mevcuttur, ancak henüz tam olarak yürütülmemiştir.
-`b`, şu anda `a` içinde olan her şeyi kendi global kapsamına çıkarır. Bu noktada, `a` henüz `x = 0` satırına ulaşmadığı için hiçbir şey içermez, dolayısıyla hiçbir şey içe aktarılmaz.
-`b`, `def` ifadesini çalıştırır ve `f()` fonksiyonunu saklar.
-`a` çalışmaya devam eder ve `x`'i başlatır.

Biri şimdi `b.f()` çağırırsa, mevcut kapsamda `x`'in olmadığına dair bir hata alırlar. Bunun nedeni, bu sefer `b`'nin hala yüklenmekte olan `a`'ya bir referansı olmaması ve içe aktarmadan sonra eklenen tanımları görmemesidir.