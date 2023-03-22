class vector:
    def __init__(self , coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimention = len(coordinates)
        except ValueError:
            raise ValueError('The coordinate must be nonempty')
        except TypeError:
            raise TypeError('The coordinate must be an iterable')

    def __str__(self) -> str:
        return 'Vector : {} , Dim : {}'.format(self.coordinates,self.dimention)
    
    def __eq__(self, v ):
        return self.coordinates == v.coordinates
    
v1 = vector([1,2,3,4])
v2 = vector([1,2,3])
print(v1 , v2)
print("Are we equal? : " ,v1 == v2)
        