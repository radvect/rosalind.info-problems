import functools

import FASTA_OPEN
def biggest(A,T,C,G):
    if(A>=T and A>=C and A>=G):

        return 1
    elif (T >= A and T >= C and T >= G):

        return 2
    elif (C >= A and C >= T and C >= G):

        return 3
    elif (G >= A and G >= T and C <= G):

        return 4
if __name__ == '__main__':
    input_file = "ConsensusAndProfile.fasta"
    list_seq = FASTA_OPEN.open_fasta_as_list(input_file)
    A = [0 for i in range(len(list_seq[0]))]
    T = [0 for i in range(len(list_seq[0]))]
    C = [0 for i in range(len(list_seq[0]))]
    G = [0 for i in range(len(list_seq[0]))]

    for i in list_seq:
        for j in range(len(i)):
            if(i[j]=="A"):
                A[j] = A[j]+1
            if (i[j] == "T"):
                T[j] = T[j] + 1
            if (i[j] == "C"):
                C[j] = C[j] + 1
            if (i[j] == "G"):
                G[j] = G[j] + 1
    final_seq = ""
    for i in range(len(list_seq[0])):
        ind = biggest(A[i],T[i],C[i],G[i])
        match ind:
            case (1):
                final_seq = final_seq + "A"
            case (2):
                final_seq = final_seq + "T"
            case (3):
                final_seq = final_seq + "C"
            case (4):
                final_seq = final_seq + "G"

    with open(("result.txt"), "w") as f:
        f.write(final_seq + "\n")
        a = " ".join(map(str, A))
        f.write("A: " + a + "\n")
        c = " ".join(map(str, C))
        f.write("C: " + c + "\n")
        g = " ".join(map(str, G))
        f.write("G: " + g + "\n")
        t = " ".join(map(str, T))
        f.write("T: " + t )
