from hareket import her_yerde_uygula
from bitki_ekim import plant_smart, harvest_combination

def uret_power():
	her_yerde_uygula(agac_ve_cimleri_ek)
	
def agac_ve_cimleri_ek():
	
	ekilecek_bitki = cali_mi_agac_mi_bul()
	
	if ( ekilecek_bitki == Entities.Tree ):
		harvest_combination(ekilecek_bitki)
	else:
		if can_harvest():
			harvest()
			
	plant_smart(ekilecek_bitki, False)