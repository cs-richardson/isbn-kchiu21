"""
Code written by Kolton
In this program, the user puts in a isbn string, then the programs
checks if the isbn string is either valid or invalid then prints "YES" or "NO". 
"""
sum = 0
isbn_input = input("ISBN: ")
while isbn_input.isdigit() == False:
    isbn_input = input("Retry: ")
isbn_input = int(isbn_input)
tenth_digit = isbn_input % 10
for i in range (1, 10):
    digit_num = isbn_input % (10 ** (i + 1))
    digit_num = digit_num // (10 ** i)
    sum = sum + digit_num * (10 - i)
if sum % 11 == tenth_digit:
    print ("YES")
else:
    print ("NO")
