def range_spliter(start, end, distance):
    if not (isinstance(start, int) and isinstance(end, int) and isinstance(distance, int)):
        return "Those variable shd be integer."
    num_range = end - start
    steps, remainder = num_range // distance, num_range % distance
    l = [f"{start + i * distance}-{start + (i + 1) * distance - 1}" for i in range(steps)]
    l.append(f"{start + steps*distance}-{end}") if remainder else None
    return ','.join(l)

if __name__ == "__main__":
    print(range_spliter(1, 120, 4))
