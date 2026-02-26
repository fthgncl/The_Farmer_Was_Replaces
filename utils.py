from error_utils import error

def bos_fonksiyon():
	pass

def fonksiyon_cagir(fonksiyon = bos_fonksiyon, p = []):
	l = len(p)

	if l > 5:
		error("Fonksiyon en fazla 5 parametre alabilir.")
		return

	if l == 0:
		fonksiyon()
	elif l == 1:
		fonksiyon(p[0])
	elif l == 2:
		fonksiyon(p[0], p[1])
	elif l == 3:
		fonksiyon(p[0], p[1], p[2])
	elif l == 4:
		fonksiyon(p[0], p[1], p[2], p[3])
	elif l == 5:
		fonksiyon(p[0], p[1], p[2], p[3], p[4])