def add_numbers(n1, n2):
    sum = n1 + n2
    return sum
    
def multiply_numbers(m1, m2):
    multiply = m1 * m2
    return multiply
    
n1 = int(input("Enter x value: "))
n2 = int(input("Enter y value: "))
sum = add_numbers(n1, n2)
print("answer is ", sum)

m1 = int(input("\n For multiplication \n Enter x value: "))
m2 = int(input("Enter y value: "))
multiply = multiply_numbers(m1, m2)
print("answer is", multiply)
    
