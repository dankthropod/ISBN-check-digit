def incr(lst, i):
    return [x+i for x in lst]

def lst():
    num = int(input(print("Enter ISBN digit: ")))
    return [int(a) for a in str(num)]

def odd_even(lst):
    odd_numbers = []
    even_numbers = []

    for number in lst:  
        if number % 2 == 1:
            odd_numbers.append(number)
        elif number % 2 == 0:
            even_numbers.append(number)
    
    return(odd_numbers,even_numbers)

def check_digit(odd):
    odd_list = odd[0]
    even_list = odd[1]
    even = 3 * (sum(even_list))
    odd = sum(odd_list)
    remainder = (even+odd)%10
    if (remainder == 0):
        return remainder
    else:
        remainder = 10-remainder
        return remainder



print(check_digit(odd_even(lst())))