# If
Kodu koşullu olarak çalıştırmak için if, elif ve else kullanabilirsiniz.

`if kosul1:
	do_a_flip()
elif kosul2:
	harvest()
else:
	do_a_flip()
	harvest()`

## Sözdizimi (Syntax)
`if`ler, kodu yalnızca bazı koşullar `True` (Doğru) ise çalıştırmanıza izin verir. Onlar döngü yapmayan bir `while` döngüsü gibidir.
`if`, tıpkı `while` döngüsü gibi bir koşul alır ve koşul `True` olarak değerlendirilirse if kod bloğunu yürütür:

`#koşul True ise takla at
if kosul:
	do_a_flip()`

Ayrıca if'den sonra, koşul `False` (Yanlış) olarak değerlendirilirse yürütülecek kodu tanımlayan bir `else` ekleyebilirsiniz.

`kosul` True ise takla at, aksi takdirde hasat et.
`if kosul:
	do_a_flip()
else:
	harvest()`

`elif`, "else if"in kısaltmasıdır.

`if kosul1:
	#a
else:
	if kosul2:
		#b
	else:
		#c`

şu şekilde kısaltılabilir:

`if kosul1:
	#a
elif kosul2:
	#b
else:
	#c`
