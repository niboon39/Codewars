# https://www.codewars.com/kata/559f44187fa851efad000087/train/python
# 7kyu
from cgi import test
from hashlib import new
from http.client import REQUEST_URI_TOO_LONG, CannotSendHeader
from msilib.schema import Error
from operator import index, ne
from pickle import FALSE
from tkinter import Y

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
  f = [i for i in range(n+1)]
  # f= [] 
  # for i in range(n+1):
  #   f.append(i)
  # print(f)
  fn = [] 
  sfn = []
  for i in range(len(f)):
    if i == 0 :
      fn.append(0)
    elif i == 1 : 
      fn.append(1)
      # sfn.append("1-st Fibo")
    elif i == 2 : 
      fn.append(1) 
      # sfn.append("2-nd Fibo")
    else:
      fn.append(fn[i-1] + fn[i-2])
      # if i ==3 :
      #   sfn.append("3-rd Fibo")
      # else:
      #   sfn.append(f"{i}-th Fibo")

    #   print(fn[i-1] , fn[i-2] , fn[i-1]+fn[i-2])
    # print(fn,i)
  return fn[n]

# print(fibonacci(10))

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
  print("Total numbers : ",range_num) 
  new_arr = []
  for i in range(len(range_num)):
    if '5' in range_num[i]:
      pass 
    else:
      new_arr.append(range_num[i])
  print("Remove 5 : " ,new_arr)
  return len(new_arr)

class Vector : 
    def __init__(self , lst_vec):
        self.lst_vec = lst_vec

    def show_vector(self):
        return self.lst_vec

    def add(self , v ):
        size_self = len(self.lst_vec)
        size_v = len(v.lst_vec)
        new_vector = []
        if ( size_self != size_v ):
            return Exception("error add")
        else:
            for i in range(size_self):
                new_vector.append(self.lst_vec[i] + v.lst_vec[i])
        return Vector(new_vector)

    def subtract(self , v ): 
        size_self = len(self.lst_vec)
        size_v = len(v.lst_vec)
        new_vector = []
        if ( size_self != size_v ):
            return Exception("error subtract")
        else:
            for i in range(size_self):
                new_vector.append(self.lst_vec[i] - v.lst_vec[i])
        return Vector(new_vector)

    def dot(self , v ):
        size_self = len(self.lst_vec)
        size_v = len(v.lst_vec)
        new_vector = []
        sum_vec = 0 
        if ( size_self != size_v ):
            return Exception("Vector sizes are different")
        else:
            for i in range(size_self):
                new_vector.append(self.lst_vec[i] * v.lst_vec[i])
        for i in range(len(new_vector)):
            sum_vec+=new_vector[i]
        return sum_vec

    def norm (self):
        new_vec_sum = 0
        for i in range(len(self.lst_vec)):
            new_vec_sum +=( self.lst_vec[i] ) **2
        return new_vec_sum ** 0.5

    def toString(self):
        str_self = '('
        for i in range(len(self.lst_vec)):
            str_self += str(self.lst_vec[i])
            if i < (len(self.lst_vec)-1):
                str_self+=','
            else : pass 
        str_self+=')'
        return str_self

    def equals(self , v ):
        return self.lst_vec == v.lst_vec 


# a = Vector([1,2,3])
# b = Vector([3,4,5])
# c = Vector([5,6,7,8])
# print(a.add(b).show_vector())
# print( a.add(b).equals(Vector([4,6,8])) )
# print(a.subtract(b).show_vector())
# print(a.dot(b))
# print(a.norm())
# print((a.toString() == '(1,2,3)'))
# print(c.toString())
# print(dont_give_me_five(start=1, end=9)) 


def is_square(n):
  if  n < 0  : return False 
  elif n == 0 : return True 
  else:
    n_2 = n**0.5 
    buff_n = str(n_2)
    sq =""
    for i in buff_n:
      if i == '.':
        break 
      else:
        sq+=i 
    print(f"Num : {n} , square : {sq}")
    if n_2 == int(sq) : 
      return True 
    else:
      return False
# print(is_square(26))

# test_case = [-1 , 0 , 3 , 4 , 25 , 26]
# for i in range(len(test_case)):
#   print(i+1 , is_square(test_case[i]))


import math as m 

def solveit(vi, vf, t):
  # your code goes here
  print(vi , vf , t)
  if vi > vf : return []
  else:
      a = (vf - vi)/t
      d = vi*t + 0.5 * a * (t**2)
      # a = str(a)
      # d = str(d)
      return [round(a , 2), round(d,2)]

# print(solveit(34.5,55.1,2.47))


def modify_multiply(st, loc, num):
  new_str = st.split(" ")
  result = (new_str[loc]+'-')*num
  return result[:len(result)-1:]

# print(modify_multiply("This is a string" , 3 , 5))



''' Split string '''
def solution_split_sting(s):
  re_list = [] # result of list 

  if len(s) % 2 == 0 :
    for i in range(len(s)+1):
      if i>=2 and i % 2 == 0 :
        ss = s[i-2]+s[i-1]
        re_list.append(ss)
  else:
    for i in range(len(s)+1):
      if i>=2 and i % 2 == 0 :
        ss = s[i-2]+s[i-1]
        re_list.append(ss)
    sso = s[len(s)-1] + '_'
    re_list.append(sso)
  return re_list

# print(solution_split_sting("abcsdfgh")) 


def amount_of_pages(summary):
  buffer_str = ""
  c = 0 
  for i in range(1,summary+1):
      if len(buffer_str) == summary:
        break 
      else:
        buffer_str+=str(i)
        c=i
  return c


# print(amount_of_pages(1095))

# Next kata : https://www.codewars.com/kata/56b2abae51646a143400001d

''' IMPORT LIBRARY '''
import math as m 

def Hour_Calculator(sTOe):
  # start_time = '05:30 AM'
  # end_time   = '09:40 PM'
  start_time = sTOe[0]
  end_time = sTOe[1]
  st_type = start_time.split(" ")
  ed_type = end_time.split(" ")
  st_buffer = st_type[0]
  ed_buffer = ed_type[0]
  st_time = st_buffer.split(":") # array[0] -> hr , array[1] -> min
  ed_time = ed_buffer.split(":") # array[0] -> hr , array[1] -> min
  result_time =[]
  Case_PM = ['PM' , 'pM' , 'Pm' , 'pm']
  Case_AM = ['AM' , 'aM' , 'Am' , 'am']
  # print(st_time , st_type[1])
  # print(ed_time , ed_type[1])
  # print(st_type[1] in Case_AM , ed_type[1] in Case_PM)
  try:
    if st_type[1] in Case_PM and ed_type[1] in Case_PM: 
      result_time.append( int(ed_time[0]) - int(st_time[0]) ) # hr
      if st_time[0] > ed_time[0]:
        result_time[0] += 24 

      if int(st_time[1]) > int(ed_time[1]) : 
        result_time[0] = result_time[0] -1 
        result_time.append( 60- (int(st_time[1]) - int(ed_time[1])) )
      else:
        result_time.append( int(ed_time[1]) - int(st_time[1]) )

    elif st_type[1] in Case_AM and ed_type[1] in Case_AM:
      result_time.append( int(ed_time[0]) - int(st_time[0]) ) # hr 
      if st_time[0] > ed_time[0]:
        result_time[0] += 24 

      if int(st_time[1]) > int(ed_time[1]) : 
        result_time[0] = result_time[0] -1 
        result_time.append( 60- (int(st_time[1]) - int(ed_time[1])) )
      else:
        result_time.append( int(ed_time[1]) - int(st_time[1]) )

    elif (st_type[1] in Case_AM and ed_type[1] in Case_PM) or ( st_type[1] in Case_PM and ed_type[1] in Case_AM )  : 
      result_time.append( int(ed_time[0]) + (12 - int(st_time[0])) ) # hr 
      if int(st_time[1]) > int(ed_time[1]) : 
        result_time[0] = result_time[0] -1 
        result_time.append( 60- (int(st_time[1]) - int(ed_time[1])) )
      else:
        result_time.append( int(ed_time[1]) - int(st_time[1]) )
    # print(result_time)
    # print(f'{result_time[0]} hrs {result_time[1]} mins' , f'{result_time[0] + (result_time[1]/100)} hrs')
    return result_time[0] + (result_time[1]/100)

  except IndexError :
    return 'Can not calculate. Please check your time.'

def Hwadam(p):
  '''
  weekday : 22 $ 
  weekend : 27.5 $
  Input : [Day , hr]
 '''
  
  weekDays = ['Mon' , 'Tue' , 'Wed' , 'Thu' , 'Fri' , 'Weekday']
  weekEnd  = ['Sun' , 'Sat' , 'weekend']
  Rate = [22 , 27.5 , 33] # [Rate in weekday , Rate in weekend]
  sum = 0 
  p[1] = str(Hour_Calculator(p[1]))
  if p[0] in weekDays:
    if 1 == len(p[1]): sum += int(p[1]) * Rate[0] 
    else: sum+= (int(p[1][0]) * Rate[0] ) + ((int(p[1][2::]) * Rate[0]  ) / 60 )

  elif p[0] in weekEnd : 
    if p[0] == weekEnd[0]:
      if 1 == len(p[1]): sum += int(p[1]) *Rate[1]  
      else: sum+= (int(p[1][0]) * Rate[2]) + ((int(p[1][2::]) * Rate[2] ) / 60 )
    else:
      if 1 == len(p[1]): sum += int(p[1]) *Rate[1]  
      else: sum+= (int(p[1][0]) * Rate[1]) + ((int(p[1][2::]) * Rate[1] ) / 60 )

  print(f'(Day,Hr) : {p[0]} , {p[1]}  \t -> $ {m.floor(sum)}' )
  return m.floor(sum)

# print(Hawadum( ['Mon' , 5.45] ))

# Calculate time to money 
'''
[ 'Day' , [ 'start (AM/PM)' , 'end (AM/PM)' ], ]
'''
pay2week = [
             ['Tue' , ['04:29 PM' , '10:07 PM']] , 
             ['Wed' , ['04:29 PM' , '10:03 PM']] , 
             ['Fri' , ['04:30 PM' , '10:11 PM']] , 
             ['Sat' , ['04:39 PM' , '10:23 PM']],
             ['Sun' , ['04:29 PM' , '09:43 PM']],
            
             ['Tue' , ['04:29 PM' , '10:23 PM']],
             ['Wed' , ['04:29 PM' , '10:10 PM']],
            #  ['Fri' , ['04:30 PM' , '10:29 PM']],
            #  ['Sat' , ['04:29 PM' , '10:12 PM']],
            #  ['Sun' , ['04:00 PM' , '09:12 PM']],
            
]

# Total_sum = 0
# for i in pay2week : 
#   Total_sum += Hwadam(i)
# print(f'Total : $ {Total_sum}')



def double_char(s):
  buff = ''
  for i in range(len(s)):
    buff += s[i]*2
  return buff

# print(double_char("String"))
def fac_recursive(n):
  return 1 if (n==1 or n==0) else n * fac_recursive(n - 1)

def fac_iterative(n):
  result = 1
  for i in range(2, n + 1):
    result *= i
  return result

def zeros(n):
  # c=1
  # for i in range(2,n+1): c*=i
  # cc = 0 
  # for i in range(len(str(c))-1 , 0 , -1):
  #   # print(buff[i] , end=" ")
  #   if int(str(c)[i]) != 0 : 
  #     break
  #   else:
  #     cc+=1
  # return cc
  c = 0 
  while n!=0 :
    c+= n//5 
    n //= 5 
  return c

# print(zeros(6))



def powers_of_two(n):
    return [2**i for i in range(0,n+1)]

# print(powers_of_two(4))

sstr = '&$%'
def is_uppercase(inp):
    c = 0 
    Not = ['!' , '@' , "$" , "%" , "^" , "&" , "*" , "(" , ")" , "_" , "-" , "+"]
    for i in range(len(inp)):
      if inp[i].isupper() or inp[i] == ' ' or (inp[i] in Not):
        c+=1
    print(c , len(inp))
    return c == len(inp)

# print(is_uppercase(sstr))

board_wh = [ "8a" , "8b" , "8c" , "8d" , "8e" , "8f" , "8g", "8h",
                "7a" , "7b" , "7c" , "7d" , "7e" , "7f" , "7g", "7h",
                "6a" , "6b" , "6c" , "6d" , "6e" , "6f" , "6g", "6h",
                "5a" , "5b" , "5c" , "5d" , "5e" , "5f" , "5g", "5h",
                "4a" , "4b" , "4c" , "4d" , "4e" , "4f" , "4g", "4h",
                "3a" , "3b" , "3c" , "3d" , "3e" , "3f" , "3g", "3h",
                "2a" , "2b" , "2c" , "2d" , "2e" , "2f" , "2g", "2h",
                "1a" , "1b" , "1c" , "1d" , "1e" , "1f" , "1g", "1h",
]

path_knight = {
    "8a" : [11 , 18],
    "8h" : [14 , 23],
    "1a" : [42 , 51],
    "1h" : [47 , 54],

    "8b" : [12 , 17 , 19],
    "8g" : [13 , 22 , 24],
    "7a" : [3 , 19 , 26],
    "7h" : [6 , 22 , 31],
    "2a" : [34 , 43 , 59],
    "2h" : [39 , 46 , 62],
    "1b" : [41 , 43 , 52],
    "1g" : [46 , 48 , 53], 

    "8c" : [9 , 13 , 18 , 20] , 
    "8d" : [10 , 14 , 19 , 21],
    "8e" : [11 , 15 , 20 , 22], 
    "8f" : [12 , 16 , 21 , 23], 

    "7b" : [4 , 20 , 25 , 27],
    "7g" : [5 , 21 , 30 , 32], 

    "6a" : [2 , 11 , 27 , 34],
    "6h" : [7 , 14 , 30 , 39],
    "5a" : [10 , 19 , 35 , 42],
    "5h" : [15 , 22 , 38 , 47],
    "4a" : [18 , 27 , 43 , 50], 
    "4h" : [23 , 30 , 46 , 55],
    "3a" : [26 , 35 , 51 , 58], 
    "3h" : [31 , 38 , 54 , 63],

    "2b" : [33 , 35 , 44 , 60],
    "2g" : [38 , 40 , 45 , 61], 

    "1c" : [42 , 44 , 49 , 53],
    "1d" : [43 , 45 , 50 , 54],
    "1e" : [44 , 46 , 52 , 54], 
    "1f" : [45 , 47 , 52 , 56],
    

    "7c" : [1 , 5 , 17 , 21 , 26 , 28],
    "7d" : [2 , 6 , 18 , 22 , 27 , 29], 
    "7e" : [3 , 7 , 19 , 23 , 28 , 30], 
    "7f" : [4 , 8 , 20 , 24 , 29 , 31], 

    "6b" : [1 , 3 , 12 , 28 , 33 , 35],
    "5b" : [9 , 11 , 20 , 36 , 41 , 43],
    "4b" : [17 , 19 , 28 , 44 , 49 , 51],
    "3b" : [25 , 27 , 36 , 52 , 57 , 59],

    "6g" : [6 , 8 , 13 , 29 , 38 , 40],
    "5g" : [14 , 16 , 21 , 37 , 46 , 48],
    "4g" : [22 , 24 , 29 , 45 , 54 , 56],
    "3g" : [30 , 32 , 37 , 53 , 62 , 64],

    "2c" : [34 ,36 , 41 , 57 , 61 , 45],
    "2d" : [35 , 37 , 42 , 58 , 62 , 46],
    "2e" : [36 , 38 , 43 , 59 , 63 , 47],
    "2f" : [37 , 39 , 44 , 60 , 64 , 48],

    "6c" : [2 , 4 , 9 , 13 , 25 , 29 , 34 , 36],
    "6d" : [3 , 5 , 10 , 14 , 26 , 30 , 35 , 37],
    "6e" : [4 , 6 , 11 , 15 , 27 , 31 , 36 , 38],
    "6f" : [5 ,7 , 12 , 16 , 28 , 32 , 37 , 39],

    "5c" : [10 , 12 , 17 , 21 , 33 , 37 , 42 , 44],
    "5d" : [11 , 13 , 18 , 22 , 34 , 38 , 43 , 45],
    "5e" : [12 , 14 , 19 , 23 , 35 , 39 , 44 , 46],
    "5f" : [13 , 15 , 20 , 24 , 36 , 40 , 45 , 47],

    "4c" : [18 , 20 , 25 , 29 , 41 , 45 , 50 , 52],
    "4d" : [19 , 21 , 26 , 30 , 42 , 46 , 51 , 53],
    "4e" : [20 , 22 , 27 , 31 , 43 , 47 , 52 , 54],
    "4f" : [21 , 23 , 28 , 32 , 44 , 48 , 53 , 55],

    "3c" : [26 , 28 , 33 , 37 , 49 , 53 , 58 , 60],
    "3d" : [27 , 29 , 34 , 38 , 50 , 54 , 59 , 61],
    "3e" : [28 , 30 , 35 , 39 , 51 , 55 , 60 , 62],
    "3f" : [29 , 31 , 36 , 40 , 52 , 56 , 61 , 63],

}

path_king = {
    "8a" : [2 , 9 , 10],
    "8h" : [7 , 15 ,16],
    "1a" : [49 ,50 , 58],
    "1h" : [55 , 56 , 63],

    "8b" : [1 , 3 , 9 , 10 , 11],
    "8c" : [2 , 4 , 10 , 11 , 12],
    "8d" : [3 , 5 , 11 , 12 , 13],
    "8e" : [4 , 6 , 12 , 13 , 14],
    "8f" : [5 , 7 , 13 , 14 , 15],
    "8g" : [6 , 8 , 14 , 15 , 16],

    "7a" : [1 , 2 , 10 , 17 , 18],
    "6a" : [9 , 10 , 18 , 25 , 26],
    "5a" : [17 , 18 , 26 , 33 , 34],
    "4a" : [25 , 26 , 34 , 41 , 42],
    "3a" : [33 , 34 , 42 , 49 , 50],
    "2a" : [41 , 42 , 50 , 57 , 58],

    "1b" : [49 , 50 , 51 , 57 , 59],
    "1c" : [50 , 51 , 52 , 58 , 60],
    "1d" : [51 , 52 , 53 , 59 , 61],
    "1e" : [52 , 53 , 54 , 60 , 62],
    "1f" : [53 , 54 , 55 , 61 , 63],
    "1g" : [54 , 55 , 56 , 62 , 64],

    "7h" : [7 , 8 , 15 , 23 , 24],
    "6h" : [15 , 16 , 23 , 31 , 32],
    "5h" : [23 , 24 , 31 , 39 , 40],
    "4h" : [31 , 32 , 39 , 47 , 48],
    "3h" : [39 , 40 , 47 , 55 , 56],
    "2h" : [47 , 48 , 55 , 63 , 64],

    "7b" : [1 , 2 , 3 , 9  , 11 , 17 , 18 , 19],
    "7c" : [2 , 3 , 4 , 10 , 12 , 18 , 19 , 20],
    "7d" : [3 , 4 , 5 , 11 , 13 , 19 , 20 , 21],
    "7e" : [4 , 5 , 6 , 12 , 14 , 20 , 21 , 22],
    "7f" : [5 , 6 , 7 , 13 , 15 , 21 , 22 , 23],
    "7g" : [6 , 7 , 8 , 14 , 16 , 22 , 23 , 24],

    "6b" : [9 , 10 , 11 , 17 , 19 , 25 , 26 , 27],
    "6c" : [10 , 11 , 12 , 18 , 20 , 26 , 27 , 28],
    "6d" : [11 , 12 , 13 , 19 , 21 , 27 , 28 , 29],
    "6e" : [12 , 13 , 14 , 20 , 22 , 28 , 29 , 30],
    "6f" : [13 , 14 , 15 , 21 , 23 , 29 , 30 , 31],
    "6g" : [14 , 15 , 16 , 22 , 24 , 30 , 31 , 32],

    "5b" : [17 , 18 , 19 , 25 , 27 , 33 , 34 , 35],
    "5c" : [18 , 19 , 20 , 26 , 28 , 34 , 35 , 36],
    "5d" : [19 , 20 , 21 , 27 , 29 , 35 , 36 , 37],
    "5e" : [20 , 21 , 22 , 28 , 30 , 36 , 37 , 38],
    "5f" : [21 , 22 , 23 , 29 , 31 , 37 , 38 , 39],
    "5g" : [22 , 23 , 24 , 30 , 32 , 36 , 39 , 40],

    "4b" : [25 , 26 , 27 , 33 , 35 , 41 , 42 , 43],
    "4c" : [26 , 27 , 28 , 34 , 36 , 42 , 43 , 44],
    "4d" : [27 , 28 , 29 , 35 , 37 , 43 , 44 , 45],
    "4e" : [28 , 29 , 30 , 36 , 38 , 44 , 45 , 46],
    "4f" : [29 , 30 , 31 , 37 , 39 , 45 , 46 , 47],
    "4g" : [30 , 31 , 32 , 38 , 40 , 46 , 47 , 48],

    "3b" : [33 , 34 , 35 , 41 , 43 , 49 , 50 , 51],
    "3c" : [34 , 35 , 36 , 42 , 44 , 50 , 51 , 52],
    "3d" : [35 , 36 , 37 , 43 , 45 , 51 , 52 , 53],
    "3e" : [36 , 37 , 38 , 44 , 46 , 52 , 53 , 54],
    "3f" : [37 , 38 , 39 , 45 , 47 , 53 , 54 , 55],
    "3g" : [38 , 39 , 40 , 46 , 48 , 54 , 55 , 56],

    "2b" : [41 , 42 , 43 , 49 , 51 , 57 , 58 , 59],
    "2c" : [42 , 43 , 44 , 50 , 52 , 58 , 59 , 60],
    "2d" : [43 , 44 , 45 , 51 , 53 , 59 , 60 , 61],
    "2e" : [44 , 45 , 46 , 52 , 54 , 60 , 61 , 62],
    "2f" : [45 , 46 , 47 , 53 , 55 , 61 , 62 , 63],
    "2g" : [46 , 47 , 48 , 54 , 56 , 62 , 63 , 64],
}
def show_board(br_in):
  c = 0
  for i in range(64): 
    if c == 7 : 
        c = 0
        print(br_in[i] , end="\t") 
        print("\n")
    else: 
        c+=1
        print(br_in[i] , end="\t") 

def knight_vs_king (knight_position, king_position):
    #Three possible outputs are "Knight", "King", and "None"
    pp_knight = str(knight_position[0]) + knight_position[1].lower()
    pp_king = str(king_position[0]) + king_position[1].lower()
    
    ppp_knight = path_knight[pp_knight]
    ppp_king = path_king[pp_king]

    # transfer number of array to string 
    list_pose_knight = []
    for i in range(len(ppp_knight)):
        list_pose_knight.append( board_wh[ppp_knight[i]-1] )
    # print(list_pose_knight)

    list_pose_king = []
    for j in range(len(ppp_king)):
        list_pose_king.append( board_wh[ppp_king[j]-1] )
    # print(list_pose_king)

    if pp_knight in list_pose_king: 
        return "King"
    elif pp_king in list_pose_knight:
        return "Knight"
    else:
        return "None"

    

# print(knight_vs_king( (2, "F"), (6, "B") ) )


def knightVsKing (knightPosition, kingPosition):
    dx = knightPosition[0] - kingPosition[0]
    dy = ord(knightPosition[1]) - ord(kingPosition[1])
    d = dx * dx + dy * dy
    if d == 5: return 'Knight'
    if d < 3: return 'King'
    return 'None'

def knightVsKing (kt_pos, kg_pos):
    kt_y, kt_x = kt_pos
    kg_y, kg_x = kg_pos
    kt_x, kg_x = (ord(kt_x) - 64), (ord(kg_x) - 64)
    if kg_y - 1 <= kt_y <= kg_y + 1 and kg_x - 1 <= kt_x <= kg_x + 1:
        return "King"
    elif (
        (kg_y in (kt_y - 1, kt_y + 1) and kg_x in (kt_x - 2, kt_x + 2))
        or (kg_y in (kt_y - 2, kt_y + 2) and kg_x in (kt_x - 1, kt_x + 1))
    ):
        return "Knight"
    else:
        return "None"


def find_missing_letter(chars):
  list_result = [i for i in range(ord(chars[0])  , ord(chars[len(chars)-1])+1 )] 
  list_letter = [ord(i) for i in chars]
  for k , j in zip(list_result , list_letter):
    if k != j : 
      return chr(k)

# print( find_missing_letter( ['a' , 'b' , 'd' , 'e'] ) )

# x = [0.0, 0.19, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25]
# s = 15

def max_list(lst):
  max = lst[0]
  for i in range(len(lst)):
    if max >= lst[i]:
      pass
    else:
      max = lst[i]
  return max 

def gps (s , x):
  dis = 0 
  result = []
  if x == [] :
    return 0 
  else:
    for i in range(len(x)-1):
      # print(i+1 , i)
      dis = ((x[i+1] - x[i]) * 3600 ) / s 
      result.append(dis)
      dis = 0 
    if result == [] :
      return 0 
    else:
      return int(max_list(result))

# print(gps(s,x))



def one_two_three(n):
  ans = []
  s_num = ""
  if len(str(n)) == 1 and n!= 0 : 
    for i in range(n):
      s_num += "1"
    ans.append(n)
    ans.append(int(s_num))
  elif len(str(n)) >= 2:
    for i in range(n):
      s_num +="1"
    ss = str(n)
    # print(ss[-1] , "last")
    if ss[-1] == "0":
      last_ss = int(ss)
    else:
      last_ss = int(ss[-1])
    buffer_ss = ""
    # last_ss = 9
    for i in range(1, len(s_num)+1 , 1) : 
      if i % last_ss == 0 :
        buffer_ss+=str(last_ss)
        # buffer_ss +="9"
      elif i >= len(s_num):
        buffer_ss+=str(len(s_num)%last_ss)
    # print(buffer_ss)
    ans.append(int(buffer_ss))
    ans.append(int(s_num))
  elif n==0:
    return [0,0]

  return ans
  # print(s_num)

# print(one_two_three(14))

def count_list(l):
  buff_l = []
  index=[]
  dup=0
  for i in range(len(l)):
    for j in l:
      if j == l[i]:
        dup+=1 
    buff_l.append(dup)
    dup=0
  # print(buff_l)
  for i in range(len(buff_l)):
    if buff_l[i] ==1:
      index.append(i)
  # print(index)
  return index

def count_list(l):
  from collections import defaultdict

  counts = defaultdict(int)
  for elem in l:
    counts[elem] += 1

  return [i for i, elem in enumerate(l) if counts[elem] == 1]


# print(count_list())

def sum_no_duplicates(l):
  undup=0
  c_int = count_list(l)
  for i in c_int:
    undup+=l[i]
  return undup

# print(sum_no_duplicates(l=[1,1,2,3]))


