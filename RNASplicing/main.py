import FASTA_OPEN

def comparison_sequances_for_nucleo(main, splice, index):
    for i in splice:
        if(i != main[index]):
            return False
        else:
            index = index +1
    return True


if __name__ == '__main__':
    FASTA_OPEN.open_fasta_as_list("DNA.fasta")