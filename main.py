from kilit_agaci import hasat_hedefini_bul
from uretim import uretim_surecini_baslat

test_item = None

while True:
	
	if test_item != None:
		uretim_surecini_baslat(test_item,num_items(test_item)+999999)
		return
		
	
	hasat_hedefi = hasat_hedefini_bul()
	if hasat_hedefi:
		hedef_urun = hasat_hedefi["item"]
		hedef_adet = hasat_hedefi["hedef"]
		uretim_surecini_baslat(hedef_urun,hedef_adet)
		
