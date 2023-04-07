import FASTA_OPEN

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
    fasta_list=FASTA_OPEN.open_fasta_as_list("DNA.fasta")
    main_seq = fasta_list[0]
    for i in range(len(main_seq)):
        for j in range(1,len(fasta_list)):
            if(comparison_sequances_for_nucleo(main_seq,fasta_list[j], i)):
                main_seq = main_seq[:i]
                i =0
    print(main_seq)