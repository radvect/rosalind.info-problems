import FASTA_OPEN
def FindingaSplicedMotif(s1,s2):
    index = 0
    i = 0
    indexesofMotif = []
    while(index!=len(s2)):
        symb = s1[i]
        if(symb == s2[index]):
            indexesofMotif.append(i+1)
            index=index+1
        i = i + 1
    listToStr = ' '.join(map(str, indexesofMotif))
    return listToStr


seq = FASTA_OPEN.open_fasta_as_list("Spliced_Motif.fasta")
print(FindingaSplicedMotif(seq[0],seq[1]))