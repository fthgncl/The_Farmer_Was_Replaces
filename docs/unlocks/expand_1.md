# Genişlet 1
<unlock=for>Ayrıca bakınız [Genişlet 2](docs/unlocks/expand_2.md)

</unlock>Çiftliğiniz büyüdü! Drone'u hareket ettiremezseniz bu alanın pek bir yararı olmaz, bu yüzden drone'u hareket ettiren yeni bir `move()` fonksiyonu var. `move()`, drone'un hareket etmesini istediğiniz yönü belirtmenizi gerektirir. Bunun için dört yeni sabit vardır: `North` (Kuzey), `East` (Doğu), `South` (Güney), `West` (Batı).

Örneğin, `move(North)` drone'u kuzeye doğru bir kare hareket ettirecektir.

Çiftliğin kenarından öteye hareket ederseniz, drone çiftliğin diğer tarafına taşınacaktır.
Aşağıdaki örnek kod, drone'u kuzeye doğru hareket ettirmeye devam edecek ve çiftliğin kenarına ulaştığında başa dönecektir:

`while True:
	move(North)`
