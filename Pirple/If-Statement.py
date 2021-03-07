def compareThree(a,b,c):
    if a == b and a == c:
        print("The three values are same")
    elif a == b and a > c:
        print("{} 'n' {} are same and higher than {}".format(a,b,c))
    elif a == c and a > b:
        print("{} 'n' {} are same and higher than {}".format(a,c,b))
    elif b == c and b > a:
        print("{} 'n' {} are same and higher than {}".format(b,c,a))
    elif a > b and a > c:
        print("{} is higher than {} 'n' {}".format(a,b,c))
    elif b > a and b > c:
        print("{} is higher than {} 'n' {}".format(b,a,c))
    else :
        print("{} is higher than {} 'n' {}".format(c,a,b))


compareThree(1,1,1) #All are same

compareThree(3,3,1) 

compareThree(2,1,2)

compareThree(1,8,8)

compareThree(3,2,1)

compareThree(1,3,2)

compareThree(1,2,3)

compareThree(5,int("5"),6)

def AreSame(a,b,c):

    if a == b and b == c:
        print(True)
        print("The three values are same {}, {} and {}".format(a,b,c))
    elif a == b:
        print(True)
        print("Two valus are same {} and {}".format(a,b))
    elif a == c:
        print(True)
        print("Two valus are same {} and {}".format(a,c))
    elif b == c:
        print(True)
        print("Two valus are same {} and {}".format(b,c))
    else:
        print(False)
        print("The three values are different {}, {} and {}".format(a,b,c))
    

AreSame(1,1,1)
AreSame(2,2,3)
AreSame(3,4,3)
AreSame(4,5,5)
AreSame(1,2,3)
AreSame(5,int("5"),6)









