# Genişlet 2
Çiftliğiniz tekrar genişledi! Artık kareler güzel bir sıra halinde değil, bu yüzden kare bir ızgarayı (grid) dolaşmanın bir yolunu bulmanız gerekiyor.

Duyuların (senses) ve operatörlerin kilidini açana kadar `while` döngüsü ile bu mümkün değildir.
`for` döngüsünü tanıtmanın zamanı geldi.

`for` döngüsü hakkında her şeyi [For Döngüsü](docs/scripting/for.md) sayfasında okuyabilirsiniz, ancak şimdilik kodu yalnızca belirli sayıda tekrar etmek için ihtiyacınız olacak.

`#n kez takla at
for i in range(5):
	do_a_flip()`

`range(n)`, `0`'dan `n-1`'e kadar `n` elemanlı bir sayı aralığı oluşturur. `for` döngüsü, dizideki her öğe için döngü gövdesini bir kez çalıştırır. Bu örnekte `do_a_flip()` `5` kez çağrılacaktır.

`get_world_size()` fonksiyonu da artık kullanılabilir. Çiftliğinizin kenar uzunluğunu döndürür. Bu şekilde, bir sonraki genişletme yükseltmesiyle bozulmayacak kodlar yazabilirsiniz.

`for i in range(get_world_size()):
	harvest()
	move(North)`

Bu örnek, herhangi bir çiftlik boyutu için çiftliğin bir sütununu hasat eder.

Drone'u çiftlikte nasıl hareket ettireceğinizi bulmakta takıldıysanız aşağıdaki ipucuna bakın.
<spoiler=ipucunu göster>Elbette çiftlikte dolaşmanın birkaç yolu vardır.
Aradığımız şey, çiftlik tekrar büyüdüğünde bozulmayacak sistematik bir şekilde dolaşmanın bir yoludur.
Çiftlikteki her yere gitmenin sistematik bir yolu, aşağıdaki 2 adımı sonsuza kadar tekrarlamak olabilir:

1. Başa dönene kadar `North` (Kuzey) yönüne git.
2. `East` (Doğu) yönüne git.

Bu fikri koda dönüştürmek için `for i in range(get_world_size()):` yararlı olabilir.
</spoiler>
<spoiler=olası çözümü göster> Temel geçiş şöyle görünebilir:

`for i in range(get_world_size()):
	for j in range(get_world_size()):
		#her karede takla at
		do_a_flip()
		move(North)
	move(East)`
</spoiler>