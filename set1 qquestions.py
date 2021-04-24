def ques1():
    def vowel_r_cons():
        i=input('')
        vowels=['a','e','i','o','u','A','E','I','O','U']
        if i in vowels:
            print(i," is a vowel")
        elif i not in vowels:
            print(i," is a consonant")
    vowel_r_cons(a)



    def ASCII():
        s=input()
        print('the ASCII value of ',ord(s))
    ASCII()



    s=int(input())
    c=0
    z=str(s)
    for i in z:
        c=c+1
    print(c)






    def fact():
        s=int(input())
        mul=1
        for i in range(2,s+1):
            mul=mul*i
        print(mul)
    fact()



    def fabonaccis():
        n=int(input())
        x=0
        y=1
        print(x)
        print(y)
        for i in range(3,n+1):
            b=x+y
            print(b)
            x=y
            y=b
    fabonaccis()





    def pos_r_neg():
        n=int(input())
        if (n<0):
            print(n,"'it's a negative num")
        elif (n==0):
            print(n," is either postive nor negative")
        else:
            print(n,"it's a positive num")
    pos_r_neg()




    def even_r_odd():
        n=int(input())
        if (n%2==0):
            print(n,'is a even num')
        else:
            print(n,'is a odd num')
    even_r_odd()




    def area_of_circle():
        r=int(input())
        pi=3.14
        A=pi*r**2
        print('area of circle is',A)
    area_of_circle()
    
    def area_of_triangle():
        h=int(input())
        b=int(input())
        A=(b*h)/2
        print('area of triangle is',A)
    area_of_triangle()



    def area_of_rectangle():
        w=int(input())
        l=int(input())
        A=w*l
        print(A)
    area_of_rectangle()


    def sum_of_digit():
        n=input()
        c=0
        for i in n:
            q=int(i)
            c=c+q
        print(c)
    sum_of_digit()




    def sum_of_n_num():
        n=int(input())
        c=0
        for i in range(1,n+1):
            c=c+i
        print(c)
    sum_of_n_num()



    def sum_of_range():
        s=int(input())
        e=int(input())
        c=0
        for i in range(s,e+1):
            c=c+i
        print(c)
    sum_of_range()




    def reverse_num():
        s=input()
        k=[]
        for i in s:  
            k.append(i)
        k.reverse()
        for i in k:
            print(i,end='')
    reverse_num()



    def strong_num():
        n=input()
        u=int(n)
        c=0
        for j in n:
            v=int(j)
            mul=1
            for i in range(2,v+1):
                mul=mul*i
            c=c+mul
            print(c)
        if (u==c):
            print(n,' is a strong number')
        else:
            print(n,' is a not strong number')
    strong_num()


   
    def perfect_num():
        n=int(input())
        c=0
        for i in range(1,int(n/2+1)):
            if n%i==0:
                c=c+i
                print(c)
            else:
                continue
        if (c==n):
            print(n,' is a perfect number')
        else:
            print(n,' is a not perfect')
    perfect_num()



    def power_of_num():
        base_n=int(input())
        power_n=int(input())
        c=0
        f=base_n*base_n
        for i in range(1,power_n-1):
            c=c+1
            if c!=power_n:
                f=f*base_n
            else:
                break
        print(base_n," power ",power_n," is ",f)
    power_of_num()




    def factors_of_num():
        n=int(input())
        c=1
        for i in range(1,n+1):
            if n%i==0:
                if i!=n:
                    c=c+1
                    print(i,end=',')
                else:
                    print(i)
            else:
                continue
            
            
        print('\nthere are ',c,'factor numbers')
    factors_of_num()



    def add_frac(n1,n2,n3,n4):
        f1=n1/n2
        f2=n3/n4
        f=f1+f2
        print(f)
    add_frac(1,2,1,2)



    def armstrong():
        n=int(input())
        n1=str(n)
        c=0
        f1=0
        for i in n1:
            c=c+1

        for i in n1:
            h=int(i)
            f=h**c
            f1=f1+f

        if f1==n:
            print(n,' is a armstrong num')
        else:
            print(n,' is not a armstrong num')
    armstrong()



    def greatest_num(n1,n2,n3):
        if n1>n2 and n1>n3:
            print(n1,' is a large num')
        elif n2>n3:
            print(n2,' is a large num')
        else:
            print(n3,' is a large num')
    greatest_num(87,848,94748)



    def leap_year(n):
        if n>=2000:
            if n%4==0:
                print(n,' is a leap year')
            else:
                print(n,'is not a leap year')
    leap_year(2002)




    def prime_num(n):
        c=0
        if n==2:
            print(n,' prime num')

        if n%2==0 and n!=2:
            print(n,' not prime num')
        if n%2==1:
            for i in range(1,n+1):
                if n%i==0:
                    c=c+1
            if c>2:
                print(n,' is not prime')
            else:
                print(n,' is prime num')
    prime_num(5)




