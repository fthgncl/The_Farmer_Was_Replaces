from companion import companion_process
from zemin import zemini_uygun_hale_getir

def plant_smart(entity, _sula = True):
	
	if get_entity_type() == entity:
		return
	
	harvest()
	zemini_uygun_hale_getir(entity)
	plant(entity)
	if _sula:
		sula()
	
def harvest_combination(entity = None):
	companion_process(entity)
	harvest()
	
def sula():
	while get_water() <= 0.5:
			use_item(Items.Water)

def yeterli_malzeme_var_mi(entity):
	# Bütün araziyi yalnızca o ürün
	# ile ekebilecek malzeme var mı
	# sorgular. İhtiyaç adetini döndürür
	
	ihtiyaclar = get_cost(entity)
	for item in ihtiyaclar: 
		ihtiyac_adeti = ihtiyaclar[item]
		tum_arazinin_ihtiyaci = ihtiyac_adeti * get_world_size() * get_world_size()
		mevcut_adet = num_items(item)
		if tum_arazinin_ihtiyaci > mevcut_adet:
			eksik_adet = tum_arazinin_ihtiyaci - mevcut_adet
			return (False, item, eksik_adet)
			
	return (True, None, None)
