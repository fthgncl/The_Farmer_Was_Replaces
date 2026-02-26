from hareket import git
from zemin import zemini_uygun_hale_getir

def companion_process(entity = None):
	if not entity == None and not entity == get_entity_type():
		return
	
	companion = get_companion()
	if not companion:
		return
		
	hedef_entity, konum = companion
	x,y = konum
	git(x,y, True, companion_bitkiyi_ek, [hedef_entity])
	
def companion_bitkiyi_ek(entity):
	if can_harvest():
		harvest()
		
	zemini_uygun_hale_getir(entity)
	plant(entity)
	


	