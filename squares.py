__author__ = 'onur'

sonuc1, sonuc2 = 0, 0

counter = 100

for x in range (1, counter+1):

    sonuc1 += x

    sonuc2 += pow (x, 2)

sonuc1 = pow (sonuc1, 2)

totale = sonuc1 - sonuc2

print ("%d" % totale)

print ("%d %d" % (sonuc1, sonuc2))


