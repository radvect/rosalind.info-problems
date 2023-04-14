import sys


import FASTA_OPEN
from TranscribingDNAintoRNA import main
def LocationRestrictionSites(s):
    a = ""
    a = main.Transcription(s)
    a = a[::-1]
    i = 0
    d = {}
    while(i<len(s)):
        l = 0

        nexti = i+1
        if(nexti>len(s)-1):
            break
        if(s[i] == a[i]):
            if(s[nexti] == a[nexti]):
                l = 2
                indexofpal = i
                while(s[i]!=a[i] and l<12 and i<len(s)):
                    i = i+1
                    l = l+1
                d[indexofpal] = l

        else:

            i = i+1
    print(d)

a = FASTA_OPEN.open_fasta_as_list("LocatingRestrictionSites.fasta")
LocationRestrictionSites(a[0])