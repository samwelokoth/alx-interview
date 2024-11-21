def generate_pascals_triangle(rows):
    triangle = []
    
    for i in range(rows):
        row = [1]
        if i > 0:
            prev_row = triangle[-1]
            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j+1])
            row.append(1)
        triangle.append(row)
    
    return triangle

def print_pascals_triangle(triangle):
    for row in triangle:
        print(row)

num_rows = int(input("Enter the number of rows for Pascal's Triangle: "))
triangle = generate_pascals_triangle(num_rows)
print_pascals_triangle(triangle)
