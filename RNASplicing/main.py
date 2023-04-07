import FASTA_OPEN
import Translation
from Bio.Seq import Seq
def comparison_sequances_for_nucleo(main, splice, index):
    if(len(splice)>len(main)-index):
        return False
    for i in splice:
        if(i != main[index]):
            return False
        else:
            index = index +1
    return True


if __name__ == '__main__':
    DNA_spliced = ""
    fasta_list=FASTA_OPEN.open_fasta_as_list("DNA.fasta")
    main_seq = fasta_list[0]
    i = 0
    while (i<len(main_seq)):
        iter =0
        for j in range(1,len(fasta_list)):
            if(comparison_sequances_for_nucleo(main_seq,fasta_list[j], i)):
                l = len(fasta_list[j])
                i = i+l-1
                iter=1
                break
        if(iter==0):
            DNA_spliced+=main_seq[i]
            iter = 0
        i = i +1

    print(Translation.translation(DNA_spliced[:-3]))

    # protein = Translation.translation(DNA_spliced)
    #
    # print(protein)