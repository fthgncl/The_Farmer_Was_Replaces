# Yedekleri Yükleme
Ne yazık ki, bazen bir kayıt dosyası bozulabilir veya bazı kod dosyalarını kaybedebilirsiniz. Bu başınıza gelirse, bir yedeği yüklemeyi deneyebilirsiniz. Eğer bu düzenli olarak oluyorsa, Steam Cloud özelliğini kapatmayı deneyin.

Oyun her kaydedildiğinde bir yedek oluşturulur ve bir şeyi geri yüklemeniz gerekmesi ihtimaline karşı az sayıda yedek saklanır.
Bu yedekler [yedekleme dizininde](persistent_data_path/Backup) bulunabilir. Bunlar [kayıt dizinindeki](persistent_data_path/Saves) kayıtların kopyalarıdır.
Bir yedeği yüklemenin en kolay yolu, yüklemek istediğiniz belirli yedeğin klasörünü kayıt dizinine kopyalamaktır.

Bir kayıt, içinde `save.json` dosyası ve bir dizi `.py` dosyası bulunan bir klasördür.
Sadece birkaç kod dosyasını kaybettiyseniz veya kod dosyaları hala oradaysa ancak `save.json` dosyası bozuksa, sadece bozuk kısımları yedekteki ilgili dosyalarla değiştirebilirsiniz.