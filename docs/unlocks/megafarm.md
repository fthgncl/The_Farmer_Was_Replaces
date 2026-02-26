# Mega Çiftlik (Mega Farm)
Bu inanılmaz derecede güçlü kilit açma, birden fazla drone'a erişmenizi sağlar.

Daha önce olduğu gibi, hala sadece bir drone ile başlarsınız. Ek drone'lar önce oluşturulmalıdır (spawn) ve program sona erdikten sonra kaybolacaktır.
Her drone kendi ayrı programını çalıştırır
Yeni drone'lar `spawn_drone(function)` fonksiyonu kullanılarak oluşturulabilir.

`def drone_function():
    move(North)
    do_a_flip()

spawn_drone(drone_function)`

Bu, `spawn_drone(function)` komutunu çalıştıran drone ile aynı konumda yeni bir drone oluşturur. Yeni drone daha sonra belirtilen fonksiyonu yürütmeye başlar. İşiniz bittiğinde otomatik olarak kaybolacaktır.

Drone'lar birbirleriyle çarpışmaz.

Oluşturulabilecek maksimum drone sayısını almak için `max_drones()` kullanın.
Çiftlikte halihazırda bulunan drone sayısını almak için `num_drones()` kullanın.


## Örnek:
`def harvest_column():
    for _ in range(get_world_size()):
        harvest()
        move(North)

while True:
    if spawn_drone(harvest_column):
        move(East)`

Bu, ilk drone'unuzun yatay olarak hareket etmesine ve daha fazla drone oluşturmasına neden olacaktır. Oluşturulan drone'lar daha sonra dikey olarak hareket edecek ve yollarına çıkan her şeyi hasat edecektir.

Mevcut tüm drone'lar zaten oluşturulmuşsa, `spawn_drone()` hiçbir şey yapmaz ve `None` döndürür.

İşte her drone'a farklı bir yön geçiren başka bir örnek.
`for dir in [North, East, South, West]:
    def task():
        move(dir)
        do_a_flip()
    spawn_drone(task)`

<spoiler=ipucunu göster> Her çiftlik karesinde herhangi bir fonksiyonu çalıştıran bu süper kullanışlı paralel `for_all` fonksiyonuna göz atın. Bunu yapmak için mevcut tüm drone'ları kullanır.

`def for_all(f):
	def row():
		for _ in range(get_world_size()-1):
			f()
			move(East)
		f()
	for _ in range(get_world_size()):
		if not spawn_drone(row):
			row()
		move(North)

for_all(harvest)`

Özellikle yararlı bir kalıp, varsa bir drone oluşturmak, aksi takdirde bunu kendiniz yapmaktır.

`if not spawn_drone(task):
	task()`
</spoiler>

## Başka Bir Drone'u Beklemek
Başka bir drone'un bitirmesini beklemek için `wait_for(drone)` fonksiyonunu kullanın. Drone'u oluşturduğunuzda `drone` referansını alırsınız.
`wait_for(drone)`, diğer drone'un çalıştırdığı fonksiyonun dönüş değerini döndürür.

`def get_entity_type_in_direction(dir):
    move(dir)
    return get_entity_type()

def zero_arg_wrapper():
    return get_entity_type_in_direction(North)
drone = spawn_drone(zero_arg_wrapper)
print(wait_for(drone))`

Drone oluşturmanın zaman aldığını unutmayın, bu nedenle her küçük şey için yeni bir drone oluşturmak iyi bir fikir değildir.

Drone'un bitip bitmediğini beklemeden kontrol etmek için `has_finished(drone)` kullanabilirsiniz.

## Paylaşılan Bellek Yok
Her drone'un kendi belleği vardır ve doğrudan başka bir drone'un globallerini okuyamaz veya yazamaz.

`x = 0

def increment():
    global x
    x += 1

wait_for(spawn_drone(increment))
print(x)`

Bu `0` yazdıracaktır çünkü yeni drone, global `x`'in kendi kopyasını artırmıştır, bu da ilk drone'un `x`'ini etkilemez.

## Yarış Durumları (Race Conditions)
Birden fazla drone aynı anda aynı çiftlik karesiyle etkileşime girebilir. İki drone aynı tik sırasında aynı kareyle etkileşime girerse, her iki etkileşim de gerçekleşir, ancak sonuçlar etkileşimlerin sırasına göre farklılık gösterebilir.

Örneğin, `0` ve `1` numaralı drone'ların neredeyse tamamen büyümüş aynı ağacın üzerinde olduğunu hayal edin.
Drone `0` şunu çağırır:
`use_item(Items.Fertilizer)`
Drone `1` şunu çağırır:
`harvest()`

Bu eylemler aynı anda gerçekleşirse, ağaç önce gübrelenecek ve sonra hasat edilecektir. Bu durumda, ondan odun alacaksınız. Ancak, Drone `1` biraz daha hızlıysa, ağaç gübrelenmeden önce hasat edilecek ve odun alamayacaksınız.
Buna "yarış durumu" denir. Sonucun işlemlerin gerçekleştirilme sırasına bağlı olduğu paralel programlamada yaygın bir sorundur.

Birden fazla drone aynı kodu aynı anda aynı konumda çalıştırdığında olabilecek başka bir sorunlu durum daha aşağıdadır.
`if get_water() < 0.5:
    use_item(Items.Water)`

Birden fazla drone bunu aynı anda çalıştırırsa, hepsi ilk satırı çalıştıracak ve bu da onları `if` bloğuna sokacaktır. Sonra hepsi su kullanacak ve çok fazla su israf edecektir.
Bir drone ikinci satıra ulaştığında, `get_water()` artık `0.5`'ten küçük olmayabilir çünkü başka bir drone bu arada kareyi sulamıştır.