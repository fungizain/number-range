def range_spliter(start, end, distance):
	if not (isinstance(start) and isinstance(end) and isinatance(distance)):
		return "Fuck you input integer ar!"
	num_range, steps = end - start, num_range // distance + 1
	return ','.join([f"{start}-{start+distance}" for i in range(steps)])

if __name__ == "__main__":
	print(range_spliter(1, 120, 3))
