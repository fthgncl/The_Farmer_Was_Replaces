# Ayçiçekleri (Sunflowers)
[Ayçiçekleri](objects/sunflower) güneşin gücünü toplar. Bu gücü hasat edebilirsiniz.

Onları ekmek, havuç veya balkabağı ekmekle tamamen aynı şekilde çalışır.

Büyümüş bir ayçiçeğini hasat etmek güç verir.
Çiftlikte en az 10 ayçiçeği varsa ve en fazla taç yaprağına sahip olanı hasat ederseniz `5` kat daha fazla güç alırsınız!

`measure()`, drone'un altındaki ayçiçeğinin taç yaprağı sayısını döndürür.
Ayçiçeklerinin en az `7` ve en fazla `15` taç yaprağı vardır.
Tamamen büyümeden önce de ölçülebilirler.

Birkaç ayçiçeği aynı sayıda taç yaprağına sahip olabilir, bu nedenle en fazla taç yaprağına sahip birkaç ayçiçeği de olabilir. Bu durumda, hangisini hasat ettiğiniz önemli değildir.

Gücünüz olduğu sürece drone onu iki kat daha hızlı çalışmak için kullanacaktır.
Her 30 eylemde (hareket, hasat, ekim gibi...) 1 güç tüketir.
Diğer kod ifadelerini yürütmek de güç kullanabilir ancak drone eylemlerinden çok daha azdır.

Genel olarak, hız yükseltmeleriyle hızlandırılan her şey güçle de hızlandırılır.
Güç ile hızlandırılan her şey, hız yükseltmelerini göz ardı ederek yürütülmesi için geçen süreyle orantılı olarak güç kullanır.
