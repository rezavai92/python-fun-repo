import random
def generateCode ():
    while(1):
        omap={}
        initialGuess = str(random.randint(1,999))
        for a in initialGuess:
            if a in omap:
                omap[a]+=1
            else :
                omap[a]=1
        track=0
        for entry in omap:
            if(omap[entry])==1:
                track+=1
        if (track==3):
            return initialGuess
            break

    


#print(generateCode())

guess = generateCode()
print("guess is " , guess)

def generateClue(guessedNumber):
    s1=guess
    
    s2 = str(guessedNumber)
    f_number = s1[0]
    s_number=s1[1]
    t_number =s1[2]

    if( (f_number not in s2) and (s_number not in s2) and (t_number not in s2) ):
        return "Nope"

    elif (f_number ==s2[0] or s_number==s2[1] or t_number==s2[2] ) :
        return "Match"

    return "Close"



while(1):
    userGuess = int(input("guess a 3 digit number!"))
    if(userGuess==int(guess) ):
        print("congrats!")
        break
    else :
        print(generateClue(userGuess))