__author__ = 'onur'

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

def AsalSayi (sayi, kontrol = 0, asallik = 0):
    for i in range (2, sayi):
        kontrol = 0
        if sayi % i == 0:
            #print("%d asal degil" % sayi)
            asallik = 0
            break
        else:
            kontrol += 1
    if kontrol != 0:
        #print("%d asaldir" % sayi)
        asallik = 1
    return asallik

array = []

#print("%d" % AsalSayi(5))

baslangic = 1
x = 0

while 1:
    baslangic += 1
    if (AsalSayi(baslangic)) == 1:
        #array.append(baslangic)
        x += 1
        print("%d" % x)


    if x == 10000:
        print("%d" % baslangic)
        break
