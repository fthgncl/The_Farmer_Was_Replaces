from string_utils import split
from error_utils import error

GLOBAL_OBJECTS = {
	"Items": Items,
	"Entities": Entities
}

def resolve_path(path):
	segments = split(path, ".")
	obj = GLOBAL_OBJECTS[segments[0]]

	i = 1
	while i < len(segments):
		target = str(obj) + "." + str(segments[i])

		found = False
		for candidate in obj:
			if str(candidate) == target:
				obj = candidate
				found = True
				break

		if not found:
			
			error("resolve_path: not found -> " + target)
			return None

		i += 1
	
	return obj