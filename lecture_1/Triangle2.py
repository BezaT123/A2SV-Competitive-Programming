def triangle_2(num_of_rows):
    for i in range(0,num_of_rows):
        for j in range(0,num_of_rows-1-i):
            print(" ",end='')
        for j in range(0,i+1):
            
            print("*",end='')
        for j in range(1,i+1):
            print("*",end='')
        print()
triangle_2(5)