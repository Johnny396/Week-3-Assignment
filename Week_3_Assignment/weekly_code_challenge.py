"""Coding challenge for basic control flows and functions"""

#Large Power
def large_power(base, exponent):
    """Large Power"""
    power = base**exponent
    if power > 5000:
        return True
    else: 
        return False


print(large_power(58,69))


#Divisible By Ten
def divisible_by_ten(num):
    """Divisible By Ten"""
    remainder = num % 10
    if remainder == 0:
        return True
    else:
        return False