from hareket import her_yerde_uygula, git
from zemin import zemini_uygun_hale_getir
from configs import max_power

sunflowers = []

def uret_power():
	on_ay_cicegi_ayarla()
	ay_ciceklerini_hasat_et()
	

def on_ay_cicegi_ayarla():
	#her_yerde_uygula(aycicegini_kaldir)
	for i in range(10):
		x = i/3//1
		y = i%3
		yaprak = ay_cicegi_ek_ve_tac_don(x,y)
		sunflowers.append((x,y,yaprak))

def aycicegini_kaldir():
	if get_entity_type() == Entities.Sunflower:
		harvest()

def ay_ciceklerini_hasat_et():
	while num_items(Items.Power) < max_power:	# Hedefe ulaşana kadar hasat yap
		max_yaprak = 0
		hedef_x = 0
		hedef_y = 0
		hedef_ay_cicegi_index = 0 
		for i in range(10):
			x, y, yaprak = sunflowers[i]
			if yaprak > max_yaprak:
				max_yaprak = yaprak
				hedef_x = x
				hedef_y = y
				hedef_ay_cicegi_index = i
		
		git(hedef_x,hedef_y)
		while not can_harvest():
			use_item(Items.Fertilizer)
		
		use_item(Items.Weird_Substance)	
		harvest()
		plant(Entities.Sunflower)
		sunflowers[hedef_ay_cicegi_index] = (hedef_x, hedef_y, measure())
				

def ay_cicegi_ek_ve_tac_don(x,y):
	git(x,y)
	harvest()
	zemini_uygun_hale_getir(Entities.Sunflower)
	plant(Entities.Sunflower)
	return measure()
	