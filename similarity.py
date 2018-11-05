import math

coppola_brando = [(5.0,5.0),(5.0,4.29)]
coppola_dreyfuss = [(5.0, 1.07), (5.0, 0.63)]
really_liked = [(5.0,5.0),(5.0,5.0)]

def euclidean_distance(points):
	squared_diffs = [(point[0] - point[1]) ** 2 for point in points]
	summed_squared_diffs = sum(squared_diffs)
	distance = math.sqrt(summed_squared_diffs)
	return distance

def similarity(points):
    return 1/(1 + euclidean_distance(points))