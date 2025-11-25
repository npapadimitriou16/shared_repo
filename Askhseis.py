"""def whatVowels(s):
    listf = "aeiou"  
    for i in s:
        if i in listf:
            print(i ,end = '')

s = "ti leei file"
whatVowels(s)"""

def wordScore(s):
    counterf = 0
    listf = "aeiou"
    lists = "mry"
    for i in s:
        if i in listf:
            counterf=counterf + 2
        if i in lists:
            counterf=counterf + 3
        else:
            counterf += 1
    return counterf

s = "ame"
print(wordScore(s))
        

        
