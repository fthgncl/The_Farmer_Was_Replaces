# Labirentler (Mazes)
Bitkileri [gübreleyerek](docs/unlocks/fertilizer.md) elde edilen `Items.Weird_Substance` (Tuhaf Madde), çalılar üzerinde garip bir etkiye sahiptir. Drone bir çalının üzerindeyse ve `use_item(Items.Weird_Substance, amount)` çağrısı yaparsanız, çalı çitlerden oluşan bir labirente dönüşecektir.
Labirentin boyutu kullanılan `Items.Weird_Substance` miktarına bağlıdır (`use_item()` çağrısının ikinci argümanı).
Labirent yükseltmeleri olmadan, `n` adet `Items.Weird_Substance` kullanmak `n`x`n` boyutunda bir labirentle sonuçlanacaktır. Her labirent yükseltme seviyesi hazineyi ikiye katlar, ancak aynı zamanda gereken `Items.Weird_Substance` miktarını da ikiye katlar.

Yani tam bir alan labirenti yapmak için:

`plant(Entities.Bush)
substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)`

Bazı nedenlerden dolayı drone, çok yüksek görünmeseler de çitlerin üzerinden uçamaz.

Çitin içinde bir yerde saklı bir hazine vardır. Hazine üzerinde `harvest()` kullanmak, labirentin alanına eşit miktarda altın verir. (Örneğin, 5x5'lik bir labirent 25 altın verecektir.)

Başka bir yerde `harvest()` kullanırsanız labirent basitçe kaybolacaktır.

Drone hazinenin üzerindeyse `get_entity_type()` `Entities.Treasure`'a, labirentin diğer her yerinde ise `Entities.Hedge`'e (Çit) eşittir.

Labirenti yeniden kullanmadığınız sürece labirentlerde herhangi bir döngü bulunmaz (bir labirentin nasıl yeniden kullanılacağı aşağıya bakın). Bu nedenle, drone'un geri gitmeden tekrar aynı konuma gelmesinin bir yolu yoktur.

İçinden geçmeye çalışarak bir duvar olup olmadığını kontrol edebilirsiniz.
`move()`, başarılı olursa `True`, aksi takdirde `False` döndürür.

`can_move()`, hareket etmeden bir duvar olup olmadığını kontrol etmek için kullanılabilir.

Hazineye nasıl ulaşacağınız konusunda hiçbir fikriniz yoksa, 1. İpucu'na bakın. Bunun gibi bir soruna nasıl yaklaşacağınızı gösterir.

Labirentin herhangi bir yerinde `measure()` kullanmak hazinenin konumunu döndürür.
`x, y = measure()`

Ekstra bir zorluk için, hazine üzerinde tekrar aynı miktarda `Items.Weird_Substance` kullanarak labirenti yeniden kullanabilirsiniz.
Bu, hazinedeki altın miktarını tam bir labirent kadar artıracak ve onu labirentte rastgele bir konuma taşıyacaktır.

Hazine her taşındığında, labirentin duvarlarından bazıları rastgele kaldırılabilir. Böylece yeniden kullanılan labirentler döngüler içerebilir.

Labirentteki döngülerin işi çok daha zorlaştırdığını unutmayın, çünkü bu geri gitmeden tekrar aynı yere gelebileceğiniz anlamına gelir.
Bir labirenti yeniden kullanmak, sadece hasat edip yeni bir labirent oluşturmaktan daha fazla altın vermez.
Bu %100 ekstra bir zorluktur ve isterseniz atlayabilirsiniz.
Sadece ekstra bilgi ve kısayollar labirenti daha hızlı çözmenize yardımcı olursa buna değer.

Hazine 300 defaya kadar yeniden konumlandırılabilir. Bundan sonra, hazine üzerinde tuhaf madde kullanmak artık içindeki altını artırmayacak ve artık hareket etmeyecektir.

<spoiler=1. ipucunu göster>İşte sorunu çözmek için genel bir yaklaşım:

Bir labirent oluşturun ve drone olduğunuzu hayal edin.

Labirentin içinde olsaydınız hazineyi nasıl bulmaya çalışacağınızı düşünün.

Stratejinizi adım adım yazın, böylece bir başkası düşünmeden takip edebilir.

Şimdi adımlarınızı koda çevirmeyi deneyin.
</spoiler>
<spoiler=2. ipucunu göster>Döngü olmadığı sürece: Tüm duvarlar aslında sadece büyük bir bağlantılı duvardır. Duvarı takip ederseniz, sizi tüm labirent boyunca götürecektir.
Bu yaklaşım çok az kod gerektirir ve nerede olduğunuzu takip etmeniz gerekmez. İhtiyacınız olan tek şey yaklaşık 10 satır koddur.</spoiler>
<spoiler=3. ipucunu göster>Drone'u doğu veya batı gibi mutlak yönlerde hareket ettirmek yerine, "sağa dön" veya "sola dön" gibi göreceli yönlerde hareket ettirmek çok yararlı olabilir. Bunu yapmak için drone'un şu anda hangi yöne hareket ettiğini takip etmeniz gerekir. Drone aslında asla dönmez, ancak yine de kodda "sanal" bir dönüş tutabilirsiniz.
Aşağıdaki indeks (dizin) hilesi bunun için yararlıdır:

`directions = [North, East, South, West]
index = 0`

"Daire etrafında" dönmesine izin vermek için `% 4` kullanın, böylece `West` (Batı)'dan sonra `North` (Kuzey)'a geri döner.
`# sağa dön
index = (index + 1) % 4`

`# sola dön
index = (index - 1) % 4

move(directions[index])`</spoiler>
<spoiler=4. ipucunu göster>Eğer çözemezseniz, her zaman hayatınızı kolaylaştırabilir ve daha az verimli bir şekilde yapabilirsiniz.
`1`x`1` labirenti çözmek çok basittir.</spoiler>