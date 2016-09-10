def generate_pascal_triangle(rows):
    if rows == 1: return [[1]]

    triangle = [[1] ,[1,1]]

    row = [1,1]

    for i in range(2,rows):
        rows = [1] + [sum(column) for column in zip(row[1:], row)] + [1]
        triangle.append(row)

    return triangle

for row in generate_pascal_triangle(6):
   print(row)
