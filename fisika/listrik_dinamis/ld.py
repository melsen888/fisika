print ("========================")
print ("")
print ("1)Kuat Arus Listrik")
print ("2)Hambatan Kawat Penghantar")
print ("3)Gaya Gerak Listrik")
print ("")
menu = int(input("pilih menu : "))


if menu == 1 :
    print ("")
    print ("Dik")
    print ("")

    q = int(input("muatan listrik : "))
    t = int(input("waktu :"))

    print ("")
    print ("Kuat arus listrik",q/t,"A" )

if menu == 2 :
    print ("Dik")
    print ("")
    
    p = int(input("Hambatan Jenis : "))
    i = int(input("Panjang Kawat : "))
    a = int(input("Luas Penampang Kawat : "))

    print ("")
    print ("Hambatan Kawat ",p*i/a,"Ohm")

if menu == 3 :
    print ("")
    print ("1)Rangkaian Batrai Seri")
    print ("2)Rangkaian Batrai Pararel")

    print ("")
    ggl = int(input("pilih menu :"))

    if ggl == 1 :
        print ("")
        print ("Dik")
        print ("")

        n = int (input("banyaknya batrai : "))
        e = int (input("GGL / V : "))
        r = int (input("Hambatan dalam : "))
        rt = int (input("Hambatan Luar : "))

        # 

        ne = n*e
        nr = n*r
        total = rt+nr
        print ("")
        print("Kuat arus total yang mengalir kerangkaian",ne/total,"(A)")
        print ("")
    
    if ggl == 2 :
        print ("")
        print ("Dik")
        print ("")

        n = int (input("banyaknya batrai : "))
        e = int (input("GGL / V : "))
        r = int (input("Hambatan dalam : "))
        rt = int (input("Hambatan Luar : "))

        # 
        rn = r/n
        total = rt+rn
        print("Kuat arus total yang mengalir kerangkaian",e/total,"(A)")







# @melsen888
