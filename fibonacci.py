__author__ = 'onur'

#Fibonacci

value1 = 1
sonuc=0
eski_toplam=0
eski_toplam2=1

sum=0

for index in range(4000000):

    if (sum<4000000):

        yeni_toplam = eski_toplam + eski_toplam2
        #print (yeni_toplam)

        eski_toplam2 = eski_toplam

        eski_toplam = yeni_toplam

        if yeni_toplam % 2 == 0:
            sum=sum+yeni_toplam

print (sum)


