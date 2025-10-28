#defining in phython
def add_even_elements(matrix):
    sum_value=0
    for row in matrix:
        for element in row:
            if element % 2 == 0:
                sum_value = sum_value + element
    return sum_value
B= [[1,2,3],[5,7,8],[4,9,10]]
value = add_even_elements(B)
print(f"The summation of even values= {value}")
