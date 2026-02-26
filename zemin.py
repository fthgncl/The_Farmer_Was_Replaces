from string_utils import join_args
from error_utils import error

def zemini_uygun_hale_getir(entity):
	
	zemin_farketmeyenler = [
		Entities.Grass,
		Entities.Bush,
		Entities.Tree
	]
	
	soil_zemin_isteyenler = [
		Entities.Carrot,
		Entities.Pumpkin,
		Entities.Sunflower,
		Entities.Cactus
	]
	
	grassland_zemin_isteyenler = []
	
	for ent in zemin_farketmeyenler:
		if ent == entity:
			return
	
	for ent in soil_zemin_isteyenler:
		if ent == entity:
			zemini_ayarla(Grounds.Soil)
			return
	
	for ent in zemin_farketmeyenler:
		if ent == entity:
			zemini_ayarla(Grounds.Grassland)
			return


	errorMessage = join_args([entity," için zemin yapılandırılması bulunamadı."])
	error(errorMessage)
	
		
def zemini_ayarla(groundType = None):
	if groundType == None or groundType != get_ground_type():
		till()