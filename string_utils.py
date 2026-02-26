def replace(text, old, new):
	result = ""
	i = 0

	while i < len(text):
		# Eğer buradan başlayan parça old ile eşleşiyorsa
		if text[i:i+len(old)] == old:
			result += new
			i += len(old)
		else:
			result += text[i]
			i += 1

	return result
	
	
def split(text, separator):
	result = []
	current = ""
	i = 0

	while i < len(text):
		if text[i:i+len(separator)] == separator:
			result.append(current)
			current = ""
			i += len(separator)
		else:
			current += text[i]
			i += 1

	# Son parçayı ekle
	result.append(current)

	return result
	
def join_args(values):
	result = ""
	i = 0
	
	while i < len(values):
		result += str(values[i])
		
		if i < len(values) - 1:
			result += " "
			
		i += 1
	
	return result