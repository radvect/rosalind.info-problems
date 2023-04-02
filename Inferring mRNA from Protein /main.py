import Bio.Data.CodonTable
d = Bio.Data.CodonTable.standard_rna_table.forward_table

string = str(input())
count = 0
variations = 1;
for i in string:
    for item in d.values():
        if(i==item):
            count+=1
    variations *= count
    count = 0;

number_of_stop_codons = 3
variations = variations*number_of_stop_codons

print(variations%1000000)

