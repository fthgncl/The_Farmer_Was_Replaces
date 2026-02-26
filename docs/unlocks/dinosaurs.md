# Dinozorlar
Dinozorlar, antik kemikler için yetiştirilebilen (farmed) eski, görkemli yaratıklardır.

Ne yazık ki dinozorların soyu uzun zaman önce tükendi, bu yüzden şimdi yapabileceğimiz en iyi şey onlar gibi giyinmek.
Bu amaçla yeni dinozor şapkasını aldınız.

Şapka şu şekilde takılabilir:
`change_hat(Hats.Dinosaur_Hat)`

Maalesef reklamdaki gibi görünmüyor...

Dinozor şapkasını takarsanız ve yeterli kaktüsünüz varsa, otomatik olarak bir [elma](objects/apple) satın alınacak ve drone'un altına yerleştirilecektir.
Drone bir elmanın üzerindeyken tekrar hareket ederse, elmayı yiyecek ve kuyruğunu bir büyütecektir. Eğer paranız yetiyorsa, yeni bir elma satın alınacak ve rastgele bir konuma yerleştirilecektir.
Elma, olmak istediği yerde başka bir şey ekiliyse ortaya çıkamaz (spawn olamaz).

Dinozorun kuyruğu drone'un arkasından sürüklenecek ve drone'un daha önce üzerinden geçtiği kareleri dolduracaktır. Bir drone kuyruğun üzerine hareket etmeye çalışırsa `move()` başarısız olacak ve `False` döndürecektir.
Kuyruğun son parçası hareket sırasında yoldan çekilir, böylece üzerine hareket edebilirsiniz. Ancak, yılan tüm çiftliği doldurursa, artık hareket edemezsiniz. Yani artık hareket edemeyip edemediğinizi kontrol ederek yılanın tamamen büyüyüp büyümediğini anlayabilirsiniz.

Bir elma üzerinde `measure()` kullanmak, bir sonraki elmanın konumunu bir demet (tuple) olarak döndürecektir.

`next_x, next_y = measure()`

Farklı bir şapka takılarak şapka tekrar çıkarıldığında kuyruk hasat edilecektir.
Kuyruk uzunluğunun karesi kadar kemik alacaksınız. Yani `n` uzunluğundaki bir kuyruk için `n**2` adet `Items.Bone` alırsınız.
Örneğin:
uzunluk 1 => 1 kemik
uzunluk 2 => 4 kemik
uzunluk 3 => 9 kemik
uzunluk 4 => 16 kemik
uzunluk 16 => 256 kemik
uzunluk 100 => 10000 kemik

Dinozor Şapkası çok ağırdır, bu yüzden takarsanız `move()` işleminin 200 tik yerine 400 tik sürmesine neden olur. Ancak, her elma topladığınızda, `move()` tarafından kullanılan tik sayısı %3 (aşağı yuvarlanmış) azalır, çünkü daha uzun bir kuyruk hareket etmenize yardımcı olabilir.

Aşağıdaki döngü, herhangi bir sayıda elmadan sonra `move()` tarafından kullanılan tik sayısını yazdırır:

`ticks = 400
for i in range(100):
    print(i, " elmadan sonraki tikler: ", ticks)
    ticks -= ticks * 0.03 // 1`

Sadece bir dinozor şapkanız var, bu yüzden sadece bir drone onu takabilir.

<spoiler=1. ipucunu göster>Tüm alanı kapsayan aynı yol boyunca hareket etmeye devam ederseniz, her seferinde tüm alanı kapsayan bir yılan elde edebilirsiniz. Çok verimli değildir ama işe yarar.
Çok büyük bir çiftliği tamamen dolaşmak uzun zaman alabilir ve aslında o kadar çok kemiğe ihtiyacınız olmayabilir. Çiftliğin boyutunu daha uygun bir şeye değiştirmek için `set_world_size()` kullanmaktan çekinmeyin.</spoiler>