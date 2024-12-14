
# 1 misol
from collections import namedtuple

Sport=namedtuple('Sport',['name','sport','trophies'])

sportsmens=[
    Sport('Messi','football',49),
    Sport('Ronaldo','football',38)
]


eng_kop_yutuq =sportsmens[0]
for sportsmen in sportsmens:
    if sportsmen.trophies > eng_kop_yutuq.trophies:
        eng_katta_shahar = sportsmen

print(f"Eng ko'p yutuqga ega sportchi : {eng_kop_yutuq.name} - {eng_kop_yutuq.trophies} sovrin")



#  2 misol
a = [ 32,32,32,324,543,43,3]
b= sum(a)
c= b/len(a)
print(c)


#  3 misol
a= range(11)
a_iter=a.__iter__()
for i in a_iter:
    print(i**2)


#  4 misol
def unli_hariflar(matn):
    unli_harflar = "aeiouAEIOU"
    unlilar = [harf for harf in matn if harf in unli_harflar]
    return unlilar

matn = "Hello World,Salom dunyo"
res = unli_hariflar(matn)

print(f"Topilgan unli harflar: {res}")

# 5 misol
def generator():
    for num in range(1, 100+1):
        if num % 2 ==0:
            yield num

for i in generator():
    print(i)


# 6 misol
def fff(a):
    def ff2():
        return len(a)
    return ff2

f = fff("hello world")
f2 = f()
print( f2)

