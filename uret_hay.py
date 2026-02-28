from hareket import her_yerde_uygula
from bitki_ekim import plant_smart, harvest_combination

def uret_hay():
	her_yerde_uygula(grass_ek)
	
def grass_ek():
	harvest_combination(Entities.Grass)
	plant_smart(Entities.Grass, False)
	