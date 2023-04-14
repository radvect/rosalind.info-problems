import sys
import copy

import FASTA_OPEN
import TranscribingDNAintoRNA.main
from TranscribingDNAintoRNA import main

def reversePalindrom(s):
    a = main.Transcription(s)
    a = a[::-1]
    if(s == a):
        return True
    else:
        return False

def LocationRestrictionSites(s):
    print(s)

    i = 0
    while(i<len(s)):
        lim = 12
        if(len(s)-i<12):
            lim = len(s)-i
        for j in range(4,lim+1,2):

            sub = s[i:i+j]
            if(reversePalindrom(sub)):
                print(str(i+1) + " " + str(j))
        i = i+1

a = FASTA_OPEN.open_fasta_as_list("LocatingRestrictionSites.fasta")
LocationRestrictionSites(a[0])