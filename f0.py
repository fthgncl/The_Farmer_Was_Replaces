harvest()
plant(Entities.Sunflower)

while not can_harvest():
	quick_print(measure())
	
quick_print(measure())