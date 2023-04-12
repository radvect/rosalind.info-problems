def Transcription(s):
    transcript = ""
    for i in s:
        if(i=="A"):
            transcript+="T"
        elif (i == "T"):
            transcript += "A"
        elif (i == "C"):
            transcript += "G"
        elif (i == "G"):
            transcript += "C"
    return transcript
