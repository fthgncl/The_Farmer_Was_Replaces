# Maliyetler
Herhangi bir maliyet, öğeleri sayılarla eşleştiren bir sözlük olarak temsil edilebilir.

`get_cost()` fonksiyonu böyle bir sözlük döndürür. Bir bitkinin veya kilidin maliyetini döndürür.

`get_cost(Entities.Pumpkin)`
`{Items.Carrot:1}` döndürür

Kilitler (Unlocks) için, maliyetini almak istediğiniz kilit seviyesi için isteğe bağlı ikinci bir argüman geçirilebilir. Varsayılan olarak, mevcut kilit seviyesidir.

`get_cost(Unlocks.Loops, 0)`
`{Items.Hay:5}` döndürür

Zaten maksimum seviyede olan kilitler için `get_cost()` `None` döndürür.

Şu şekilde kullanılabilir:
`cost = get_cost(something)
for item in cost:
	amount_of_this_item_needed = cost[item]`
