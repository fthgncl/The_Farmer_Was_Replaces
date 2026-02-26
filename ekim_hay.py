from hareket import her_yerde_uygula
from game_registry import GLOBAL_OBJECTS
from bitki_ekim import plant_smart, harvest_combination

def hay_uret(hay):
	if not GLOBAL_OBJECTS["hedef_uretim"] == Entities.Grass:
		GLOBAL_OBJECTS["hedef_uretim"] = Entities.Grass
	
	else:
		her_yerde_uygula(grass_ek)
	
def grass_ek():
	harvest_combination(Entities.Grass)
	plant_smart(Entities.Grass)
	