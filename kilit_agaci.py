def acilabilecek_kilidi_bul():
	kilit_maliyet_listesi = kilit_maliyetlerini_al()
	for kilit_ve_maliyeti in kilit_maliyet_listesi:
		kilit = kilit_ve_maliyeti["unlock"]
		maliyetler = kilit_ve_maliyeti["cost"]
		if kilit_maliyeti_karsilanabilir_mi(maliyetler):
			return kilit
			
	return None
		
def kilit_maliyeti_karsilanabilir_mi(maliyetler):
	for item in maliyetler:
		if num_items(item) < maliyetler[item]: return False
		
	return True

def kilit_maliyetlerini_al():
	kilit_maliyet_listesi = []
		
	for kilit in Unlocks:
		maliyet = get_cost(kilit)
		
		if len(maliyet) > 0:
			kilit_maliyet_listesi.append({
				"unlock": kilit,
				"cost": maliyet 
			})
			
	return kilit_maliyet_listesi


def oncelik_sirasi_itemler():
	sirali_itemler = []
	
	for item in Items:
		sirali_itemler.append(item)
		
	return sirali_itemler
	
def oncelikli_kilidi_bul():
	
	acilabilecek_kilit = acilabilecek_kilidi_bul()
	if acilabilecek_kilit:
		return acilabilecek_kilit
	
	
	kilit_maliyet_listesi = kilit_maliyetlerini_al()
	for kilit_ve_maliyeti in kilit_maliyet_listesi:
		kilit = kilit_ve_maliyeti["unlock"]
		return kilit
		
	return None
	
def hasat_hedefini_bul():
	kilit = oncelikli_kilidi_bul()
	if not kilit:
		return None
	
	gerekliItemler = get_cost(kilit)
	
	for item in gerekliItemler:
		ihtiyac_adeti = gerekliItemler[item]
		mevcut_adet = num_items(item)
		if ihtiyac_adeti > mevcut_adet:
			return {"item":item, "hedef": ihtiyac_adeti}
	
	for i in range(5):
		print("[",kilit,"] Kilit açılıyor")
		do_a_flip()
		do_a_flip()
	
	unlock(kilit)


	