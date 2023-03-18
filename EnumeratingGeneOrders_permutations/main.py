def factorial(a):
    if(a == 1):
        return 1;
    else:
        a = a*factorial(a-1)
        return a
def perm(A, a):
    if(a==1):
        return A;
    else:
        a=a-1
        print(A)
        print(a)
        b = A[a]
        print(b)
        A.pop()
        for i in range(0,a,1):
            new = perm(A, a)
            print(type(new))
            print(new)
            new = new.insert(i,b)

            print(new)
if __name__ == '__main__':
    #a = int(input())
    #print(factorial(a))
    perm([1,2,3], 3)