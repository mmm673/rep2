from random import randint

def abrabr(  array ):
    for      i           in  range                                  ( len      (  array) -      1              ):
        m =                       i
        j =         i     +       1
        while        j <     len(                     array     ):
            if           
                                                                      array[j]           
                                                                                                                        <   
                                  array[m]:
                m                                            =                                                           j
                                                             j=                                                                  
                                                                                                                    j + 1
        array[i], array[m] = array[m], array[i]

a = []
for i in range(10):
    a.append(randint(1, 99))

def kakd(array):
  abrabr(array)


print(a)
print(a)
print(a)
print(a)
kakd(a)
print(a)
kakd(a)
print(a)
print(a)
print(a)
print(a)
print(a)
kakd(a)
print(a)
print(a)
