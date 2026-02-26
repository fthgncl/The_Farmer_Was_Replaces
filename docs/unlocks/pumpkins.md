# Balkabakları (Pumpkins)
[Balkabakları](objects/pumpkin) sürülen toprakta havuç gibi büyür. Onları ekmek havuç maliyetindedir.

Bir karedeki tüm balkabakları tamamen büyüdüğünde, dev bir balkabağı oluşturmak için birlikte büyüyeceklerdir (birleşeceklerdir). Ne yazık ki, balkabaklarının tamamen büyüdüklerinde ölme ihtimali %20'dir, bu yüzden birleşmelerini istiyorsanız ölü olanları yeniden ekmeniz gerekecektir.

Bir balkabağı öldüğünde, hasat edildiğinde hiçbir şey düşürmeyecek ölü bir balkabağı bırakır. Yerine yeni bir bitki ekmek ölü balkabağını otomatik olarak kaldırır, bu nedenle hasat etmeye gerek yoktur. `can_harvest()` ölü balkabakları üzerinde her zaman `False` döndürür.

Dev bir balkabağının verimi, balkabağının boyutuna bağlıdır.

1x1 balkabağı `1` balkabağı verir.
2x2 balkabağı `4` yerine `2*2*2 = 8` balkabağı verir.
3x3 balkabağı `9` yerine `3*3*3 = 27` balkabağı verir.
4x4 balkabağı `16` yerine `4*4*4 = 64` balkabağı verir.
5x5 balkabağı `25` yerine `5*5*5 = 125` balkabağı verir.
`n`x`n` balkabağı, `n >= 6` için `n*n*6` balkabağı verir.

Tam çarpanı elde etmek için en az 6x6 boyutunda balkabakları elde etmek iyi bir fikirdir.

Bu, bir karedeki her kareye bir balkabağı ekseniz bile, balkabaklarından birinin ölebileceği ve mega balkabağının büyümesini engelleyebileceği anlamına gelir.
