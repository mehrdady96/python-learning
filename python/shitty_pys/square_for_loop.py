



my_list = []

for y in range(10):
    row = []
    for x in range(10):
        row.append((y,x))
    my_list.append(row)


def move_in_sqaure(matrix):
    x_start = 0
    y_start = 0
    array = []
    sqaure_size = 5
    height = len(matrix) - sqaure_size + 1
    width = len(matrix[0]) - sqaure_size + 1
    for y_start in range(0 , height , sqaure_size):
        for x_start in range(0 , width , sqaure_size):
            sqaure = []
            for y in range(y_start , y_start + sqaure_size):
                row = []
                for x in range(x_start , x_start + sqaure_size):
                    row.append(matrix[y][x])  
                sqaure.append(row)       
            array.append(sqaure)
    return array





for matrix in move_in_sqaure(my_list):
    for row in matrix:
     print(row)
    print()