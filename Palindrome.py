__author__ = 'onur'


sonuc = 0
for i in range (999, 100, -1):
    for j in range (999, 100, -1):
        carpim = i * j
        string = str(carpim)
        string1 = string[0:3]
        string2 = string[3:6]
        string2 = string2 [::-1]
        if string1 == string2:
            #print ("%s %s" % (string1,string2))
            if carpim > sonuc:
                sonuc = carpim
print ("%d" % sonuc)