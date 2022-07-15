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

a = Vector([1,2,3])
b = Vector([3,4,5])
c = Vector([5,6,7,8])
print(a.add(b).show_vector())
print( a.add(b).equals(Vector([4,6,8])) )
print(a.subtract(b).show_vector())
print(a.dot(b))
print(a.norm())
print((a.toString() == '(1,2,3)'))
print(c.toString())
