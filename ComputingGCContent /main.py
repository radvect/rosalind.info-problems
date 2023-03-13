










if __name__ == '__main__':
    name = ""
    percent = 0
    counterGC=0
    lenseq = 0
    with open("GC_genoms.txt", 'r') as f:
        list_of_seq = f.read().split(">")
    for i in list_of_seq:
        i = i.replace('\n', '')
        if(len(i)==0):
            continue
        lenseq = len(i) - 13

        for j in range(len(i)):

            if (i[j] == 'C' or i[j] == 'G'):
                counterGC += 1

        percent_curr = counterGC/lenseq*100
        counterGC = 0
        if(percent_curr>percent):
            percent = percent_curr
            name = i[0:13]
            leng = lenseq
            i_curr = i

    print(name)
    print(percent)
