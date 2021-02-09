def power_of_number_iterative(b,e):
    i = 0
    product = 1
    while i < e:
        product *= b
        i+=1
    return product
def power_of_number_recursive(b,e):
    assert e >= 0 and int(e) == e, "exponent should not be negative"
    if e == 0:
        return 1
    return b * power_of_number_recursive(b,e-1)
print(power_of_number_recursive(-2,3))
