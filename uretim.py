from error_utils import error
from string_utils import join_args
from bitki_ekim import yeterli_malzeme_var_mi
from game_registry import GLOBAL_OBJECTS
from ekim_hay import hay_uret
from ekim_pumpkin import pumpkin_uret

son_bilgilendirme_zamani = 0

URETIM_SENARYOLARI = {
	Items.Hay: {
		"uretim_fonksiyonu": hay_uret,
		"hedef_entity": Entities.Grass,
	},
	Items.Pumpkin: {
		"uretim_fonksiyonu": pumpkin_uret,
		"hedef_entity": Entities.Pumpkin,
	},
}


def uretim_surecini_baslat(item, hedef_adet):
	mevcut_adet = num_items(item)
	while mevcut_adet < hedef_adet:
		uretim_bilgisi(item, mevcut_adet, hedef_adet)
		uretim_yap(item)
		mevcut_adet = num_items(item)


def uretim_yap(item):
	senaryo = _uretim_senaryosu_bul(item)
	if senaryo == None:
		return
	
	GLOBAL_OBJECTS["hedef_uretim"] = senaryo["hedef_entity"]
	_malzeme_yeterliligini_sagla(senaryo["hedef_entity"])
	senaryo["uretim_fonksiyonu"](item)

def _uretim_senaryosu_bul(item):
	if item in URETIM_SENARYOLARI:
		return URETIM_SENARYOLARI[item]

	errorMessage = join_args(["Elde edilmek istenen ürün için (",item,") üretim senaryosu bulunamadı"])
	error(errorMessage)
	do_a_flip()
	do_a_flip()
	do_a_flip()
	return None


def _malzeme_yeterliligini_sagla(entity):
	yeterlilik, eksik_item, ihtiyac_adeti = yeterli_malzeme_var_mi(entity)
	if yeterlilik:
		return

	if eksik_item == None or ihtiyac_adeti == None:
		return

	uretim_surecini_baslat(eksik_item, num_items(eksik_item) + ihtiyac_adeti)


def uretim_bilgisi(item, mevcut_adet, hedef_adet):
	global son_bilgilendirme_zamani

	simdiki_zaman = get_time()

	if simdiki_zaman > son_bilgilendirme_zamani + 5.0:
		son_bilgilendirme_zamani = simdiki_zaman

		if hedef_adet > 0:
			yuzde = (mevcut_adet * 100) / hedef_adet
		else:
			yuzde = 0

		bar_uzunluk = 20
		dolu = (mevcut_adet * bar_uzunluk) / hedef_adet

		bar = "["

		i = 0
		while i < bar_uzunluk:
			if i < dolu:
				bar = bar + "|"
			else:
				bar = bar + " "
			i = i + 1

		bar = bar + "]"

		quick_print("Mevcut: " + str(mevcut_adet) + " / " + str(hedef_adet))
		quick_print(bar + " %" + str(yuzde))

