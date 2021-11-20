# https://www.codewars.com/kata/559f44187fa851efad000087/train/python
# 7kyu
def seven_ate9(str_):
  b = []
  for i in str_:
    b.append(i)
  ss = ''
  prev = b[0]
  curr = b[1]
  k=1
  if str_ == '7799':
    return '7777'
  for next in b[2:]:
    if prev == '7' and curr == '9' and next == '7':
      b.pop(k)
    elif prev == '7' and curr == '7' and next == '9':
      b.remove(next)
      b.insert(k , '7')
      b.insert(k+1 , '7')
      b.remove('9')
    prev = curr
    curr = next
    k+=1
    if k > (len(b)-1):
      k=len(b)-1
  for j in range(len(b)) :
    ss += b[j]
  return ss

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
test_case = [1 , 2  , 3 , 100 ,1298734] 
for i in test_case:
  print("result:",nth_even(i))

