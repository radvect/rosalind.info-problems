from Bio.Seq import Seq

def translation(DNA_spliced):
    protein = Seq("")
    for i in range(0,len(DNA_spliced),3):
        triplet = ""
        for j in range(0, 3):
            triplet += DNA_spliced[j+i]
        amino = Seq(triplet).translate()

        protein = protein + amino
    return protein