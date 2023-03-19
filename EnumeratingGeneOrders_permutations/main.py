def factorial(a):
    if(a == 1):
        return 1;
    else:
        a = a*factorial(a-1)
        return a
def swap(list, i,j): #function changing elements by indexes
    new_list = [i for i in list] #deepcopy
    a = list[i]
    b = list[j]
    new_list[i]=b
    new_list[j]=a
    return new_list

def perm(A, a):
    if(a==0):
        print(*A, sep=" ")
    else:
        for i in range(0,a,1):
            list = swap(A, i,a-1)
            perm(list, a-1)

if __name__ == '__main__':
    a = int(input())
    print(factorial(a))
    list = [i for i in range(1,a+1,1)]
    perm(list, len(list))