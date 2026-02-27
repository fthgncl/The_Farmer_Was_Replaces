from hareket import her_yerde_uygula, git
from game_registry import GLOBAL_OBJECTS
from zemin import zemini_uygun_hale_getir
from bitki_ekim import plant_smart

def pumpkin_uret(pumpkin):
	if not GLOBAL_OBJECTS["hedef_uretim"] == Entities.Pumpkin:
		GLOBAL_OBJECTS["hedef_uretim"] = Entities.Pumpkin
	
	else:
		pumpkin_ek()
	
def pumpkin_ek():
	olmamis_kabaklar = []
	ilk_kabak_id = [None]
	her_yerde_uygula(big_pumpkin_kontrol, True , [olmamis_kabaklar, ilk_kabak_id])
	olmamis_kabaklari_gez(olmamis_kabaklar, ilk_kabak_id)
	harvest()
	

def big_pumpkin_kontrol(olmamis_kabaklar, ilk_kabak_id):
	if not can_harvest() or get_entity_type() != Entities.Pumpkin:
		olmamis_kabaklar.append((get_pos_x(),get_pos_y()))
		plant_smart(Entities.Pumpkin)
		if ilk_kabak_id[0] == None and get_entity_type() == Entities.Pumpkin:
			ilk_kabak_id[0] = measure()
		
def olmamis_kabaklari_gez(olmamis_kabaklar, ilk_kabak_id):
	while True:
		kalanlar = []
		olmamis_var = False
		
		for x, y in reversed(olmamis_kabaklar):
			git(x, y)

			if ilk_kabak_id[0] != None and get_entity_type() == Entities.Pumpkin and measure() == ilk_kabak_id[0]:
				break

			if not can_harvest() or get_entity_type() != Entities.Pumpkin:
				plant_smart(Entities.Pumpkin)
				if ilk_kabak_id[0] == None and get_entity_type() == Entities.Pumpkin:
					ilk_kabak_id[0] = measure()
				olmamis_var = True
				kalanlar.append((x, y))

		kalanlar.reverse()
		olmamis_kabaklar = kalanlar
		
		if not olmamis_var:
			break
			
