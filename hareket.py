from utils import fonksiyon_cagir, bos_fonksiyon
	
def basa_don():
	while (get_pos_x() > 0):
		move(West)
		
	while (get_pos_y() > 0):
		move(South)
		
def her_yerde_uygula(fonksiyon, uygulama_ekseni = True, fnc_params = [], start_x = 0, start_y = 0):
	git(start_x, start_y)
	for y in range(get_world_size()):
		
		for x in range(get_world_size()):
			fonksiyon_cagir(fonksiyon,fnc_params)
			if uygulama_ekseni:
				move(East)
			else:
				move(North)
				
		if uygulama_ekseni:
			move(North)
		else:
			move(East)
			
def git(x, y, geri_gel=False, fonksiyon = bos_fonksiyon, params = []):
	world = get_world_size()
	
	start_x = get_pos_x()
	start_y = get_pos_y()

	# --- X ekseni ---
	current_x = start_x
	dx = x - current_x
	
	if dx > 0:
		wrap_dx = dx - world
	else:
		wrap_dx = dx + world
		
	if abs(wrap_dx) < abs(dx):
		dx = wrap_dx
	
	if dx > 0:
		for i in range(dx):
			move(East)
	elif dx < 0:
		for i in range(-dx):
			move(West)

	# --- Y ekseni ---
	current_y = get_pos_y()
	dy = y - current_y
	
	if dy > 0:
		wrap_dy = dy - world
	else:
		wrap_dy = dy + world
	
	if abs(wrap_dy) < abs(dy):
		dy = wrap_dy
	
	if dy > 0:
		for i in range(dy):
			move(North)
	elif dy < 0:
		for i in range(-dy):
			move(South)
	
	fonksiyon_cagir(fonksiyon, params)

	if geri_gel:
		git(start_x, start_y)