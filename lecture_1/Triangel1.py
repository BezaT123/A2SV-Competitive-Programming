def triangle_1(num_of_rows):
    for i in range(0,num_of_rows):
        for j in range(0,i+1):
            print("*",end='')
        print()
triangle_1(5)