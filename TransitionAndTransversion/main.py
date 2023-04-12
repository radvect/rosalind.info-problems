import FASTA_OPEN


def TransitionAndTransversion(s1,s2):
    transition = 0;
    transversion = 0;

    for i in range(len(s1)):
        if(s1[i]=="A" and s2[i]!="A"):
            if(s2[i]=="G"):
                transition+=1
            else:
                transversion+=1
        elif(s1[i]=="G" and s2[i]!="G"):
            if(s2[i]=="A" or s2[i]=="G"):
                transition+=1
            else:
                transversion+=1
        if (s1[i] == "T" and s2[i]!="T"):
            if (s2[i] == "T" or s2[i] == "C"):
                transition += 1
            else:
                transversion += 1
        elif (s1[i] == "C" and s2[i]!="C"):
            if (s2[i] == "T" or s2[i] == "C"):
                transition += 1
            else:
                transversion += 1
    return transition/transversion


seq = FASTA_OPEN.open_fasta_as_list("transition_transversion.fasta")
print(TransitionAndTransversion(seq[0],seq[1]))

