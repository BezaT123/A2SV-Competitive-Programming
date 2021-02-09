def product_of_array_iterative(arr):
    product = 1
    for i in range(len(arr)):
        product *= arr[i]
    return product

def product_of_array_recursive(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] * product_of_array_recursive(arr[1:])
print(product_of_array_recursive([1,2,3,4,5]))