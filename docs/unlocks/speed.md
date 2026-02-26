# Hız Yükseltmesi
Yürütme hızı iki katına çıkarıldı. Sorun şu ki, drone artık çimin büyüyebileceğinden daha hızlı hasat yapıyor ve bu da hiç hasat yapılamamasına neden oluyor. Bunun üstesinden gelmek için [if](docs/scripting/if.md) dalları ve [can_harvest](functions/can_harvest) fonksiyonu artık açıldı.

## Hasattan Önce Kontrol
Şimdiye kadar koşul olarak sadece `True` ve `False` vardı, bu da elbette `if` ile çok kullanışlı değil.

Yeni can_harvest() fonksiyonu daha iyi bir koşul sağlar. `can_harvest()`, drone'un altındaki bitki hasat edilebilirse `True`, aksi takdirde `False` döndürür.

`if can_harvest():
	#bir şeyler yap`

Bu fonksiyonu bu şekilde bir koşul olarak kullanabilmenizin nedeni, bir boolean değeri döndürmesidir.

Bir dönüş değeri, işlevsellik yürütüldükten sonra fonksiyon çağrısı ifadesinin döndürülen değer olarak değerlendirildiği (sonuçlandığı) anlamına gelir.

Yukarıdaki kod çalıştığında ne olur:
	-if çalışır
	-`can_harvest()` çağrılır
	-`can_harvest()` işini yapar
	-`can_harvest()`, `True` veya `False` döndürür
	-ifade artık `if True:` veya `if False:` olur
	-kod bloğu yalnızca hasat yapabiliyorsa yürütülür

Artık drone'un çok erken hasat yapmasını önlemek için `if` kullanabiliriz.