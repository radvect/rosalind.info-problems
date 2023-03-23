import math

if __name__ == '__main__':
    seq = str(input())
    AT = 0;
    CG = 0
    for i in seq:
        if(i=="A" or i=="T"):
            AT +=1
        else:
            CG+=1
    print(AT)
    print(CG)
    probabilities_CG = [float(x) for x in input().split()]
    for i in probabilities_CG:
        prob_C_or_G = i/2
        prob_A_or_T= (1-i)/2
        print(round(math.log10(prob_A_or_T**AT * prob_C_or_G**CG),3), sep = " ",end=' ', flush=True)