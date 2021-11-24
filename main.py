# https://www.codewars.com/kata/559f44187fa851efad000087/train/python
# 7kyu
from typing import Sequence


def seven_ate9(str_):
    while '797' in str_:
        str_ = str_.replace('797' , '77')
    return str_


# print(seven_ate9('79997'))

# 7kyu
def add(*a):
  sum = 0 
  for i in a :
    sum += i 
  return sum  
  
# print(add(2,3))


# 5 kyu 
def rotate(matrix, direction): 
    new_matrix = []

    if direction=="clockwise":
        for j in range(0,len(matrix[0])):
            list_cc = []
            for i in range(0,len(matrix)):
                list_cc.append(matrix[i][j])
            list_cc.reverse()
            new_matrix.append(list_cc)
    
    elif direction=="counter-clockwise":
        for j in range(0,len(matrix[0])):
            list_cc = []
            for i in range(0,len(matrix)):
                list_cc.append(matrix[i][j])
            new_matrix.insert(0,list_cc)
    else:
        pass    
    return new_matrix

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
# print(rotate(matrix ,'counter-clockwise'))

# 7 kyu
def generate_shape(n):
    s = ""
    for i in range(n):
      for j in range(n):
        s += "+"
      if i < n-1:
        s += "\n"
    return s

# print(generate_shape(4))


# https://www.codewars.com/kata/5933a1f8552bc2750a0000ed/train/python
def nth_even(n):
  # pass
  return (n*2)-2
# test_case = [1 , 2  , 3 , 100 ,1298734] 
# for i in test_case:
#   print("result:",nth_even(i))


# https://www.codewars.com/kata/57cfdf34902f6ba3d300001e/train/python
def two_sort(array):
    # Sort 
    array = set(array)
    array = sorted(array, reverse=True)
    array.sort()
    # print(array)
    str1 = array[0]
    buff = ""
    for i in range(0,len(str1)):
      buff += str1[i] 
      if len(str1)-1 > i:
       buff+= '***'
    return buff
# lst1 = ["turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"]
# lst2 = ["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]
# lst3 = ["i", "want", "to", "travel", "the", "world", "writing", "code", "one", "day"]
# print(two_sort(lst))
# l = [lst1 , lst2 , lst3]
# for i in l : 
#   print(two_sort(i))


# https://www.codewars.com/kata/57cc981a58da9e302a000214/python
def small_enough(array, limit):
    buff = []
    for i in range(len(array)):
      # print(array[i])
      if array[i]  <= limit:
        buff.append(True)  
      else:
        buff.append(False)
    print(buff)
    if (False in buff):
      return False 
    else :
      return True 

# test =[12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
# lim = 12
# print(small_enough(test , lim))


# https://www.codewars.com/kata/5511b2f550906349a70004e1/train/python
def last_digit(n1, n2):
  if n2 == 0 :return 1 
  return pow(n1,n2,10)


# https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python
# 4 kyu
def solution(string,markers):
    lst = string.split('\n')
    for i, s in enumerate(lst):
        for j in markers:
            f = s.find(j)
            s = s[0:f] if f >= 0 else s[:]
        lst[i] = s.strip()

    return '\n'.join(lst)


# string = "apples, pears # and bananas\ngrapes\nbananas !apples"
# markers = ["#", "!"]
# print(solution(string , markers))


# https://www.codewars.com/kata/5262119038c0985a5b00029f/train/python
# 6 kyu

# def is_prime(n):
#   if n<=1:return False
#   factor = 0 
#   for i in range(1 ,n+1):
#     if n%i == 0 :factor +=1 

#   if factor == 2 :
#     return True
#   return False 

def is_prime(n):
  if n <= 1: return False 
  i = 2 
  while i*i <= n :
    if n%i == 0 : return False 
    i+=1 
  return True

# def is_prime(num):
#     import math

#     # There's only one even prime: 2
#     if num < 2    : return False
#     if num == 2   : return True
#     if num %2 == 0: return False
    
#     """
#     Property:
#         Every number n that is not prime has at least one prime divisor p
#         such 1 < p < square_root(n)
#     """
#     root = int(math.sqrt(num))
    
#     # We know there's only one even prime, so with that in mind 
#     # we're going to iterate only over the odd numbers plus using the above property
#     # the performance will be improved
#     for i in range(3, root+1, 2):
#         if num % i == 0: return False

#     return True

# lst = [0 , 1 , 2 , 73 , 75 , -1]
# for i in range(len(lst)):
#   print(is_prime(lst[i]))


import math as m 
import random 
def how_much_i_love_you(n):
    # your code
    array = ["I love you",
            "a little",
            "a lot",
            "passionately",
            "madly",
            "not at all",]
    return array[(n-1)%6]

# re = [7 , 3 , 6]
# for i in re : 
#   print(how_much_i_love_you(i))


ticks = [1 , 2 , 3 , 4 , 5 , 
         6 , 7 , 8 , 9 , 10, 
         11 , 12 , 13 ,  14, 
         15 , 16 , 17 , 18 , 19 , 20 ]

pwm = 212.5
set_pwm = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
# for i in ticks : 
#   print(f"{i} : {(i/0.000785)}") 

# for j in set_pwm: 
#   print(f"{j} m/s : {pwm * j}")

nn = 12.7 # max 41800 mah
cu = 12.0 # ?? mah 

result = (cu * 41800 )/ 12.7
# print(result)


def correct(s):
  for i in s:
    if i == '5':
      s = s.replace('5' , 'S')
    elif i == '0':
      s = s.replace('0' , 'O')
    elif i == '1':
      s = s.replace('1' , 'I')
  return s
# f = ['L0ND0N' , 'DUBL1N' , '51NGAP0RE']
# for i in f : 
#   print(correct(i))

def median(array):
  size = len(array)
  if size % 2 != 0 :
        array.sort()
        # print(array)
        return array[int(size/2)]
  else:
    sort = sorted(array)
    even = len(sort) / 2
    return (sort[int(even)] + sort[int(even)-1])/2

# odd = [797, 853, 23, 172, 833, 631, 740]
# print(median(odd))