# def division(a,b):
#     x=str(a)
#     quotent=0
#     remainder=b
#     result=""
#     dividend = x[0]
#     index = 0
#     while True:
#         if remainder == 0:
#             break
#         print(dividend)
#         while int(dividend) < b:
#             index+=1
#             dividend = x[:index+1]
#         print(dividend)
#         quotent = int(dividend)//b
#         result= result + str(quotent)
#         remainder= int(dividend) % b
#         difference = int(dividend)- (quotent* b)
#         if difference ==0:
#             dividend = x[index+1:]
#         else:
#             dividend = str(difference) + x[index+1:]
#         print("hallo")
#         if dividend == "":
#             remainder = 0
#         else:
#             remainder = int(dividend[0])
#             dividend
#     print(result)
# division(155555,5)

def division(a,b):
    x = str(a)
    dividend = x[0]
    quotent = 0
    remainder = b
    index = 0
    result = ""
    count = 0
    while True:
                
        while int(dividend) < b:
            index += 1
            # count +=1
            dividend = x[:index + 1]
        
        quotent = int(dividend) // b
        result= result + str(quotent)

        remainder = int(dividend) - (quotent * b)
        # if remainder == 0:
        index +=1
        if remainder < b and index == len(x):
            break
        dividend = str(remainder) + x[index:index +1]
    print(result)
division(100,5)

        
        


