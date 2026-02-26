# 1.0 Sonunda Burada!
Geliştirmeyle geçen 3,5 yıldan, 20'den fazla güncellemeden ve sizlerin harika geri bildirimlerinden sonra, Erken Erişim nihayet sona erdi.

## 1.0'da neler yeni?
- Çiftçiliğinizi en üst düzeye çıkarmak için birden fazla drone
- Daha üstel bir ilerlemeye sahip yeniden işlenmiş bir kilit açma ağacı
- Becerilerinizi test etmek için 60 başarı
- Belirli başarıların kilidini açmak drone'unuza özel şapkalar verecektir
- Tam bir ses revizyonu
- Bir yeni müzik parçası
- Yaşam kalitesi iyileştirmeleri ve çeşitli düzeltmeler
- Kırıcı Değişiklikler: Yükseltmeler kısmen sıfırlanacak. Labirentleri yeniden kullanmak biraz farklı çalışıyor.

Erken Erişim'den tam sürüme kadar The Farmer Was Replaced'i desteklediğiniz için hepinize çok teşekkür ederim.
Çoklu drone'ları yaratıcı ve zekice yollarla nasıl kullandığınızı görmek için sabırsızlanıyorum!
-Timon

Ayrıca Discord'da bize katılmayı unutmayın:
[Discord](https://discord.com/invite/kj33cJkeJn)

## Tam Yama Notları
Kırıcı Değişiklikler:
-Teknoloji ağacının yeniden işlenmesi nedeniyle, eski kayıt dosyalarındaki yükseltme sayıları artık geçerli olmayacak. Eski bir kaydı açtığınızda oyun tüm yükseltmeleri makul bir seviyeye sıfırlayacak.
-Labirentleri yeniden kullanıyorsanız, artık önce ölçüp sonra yeniden konumlandırmak yerine önce hazineyi yeniden konumlandırmalı ve sonra konumunu ölçmelisiniz.

Oynanış:
-Çiftlikteki karelerin üzerine gelindiğinde yararlı bilgiler içeren ipuçları eklendi.
-Labirentin herhangi bir yerinde `measure()` kullanmak artık her zaman mevcut hazinenin konumunu döndürüyor. Artık özellikle hazineyi ölçmeniz gerekmiyor.
-Labirent için artık bir `can_move()` fonksiyonu var.
-Balkabakları artık 5x5 yerine 6x6'ya kadar büyüyor.
-Zemin kuruma davranışı biraz değişti. Her 0,8 ila 1,2 saniyede %1 kuruması yerine, her zemin karesinin artık her 0,1 saniyede %10 kuruma şansı var.
-Kaktüs büyüme süresi artık her zaman tam olarak 1 saniyedir.
-Balkabakları artık öldüklerini belirtmek için arkalarında ölü bir balkabağı bırakıyorlar.
-`pet_the_piggy()` eklendi.
-`num_unlocked()` artık Duyular (Senses) ile birlikte açılıyor.

Ses:
-Ses tamamen yeniden yapıldı.
-Artık oyuna başladığınızda müzik var!

Görseller:
-Teknoloji ağacının görselleri tamamen yeniden işlendi.
-Ekranın sol üst köşesindeki envanter paneli artık güzel bir eşya alma görsel efektine sahip.
-Kaktüsler artık doğru şekilde sıralanmadıklarında daha görünür olması için kahverengi oluyor.
-Bitkiler artık henüz büyümemiş olsalar bile ekildikten hemen sonra görünür oluyorlar.

Kod Editörü:
-Alt çizgi içeren tanımlayıcılara çift tıklamak artık tüm tanımlayıcıyı seçiyor.
-"Sekmeleri boşluklara dönüştür" seçeneği kapalıysa, girinti boşlukları artık sekmelere dönüştürülüyor.
-Yakınlaştırma (Zoom) artık çok daha pürüzsüz.
-Kod tamamlayıcı artık içe aktarma (import) konusunda düzgün bir şekilde farkındalık sahibi ve diğer dosyalardan önerilerde bulunabiliyor.
-Metin düzenleme ve pencereleri yeniden boyutlandırma için farklı imleçler eklendi.
-Hata ayıklayıcı (Debugger) adımları artık simülasyon tikleri yerine kod satırına dayanıyor.

Diğer:
-Artık Python'daki gibi karşılaştırma operatörlerini zincirleyebilirsiniz.
-`get_cost(Entities.Hedge)` ve `get_cost(Entities.Treasure)` artık 1x1'lik bir labirentin maliyetini döndürüyor.
-Bir çözünürlük ayarı eklendi.
-Kod çalışırken yanıp sönen vurguları kapatmak için bir ayar eklendi.
-Kod yürütme daha da optimize edildi, böylece kod çalışırken oyunun daha akıcı çalışması sağlandı.
-Bir "HUD'u Aç/Kapat" tuş ataması eklendi.

Düzeltmeler:
-Kod vurgularının diğer pencerelerden görünmesine neden olan en yaygın durumlardan bazıları düzeltildi.
-Toprak sürme gibi eylemler artık su kuruma davranışını etkileyemez.
-ABD dışı klavyelerdeki tuş atama sorunları düzeltildi.
-Kumbaranın bazen çiftlikten çok uzağa gitmesi düzeltildi.
-Gübrelerin tam büyümüş bitkilere hastalık bulaştırmaması düzeltildi.
-`set_world_size(get_world_size())`'nin drone konumunu sıfırlaması düzeltildi.
-Çok sayıda elmanın geride kalmasına neden olan bir simülasyon + dinozor etkileşimi düzeltildi.
-Küçültmeye tıklayıp menüyü açtığınızda hata mesajlarının etrafta dolaşmasına neden olan hata düzeltildi.
-Hala yazarken hata mesajlarının açılması düzeltildi.

Kaçırmış olabileceğiniz eski Yamalardan Kırıcı Değişiklikler:
-Diğer dosyalarda (oyundaki pencereler) tanımlanan fonksiyonlar artık örtük olarak içe aktarılmıyor. Artık Python'daki gibi açık içe aktarma ifadelerinin kilidini açmanız ve kullanmanız gerekiyor (İçe aktarma (import) kilidine bakın).
-`Items.Bones`, `Items.Bone` olarak yeniden adlandırıldı, böylece tüm eşyalar tekil oldu.
-`Entities.Carrots`, `Entities.Carrot` olarak yeniden adlandırıldı, böylece tüm varlıklar tekil oldu.
-`Grounds.Turf`, anlaşılmasını kolaylaştırmak için `Grounds.Grassland` olarak yeniden adlandırıldı.
-`Items.Water_Tank`, tank doldurma özelliği kaldırıldığı için `Items.Water` olarak yeniden adlandırıldı.
-`Unlocks.Benchmark`, `Unlocks.Timing` ile değiştirildi.
-`get_op_count()`, `get_tick_count()` olarak yeniden adlandırıldı.
-`set_farm_size()`, `get_world_size()` ile tutarlı olması için `set_world_size()` olarak yeniden adlandırıldı.
-`get_companion()` artık bir liste yerine (entity, (x, y)) biçiminde bir demet (tuple) döndürüyor.
-`trade()` oyundan kaldırıldı.