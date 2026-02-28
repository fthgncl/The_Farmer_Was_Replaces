from hareket import her_yerde_uygula, git
from zemin import zemini_uygun_hale_getir
from bitki_ekim import plant_smart

def uret_pumpkin():
	pumpkin_ek()
	
def pumpkin_ek():
	olmamis_kabaklar = []
	her_yerde_uygula(big_pumpkin_kontrol, True , [olmamis_kabaklar])
	olmamis_kabaklari_gez(olmamis_kabaklar)
	harvest()
	
	
def big_pumpkin_kontrol(olmamis_kabaklar):
	if not can_harvest() or get_entity_type() != Entities.Pumpkin:
		olmamis_kabaklar.append((get_pos_x(),get_pos_y()))
		plant_smart(Entities.Pumpkin)
		
def olmamis_kabaklari_gez(olmamis_kabaklar):
	while True:
		kalanlar = []
		olmamis_var = False
		
		for x, y in olmamis_kabaklar:
			git(x, y)
			if not can_harvest() or get_entity_type() != Entities.Pumpkin:
				plant_smart(Entities.Pumpkin)
				olmamis_var = True
				kalanlar.append((x, y))

		olmamis_kabaklar = kalanlar
		
		if not olmamis_var:
			break
			