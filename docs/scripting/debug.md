# Hata Ayıklama (Debug)
Bazen kodunuz çalışmaz ve nedenini bulmanız gerekir. Bunu yapmanıza yardımcı olacak birkaç araç vardır.

Birincisi programı adım adım çalıştırmaktır.
Çalıştır düğmesinin yanındaki düğmeyle veya bir kesme noktası (breakpoint) belirleyerek adım adım moda geçebilirsiniz.

Kesme noktaları, kodun solundaki kesme noktası paneline tıklayarak eklenebilir.
![](Breakpoints227)
Yürütme, kesme noktasının bulunduğu satıra ulaştığında otomatik olarak adım adım moda geçer.

Farenizi bir değişkenin üzerine getirdiğinizde, mevcut değeri görüntülenir.

`print()` fonksiyonu da çok yararlı olabilir. Kendisine geçirilen herhangi bir değeri doğrudan havaya yazar.

Örnekler:

"0.24" yazdır.
`print(0.24)`

"True" veya "False" yazdır.
`print(can_harvest())`

Mevcut konumu yazdır.
`print(get_pos_x(), get_pos_y())`

Print fonksiyonu değeri doğrudan havaya ve [Çıktı (Output)](docs/output.md) sayfasına yazdırır.

Çok fazla değer yazdırmak istiyorsanız havaya yazmak bazen biraz yavaş olabilir.
Bu durumda, yalnızca çıktı penceresine yazdıran `quick_print()` fonksiyonunu kullanabilirsiniz.

Çıktı penceresi ayrıca uyarıları ve hataları da günlükler, bu nedenle bir şeyler beklendiği gibi çalışmazsa bunu kontrol etmek yararlı olabilir.

Yürütme durduğunda, çıktı oyun klasöründeki output.txt dosyasına da yazılır. [output.txt](persistent_data_path/output.txt).