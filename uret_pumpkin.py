from hareket import git, capraz_uygula
from zemin import zemini_uygun_hale_getir
from bitki_ekim import plant_smart, sula

def uret_pumpkin():
	pumpkin_ek()
	
def pumpkin_ek():
	kabaklar = []
	capraz_uygula(big_pumpkin_kontrol, True, [kabaklar])
	olmamis_kabaklari_gez(kabaklar)
	harvest()
	
	
def big_pumpkin_kontrol(kabaklar):
	if not can_harvest() or get_entity_type() != Entities.Pumpkin:
		plant_smart(Entities.Pumpkin, False)
		
	if get_entity_type() == Entities.Pumpkin:
		kabaklar.append((get_pos_x(),get_pos_y(),measure()))
		
def olmamis_kabaklari_gez(olmamis_kabaklar):
	while True:
		
		i = len(olmamis_kabaklar) - 1
		
		if i <= 0:
			break
		
		while i >= 0:
			x, y, _measure = olmamis_kabaklar[i]
			git(x,y)
			while not can_harvest():
				if get_entity_type() == Entities.Dead_Pumpkin:
					plant(Entities.Pumpkin)
				
				if num_items(Items.Fertilizer) > 0:
					use_item(Items.Fertilizer)
				else:
					sula()
			
			olmamis_kabaklar[i] = (get_pos_x(),get_pos_y(),measure())
			ana_kabak = eslesen_ilk_kabak_bul(olmamis_kabaklar,i)
			if ana_kabak != None:
				x_ana_kabak, y_anakabak, _ = ana_kabak
				alani_kaldir(olmamis_kabaklar,(x_ana_kabak, y_anakabak),(x,y))
			else:
				olmamis_kabaklar.pop(i)
			
				
			i = len(olmamis_kabaklar) - 1
			
			
def eslesen_ilk_kabak_bul(kabaklar,aranan_index):
	_,_,aranan_measure = kabaklar[aranan_index]
	for i in range(len(kabaklar)):
		x, y, measure = kabaklar[i]
		if measure == aranan_measure and i != aranan_index:
			return kabaklar[i]
			
	return None
	
def alani_kaldir(olmamis_kabaklar, konum1, konum2):
	
	x1, y1 = konum1
	x2, y2 = konum2
	x_start = None
	x_end = None
	y_start = None
	y_end = None
	
	if x1 < x2:
		x_start = x1
		x_end = x2
	else:
		x_start = x2
		x_end = x1
		
	if y1 < y2:
		y_start = y1
		y_end = y2
	else:
		y_start = y2
		y_end = y1
		
		
	i = 0
	length = len(olmamis_kabaklar)
	while i < length:
		x, y, _ = olmamis_kabaklar[i]

		if x == x_start and y == y_start:
			i = i+1
			continue
		
		if x_start <= x and x <= x_end:
			if y_start <= y and y <= y_end:
				olmamis_kabaklar.pop(i)
				length  = length - 1
				i = i-1
				
		i = i+1
		
		
		
		
		
		
		