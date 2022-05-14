# https://www.codewars.com/kata/559f44187fa851efad000087/train/python
# 7kyu
from operator import index, ne

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

def single_digit(n):
  buff = bin(n).replace('0b' , '')
    

# print(single_digit(123456789))


def reverse_number(n):
  s = str(n)
  if s[0] == '-':
    s = s.replace('-','')
    return (-2*(int(s[::-1])) + int(s[::-1])) # Or method * -1 (LOL)
  else:
    return int(s[::-1])

# print(reverse_number(123))


def is_triangular(n):
    x = 8.0*n+1.0
    return x % x**0.5 == 0.0

def halving_sum(n): 
  # n + n/2 + n/4 + n/8 + ...
  s = 0 
  while n != 0 : 
    s += n 
    n =  n // 2 
  return s 

# print(halving_sum(25))
# https://www.codewars.com/kata/5dd462a573ee6d0014ce715b/train/python
def same_case(a, b): 
  if (ord(a)>=65 and ord(a)<=90) and (ord(b)>=65 and ord(b)<=90): return 1    # A-Z == A-Z 
  elif (ord(a)>=97 and ord(a)<=122) and (ord(b)>=97 and ord(b)<=122): return 1  # a-z == a-z
  elif (ord(a) >= 65 and ord(a)<=90) and (ord(b)>=97 and ord(b)<=122) : return 0   # A-Z != a-z
  elif (ord(b) >= 65 and ord(b)<=90) and (ord(a)>=97 and ord(a)<=122) : return 0 # a-z != A-Z
  elif (type(a) and type(b) ) != type(str) : return -1 
  elif ((ord(a)<65 and ord(a)>122) or (ord(b)<65 and ord(b)>90)):return -1
  elif ((ord(b)<65 and ord(b)>122) or (ord(a)<65 and ord(a)>90)):return -1
  

# print(same_case('H',':'))

# a = np.arange(6).reshape((2,3))
# np.reshape(a,(3,-1))
# print(a)

# p = True 
# q = False 

# if p ^ q :
#   print("k")

def fibonacci(n):
    if n == 1 or n == 2:
        return 1 
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

# a = range(3,8)
# print(list(map(lambda x : fibonacci(x+1) , a )))

import multiprocessing as mp
import numpy as np 

def f(a,b):
  print(np.matmul(a,b))
  # print(a+b)

# if __name__ == '__main__':
#   a = np.array([[i for i in range(10)] for _ in range(10)])
#   b = np.array([[i*2 for i in range(10)] for _ in range(10)])
#   p = mp.Process(target = f , args=(a,b))
#   p.start()


def final_grade(exam, projects):
    if exam > 90 or projects  > 10:return 100 
    elif exam > 75 and projects >= 5 : return 90 
    elif exam > 50 and projects >= 2 : return 75 
    else: return 0 


def binary_array_to_number(arr):
    count = 0 
    sum = 0
    bit=[1,2,4,8,16,32,64,128]
    for i in range(len(arr)-1 , -1 , -1):
      # print(arr[i])
      if arr[i] == 1 :
        # print("Bit count : ",bit[count])
        sum+=bit[count]
      count+=1 
    return sum 

  # s = 0
  # for i in arr:
  #   s=s*2 +i 
  # return s 

# print(binary_array_to_number([1,1,1,0,1]))

def ice_brick_volume(radius, bottle_length, rim_length):
    return 2*(radius**2) * (bottle_length - rim_length)



def calculate2(num1, op, num2): 
    # your code here
    if op == '+': return num1 + num2
    elif op == '-' :return num1 - num2 
    elif op == '*' :return num1 * num2 
    elif op == '/' : 
      if num1 == 0 or num2 == 0 : return None
      return num1 / num2  
    else:return None


import math as m 
arr = [4, 3, 9, 7, 2, 1 ]
def square_or_square_root(arr):
  new_arr = []
  for i in range(len(arr)):
    if m.ceil(m.sqrt(arr[i])) == m.floor(m.sqrt(arr[i])):
      new_arr.append(int(arr[i]**0.5))
    else:
      new_arr.append(arr[i]**2)
      
  return new_arr

# print(square_or_square_root(arr))


s = "Look mom, no hands"
h = "4c6f6f6b206d6f6d2c206e6f2068616e6473"

bytes_obj = bytes.fromhex(h)
ascii_str = bytes_obj.decode("ASCII")
# print(ascii_str)

ascii_hex = ""
for i in s:
  ascii_hex+= hex(ord(i)).replace("0x" , "")

# print(ascii_hex)


class Converter():
  @staticmethod
  def to_ascii(h):
      #your code here
      bytes_obj = bytes.fromhex(h)
      return bytes_obj.decode("ASCII")
  @staticmethod
  def to_hex(s):
      #your code here
      ascii_hex = ""
      for i in s:
          ascii_hex+= hex(ord(i)).replace("0x" , "")
      return ascii_hex

num = [ 1, 1, 1, 2, 1, 1 ]

def find_uniq(arr):
  buff = [] 
  for i in arr :
    if i not in buff : 
      buff.append(i)
  # print(buff)
  buff2=[]
  a = 0 
  for i in range(len(buff)) : 
    for j in arr: 
      if buff[i] == j : 
        a+=1
    buff2.append(a)
    a = 0 
  # print(buff2)

  element_list = buff2.index(min(buff2))
  #print(buff[element_list])
  return buff[element_list]
# print(find_uniq(num))

list_str = [ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]
list_str_2 = [ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]
list_str_3 = [ '', '', '', 'a', '', '' ]
arr = ['0x1' , '0x2']

def find_u (arr):
  buff = []
  index_ele = 0 
  if (arr[0])[0:2] == '0x':
    index_ele +=2
  # print(index_ele)
  for i in range(len(arr)):
    if arr[i] == '':
      arr[i] = "buff"
    buff.append((arr[i])[index_ele])
  # print(buff)
  # print(arr)
  # Check 
  sbuff = list(set(buff))
  # print(sbuff)
  c = []
  a = 0 
  for j in range(len(sbuff)):
    for k in range(len(arr)):
      if sbuff[j] == (arr[k])[index_ele]:
        a+=1 
    c.append(a)
    a = 0 
  element_list = c.index(min(c))
  # print(element_list)
  s= ""
  for e in arr:
    if sbuff[element_list] == e[index_ele]:
      s+=e
      # print(e)
  return s

# print(find_u(list_str))

# def int_to_negabinary(i):
#     ds = []
#     while i != 0:
#         ds.append(i & 1)
#         i = -(i >> 1)
#     return ''.join(str(d) for d in reversed(ds)) if ds else '0'
    
# def negabinary_to_int(s):
#     i = 0
#     for c in s:
#         i = -(i << 1) + int(c)
#     return i



def int_to_negabinary(i):
  return bin((i+0xAAAAAAAA)^0xAAAAAAAA).replace("0b","")
# print(int_to_negabinary(4587))

def negabinary_to_int(s):
  # base = [1 , -2 , 4 , -8 , 16 , -32 , 64 , -128 , 256 , -512 , 1024 , -2048 , 4096 , -8192]
  base_size = [1] 
  size = len(s) -1
  neg_to_int = 0 
  base = 1 
  for i in range(len(s)):
    if i %2 == 0 :
      base *= -2
    else:
      base *= -2 
    base_size.append(base)
  # print(base_size)
  for j in range(len(s)):
    if s[j] == '1':
      neg_to_int += base_size[size]
      # print(neg_to_int , end=" ")
    size -=1
  return neg_to_int

# print(negabinary_to_int('1011000111111'))



def fibonacci (n):
  f = []
  for i in range(n+1):
    f.append(i)
  # print(f)
  fn = [] 
  sfn = []
  for i in range(len(f)):
    if i == 0 :
      fn.append(0)
    elif i == 1 : 
      fn.append(1)
      sfn.append("1-st Fibo")
    elif i == 2 : 
      fn.append(1) 
      sfn.append("2-nd Fibo")
    else:
      fn.append(fn[i-1] + fn[i-2])
      if i ==3 :
        sfn.append("3-rd Fibo")
      else:
        sfn.append(f"{i}-th Fibo")

    #   print(fn[i-1] , fn[i-2] , fn[i-1]+fn[i-2])
    # print(fn,i)
  return fn[n]

# print(fibonacci(100))

def nth_fib (n):
  f = []
  for i in range(n+1):
    f.append(i)
  # print(f)
  fn = [] 
  sfn = []
  for i in range(len(f)):
    if i == 0 :
      fn.append(0)
      sfn.append("1-st Fibo")
    elif i == 1 : 
      fn.append(1)
      sfn.append("2-nd Fibo")
    elif i == 2 : 
      fn.append(1) 
      sfn.append("3-rd Fibo")
    else:
      fn.append(fn[i-1] + fn[i-2])
      sfn.append(f"{i}-th Fibo")

    #   print(fn[i-1] , fn[i-2] , fn[i-1]+fn[i-2])
    # print(fn,i)
  element = sfn.index(sfn[n-1])
  return fn[element]
# print(nth_fib(7))


''' No library '''

def bin_to_decimal (n_str):
  # Gen binary
  # arr_bin = []
  # for i in range(len(n_str)):
  #   arr_bin.append(2**i)
  # print(arr_bin)
  result = 0 
  for lst_bin in range(len(n_str)):
    if n_str[::-1][lst_bin] == '1':
      # result+= arr_bin[lst_bin]
      result+= 2**lst_bin
  return result

# print(bin_to_decimal("1001001"))

# import operator 
# def calculate(s):
#   ops = {"+" : operator.add ,
#          "-" : operator.sub}

#   # print(ops["+"](1,1))
  

# print(calculate(s=1))

def digitize2(n):
    n = str(n)[::-1]
    ans = []
    for i in range(len(n)):
      ans.append(int(n[i]))
    return ans


def rgb(r, g, b):
    r , g , b = str(hex(r)) , str(hex(g)) , str(hex(b))
    return (r + g + b).replace("0x", "")

# print(rgb(1 , 2 , 3))

def count_positives_sum_negatives(arr):
    lst_positive = []
    lst_negative = []
    size = len(arr)
    for i in range(len(arr)):
      if arr[i] <= 0 :
        lst_negative.append(arr[i])
      else:
        lst_positive.append(arr[i])
    if  arr == []:
      return [] 
    else:
      return [len(lst_positive) , sum(lst_negative)]

# print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))

#https://www.codewars.com/kata/5813d19765d81c592200001a
def dont_give_me_five(start,end):
  range_num = [ str(num) for num in range(start , end+1 , 1)]
  print(range_num) 
  new_arr = []
  for i in range(len(range_num)):
    if '5' in range_num[i]:
      pass 
    else:
      new_arr.append(range_num[i])
  print(new_arr)
  return len(new_arr)

print(dont_give_me_five(start=1, end=9)) 
