



if __name__ == '__main__':
    name = ""
    with open("ConsensusAndProfile.txt", 'r') as f:
        list_of_seq = f.read().split(">")
    for i in list_of_seq:
        i = i.replace('\n', '')
        if (len(i) == 0):
            continue
        lenseq = len(i) - 13
        for j in range(len(i)):

            if (i[j] == 'A'):

            if (i[j] == 'T'):

            if (i[j] == 'C'):

            if (i[j] == 'G'):


        percent_curr = counterGC / lenseq * 100
        counterGC = 0
        if (percent_curr > percent):
            percent = percent_curr
            name = i[0:13]
            leng = lenseq
            i_curr = i