A = float(input('Enter a coefficient: '))
B = float(input('Enter b coefficient: '))
C = float(input('Enter c coefficient: '))

if A == 0:
    print('Since a = 0, function is not a quadratic.')

else:
    SOLUTION1 = (-B+((B*B-4*A*C)**(1/2.0)))/(2*A)
    SOLUTION2 = (-B-((B*B-4*A*C)**(1/2.0)))/(2*A)
    print('solution 1 is:', SOLUTION1)
    print('solution 2 is:', SOLUTION2)    