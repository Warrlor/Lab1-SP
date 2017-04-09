import math
m = 5.7
p = int(input('введите p '))
t = math.sin(math.pow(m,3))
print ('t=',t)
x = (math.pow(p,2))+t
print ('x=',x)
y = math.log10(math.fabs(x+t))
print ('y=',y)
