# Liderlik Tablosu
Buraya kadar geldiyseniz, birçok zorluğun üstesinden gelmişsiniz demektir. Ama bunları verimli bir şekilde çözdünüz mü?
En verimli çiftçilik yöntemleri için çeşitli liderlik tablolarında diğer oyuncularla rekabet edebilirsiniz.

`leaderboard_run(leaderboard, filename, speedup)` çağrısı yaparak bir liderlik tablosu koşusu başlatabilirsiniz.
Bu, başlangıç koşullarının sabit olması dışında `simulate()` benzeri bir [simülasyon](docs/unlocks/simulation.md) başlatır. Her liderlik tablosu kategorisinin farklı başlangıç ve başarı koşulları vardır.

Simülasyon sona erdiğinde başarı koşulu `True` ise liderlik tablosu koşusu başarılı olur.

Simülasyon hedefe ulaşıldığında otomatik olarak SONA ERMEZ. Programın sonlandığından emin olmalısınız.
Koşu başarılı olursa, süreniz liderlik tablosuna eklenecektir.

Varyansı azaltmak için tüm koşuların en az 2 saat sürmesi gerekir (Hızlandırabilirsiniz, böylece o kadar uzun sürmez). Bir koşu daha erken tamamlanırsa, toplam 2 saatlik süreye ulaşılana kadar tekrarlanır. Daha sonra tüm koşuların ortalaması puanınız olarak yüklenir.

İşte sizi saman liderlik tablosuna sokacak örnek bir kurulum.
![](LeaderboardSetup400)

## Fastest Reset (En Hızlı Sıfırlama)
En hızlı sıfırlama en prestijli kategoridir. Oyunu tek bir çiftlik alanından liderlik tablolarının kilidini tekrar açmaya kadar tamamen otomatikleştirin.

Her şeyin kilidini açmak zorunda değilsiniz, sadece `Unlocks.Leaderboard` kilidini olabildiğince hızlı açmaya çalışın.

Bir şeyin kilidinin açık olup olmadığını kontrol etmek için `num_unlocked(unlock) > 0` kullanabileceğinizi ve doğru eşyaları otomatik olarak toplamak (farm) için ne kadara mal olduklarını görmek üzere kilitler üzerinde `get_cost()` kullanabileceğinizi unutmayın.

Fonksiyon Çağrısı:
`leaderboard_run(Leaderboards.Fastest_Reset, filename, speedup)`

Eşdeğer Simülasyon:
`unlocks = {}
items = {}
globals = {}
#negatif bir tohum (seed) değeri rastgele bir tohum anlamına gelir
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Başarı Koşulu:
`num_unlocked(Unlocks.Leaderboard) > 0`

## Maze (Labirent)
Her şeyin kilidi açık olarak başlayın ve olabildiğince hızlı bir şekilde `9863168` altın toplayın. Bu, bir 32x32 labirenti `300` kez yeniden kullanarak kazanacağınız altın miktarıdır.

Fonksiyon Çağrısı:
`leaderboard_run(Leaderboards.Maze, filename, speedup)`

Eşdeğer Simülasyon:
`unlocks = Unlocks
items = {Items.Weird_Substance : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Başarı Koşulu:
`num_items(Items.Gold) >= 9863168`

## Dinosaur (Dinozor)
Her şeyin kilidi açık olarak başlayın ve olabildiğince hızlı bir şekilde `33488928` kemik toplayın. Bu, 32x32'lik bir alanı dinozor kuyruğuyla doldurursanız elde edeceğiniz kemik miktarıdır.

Fonksiyon Çağrısı:
`leaderboard_run(Leaderboards.Dinosaur, filename, speedup)`

Eşdeğer Simülasyon:
`unlocks = Unlocks
items = {Items.Cactus : 1000000000, Items.Power: 1000000000}
globals = {}
seed = -1
simulate(filename, unlocks, items, globals, seed, speedup)`

Başarı Koşulu:
`num_items(Items.Bone) >= 33488928`

## Diğer Kaynak Liderlik Tabloları
Her bitkinin, o bitkiyi mümkün olduğunca çabuk toplamak için kendi liderlik tablosu vardır. Tüm kilitler açık, bitkiyi yetiştirmek için ihtiyacınız olan kaynaklar ve bol miktarda güç ile başlarsınız. Amaç, bitki tarafından üretilen belirli miktarda kaynağı toplamaktır.

Her zaman olduğu gibi, hedefe ulaştığınızda programınızın sonlandığından emin olmalısınız. Hedefe ulaşılsa bile program bitene kadar bir koşu tamamlanmış sayılmaz.

### `Leaderboards.Cactus`
`leaderboard_run(Leaderboards.Cactus, filename, speedup)`
Başarı Koşulu: `num_items(Items.Cactus) >= 33554432`

### `Leaderboards.Sunflowers`
`leaderboard_run(Leaderboards.Sunflowers, filename, speedup)`
Başarı Koşulu: `num_items(Items.Power) >= 100000`

### `Leaderboards.Pumpkins`
`leaderboard_run(Leaderboards.Pumpkins, filename, speedup)`
Başarı Koşulu: `num_items(Items.Pumpkin) >= 200000000`

### `Leaderboards.Wood`
`leaderboard_run(Leaderboards.Wood, filename, speedup)`
Başarı Koşulu: `num_items(Items.Wood) >= 10000000000`

### `Leaderboards.Carrots`
`leaderboard_run(Leaderboards.Carrots, filename, speedup)`
Başarı Koşulu: `num_items(Items.Carrot) >= 2000000000`

### `Leaderboards.Hay`
`leaderboard_run(Leaderboards.Hay, filename, speedup)`
Başarı Koşulu: `num_items(Items.Hay) >= 2000000000`

## Tek Drone Liderlik Tabloları
Tek bir drone ile çiftçilik yapmak için Liderlik Tabloları da vardır. Sadece bir drone ve 8x8 bir çiftlik alırsınız ve belirli miktarda kaynağı olabildiğince hızlı toplamanız gerekir.

### `Leaderboards.Maze_Single`
`leaderboard_run(Leaderboards.Maze_Single, filename, speedup)`
Başarı Koşulu: `num_items(Items.Gold) >= 616448`

### `Leaderboards.Cactus_Single`
`leaderboard_run(Leaderboards.Cactus_Single, filename, speedup)`
Başarı Koşulu: `num_items(Items.Cactus) >= 131072`

### `Leaderboards.Sunflowers_Single`
`leaderboard_run(Leaderboards.Sunflowers_Single, filename, speedup)`
Başarı Koşulu: `num_items(Items.Power) >= 10000`

### `Leaderboards.Pumpkins_Single`
`leaderboard_run(Leaderboards.Pumpkins_Single, filename, speedup)`
Başarı Koşulu: `num_items(Items.Pumpkin) >= 10000000`

### `Leaderboards.Wood_Single`
`leaderboard_run(Leaderboards.Wood_Single, filename, speedup)`
Başarı Koşulu: `num_items(Items.Wood) >= 500000000`

### `Leaderboards.Carrots_Single`
`leaderboard_run(Leaderboards.Carrots_Single, filename, speedup)`
Başarı Koşulu: `num_items(Items.Carrot) >= 100000000`

### `Leaderboards.Hay_Single`
`leaderboard_run(Leaderboards.Hay_Single, filename, speedup)`
Başarı Koşulu: `num_items(Items.Hay) >= 100000000`