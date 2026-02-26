# Gübre
Bir noktada, bitkilerin büyümesini beklemek artık yeterince verimli değildir.
Suya benzer şekilde, her 10 saniyede bir otomatik olarak 1 gübre alacaksınız, bu miktar her yükseltmede iki katına çıkacaktır.

Gübre bitkilerin anında büyümesini sağlayabilir. `use_item(Items.Fertilizer)`, drone'un altındaki bitkinin kalan büyüme süresini 2 saniye azaltır.

Bunun bazı yan etkileri vardır.
Gübre ile yetiştirilen bitkiler enfekte (hasta) olacaktır.

bir bitki enfekte olduğunda, hasat edildiğinde veriminin yarısı `Items.Weird_Substance`'a (Tuhaf Madde) dönüşür.
Tuhaf Madde bitkiler üzerinde de kullanılabilir, bu da bitkinin ve tüm komşu bitkilerin enfeksiyon durumunu değiştirme etkisine sahiptir.

Yani enfekte olmuş bir bitki üzerinde `use_item(Items.Weird_Substance)` kullanırsanız iyileşir, ancak sağlıklı bir bitki üzerinde kullanırsanız enfekte olur.

eğer sağlıklı komşuları olan enfekte bir bitki üzerinde kullanırsanız, hedef bitkiyi iyileştirir ancak komşularını enfekte eder ve bunun tersi de geçerlidir.