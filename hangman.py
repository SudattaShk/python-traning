word=str(input("enter a word: "))

chance =5

for i in range (len(word)):
    for j in range (i):
        print("_")

while chance>0:
    
    guess=str(input("guess the word or a letter: "))
    
    avai =word.find(guess)

    print (avai)


    if avai== -1:
        chance-=1
        print("The Letter is not in the word")


    else : 
        print("The Letter is in the word")
        avai+=1 


