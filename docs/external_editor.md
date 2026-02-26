# Harici Kod Düzenleyici
Oyun içi metin düzenleyici genellikle bu oyunu oynamak için yeterlidir, ancak elbette Visual Studio Code gibi daha gelişmiş metin düzenleyicileriyle rekabet edemez.

Oyun tüm kod dosyalarını .py dosyaları olarak kaydeder, böylece bunları Python düzenleyicileriyle düzenleyebilirsiniz.
Bunun sadece kolaylık sağlamak için olduğunu unutmayın. Oyun içi dil aslında Python değildir, ancak Python IntelliSense'in üzerinde düzgün çalışabileceği kadar yakındır.
Dosyaları [kayıt klasöründe](persistent_data_path/Saves) bulabilirsiniz.

Her kayıt ayrıca, IntelliSense'i etkinleştirmek için oyun içi yerleşiklerle eşleşen yerleşik Python tanımlarını içeren bir `__builtins__.py` dosyası içerir.
VS Code, `__builtins__.py` dosyasını otomatik olarak algılayabilir, ancak bazı düzenleyiciler yalnızca `from __builtins__ import *` yaparsanız çalışabilir.

Harici değişiklikleri oyunda kaydı yeniden yüklemeden görmek için "Dosya İzleyici" (File Watcher) seçeneğini etkinleştirmelisiniz. Harici olarak dosya oluşturur veya silerseniz, bunları görmek için yine de kaydı yeniden yüklemeniz gerekir.

## VS Code Kullanımı
Visual Studio Code, The Farmer Was Replaced ile kullanılması önerilen kod düzenleyicisidir.

[Buradan](https://code.visualstudio.com/download) yükleyebilirsiniz.

İndirdikten sonra, VS Code'a Python uzantısını yükleyin.

Buna sahip olduğunuzda, VS Code'da `.py` dosyalarınızı içeren [klasörü](persistent_data_path/Saves) açın. Bireysel dosyaları değil tüm klasörü açtığınızdan emin olun, aksi takdirde `__builtins__.py` dosyası çalışmaz.

Oyunda, "Dosya İzleyici" seçeneğinin açık olduğundan emin olun. Artık VS Code'da her kaydettiğinizde, değişiklikler otomatik olarak oyunda görünecektir.

İşte bu kadar! Artık kodunuzu profesyonel bir kod düzenleyicide yazabilirsiniz!