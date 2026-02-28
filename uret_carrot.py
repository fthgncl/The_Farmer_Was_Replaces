from hareket import her_yerde_uygula
from bitki_ekim import plant_smart, harvest_combination

def uret_carrot():
	her_yerde_uygula(carrot_ek)
	
def carrot_ek():
	harvest_combination(Entities.Carrot)
	plant_smart(Entities.Carrot)
	