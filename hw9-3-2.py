# Author: SMR (AMDG) 01/18/22
print('Enter the net sales for')
try:
    previous = float(input('- Prior period:'))
    current = float(input('- Current period:'))

    change = (current - previous) * 100 / previous
    if change > 0:
        result = f'Sales increase {abs(change)}%'
    else:
        result = f'Sales decrease {abs(change)}%'
    print(result)
except ZeroDivisionError:
    print("The value in the prior period cannot be equivilent to zero.")
except ValueError:
    print("Invalid input. Use only numerical values.")

