#!/usr/bin/python3 

# Task 1. Define a function that takes an argument and prints hello...
def hello(str_):
    print ("Hello " + str_)

hello("World")

# Task 2. Define function sum and multiply....

def sum_func(x):
    print(sum(x))

sum_func([1,2,3,4,5])

def mult_func(x):
    l = 1
    for y in x:
        l*=y
    print(l)

mult_func([1,2,3,4,5])

# Task 3, Function reverse

def reverse(str_):
    print(str_[::-1])

reverse("Hello World")

# Task 4. Palindrome function

def is_palindrome(str_):
    print (str_==str_[::-1])

is_palindrome("radar")

# Task 5. Histogram

def histogram(list_):
    for i in list_:
        print('*'*i)

histogram([4,9,7])

# Task 6. Caesar Cipher

def caesar_cipher(str_, x):
    res_str=''
    for i in str_:
        res_str+=chr(ord(i)+x)
    print(res_str)

caesar_cipher("abcdef", 3)

# Task 7. List reverse

def diaginal_reverse(list_):
    res_list = [[],[],[]]
        for i in list_:
            l = 0
            for j in i:
                res_list[l].append(j)
                l+=1
    print(res_list)

diaginal_reverse([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

# Task 8. Random Game

import random

def game(x,y):
    guess_number = random.randint(x,y)
    print("Guess")
    user_try = int(input())
    while True:
        if user_try == guess_number:
            print('Win')
            break
        else:
            print('Try again')
            user_try = int(input())

x,y = input().split()
game(int(x),int(y))

# Task 9. Brackets

def brackets(str_):
    counter = 0 
    for x in str_:
        if x == '[': counter+=1
        if x == ']': counter-=1
        if counter < 0: print('Not Ok')
    if counter == 0: print('Ok')
    else: print('Not ok')

brackets('[[[][]]')

# Task 10. Letter freq

def char_freq(str_):
    a = {}
    for i in str_:
        if i in a.keys(): a[i]+=1
        else: a[i]=1
    print (a)

char_freq('aaabbbbccddddd')

# Task 11. DEC to BIN

def dec_to_bin(x):
    print(bin(x))

dec_to_bin(115)
