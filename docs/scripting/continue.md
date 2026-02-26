# Continue
`continue`, bir döngünün o anki yinelemesini durdurarak en içteki döngünün bir sonraki yinelemesine atlamayı sağlar.

`for i in range(10):
	continue
    print("bu asla yazdırılmaz")`

Bu, döngünün `10` yinelemesini de çalıştırır, ancak `continue`dan sonraki `print` ifadesi her zaman atlanır.

`while` döngülerinde de çalışır.

`while True:
	if not can_harvest():
		continue
    
    harvest()`

Bu kod, `can_harvest()` sadece `True` olduğunda `harvest()` fonksiyonunu çağırır.
Şununla aynı etkiye sahiptir:

`while True:
	if can_harvest():
		harvest()`

İç içe döngülerde `continue` her zaman en içteki döngüyü etkiler.

`for i in range(10):
	for j in range(10):
	    print("bu 100 kez yazdırılır")
		continue
		print("bu asla yazdırılmaz")
	print("bu 10 kez yazdırılır")`