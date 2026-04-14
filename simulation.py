import numpy as np

datafile = open("data.txt",'a') #open file to write data to

dicenum = 25 #number of dice
outputoccurences=[0,0,0,0,0,0,0,0,0,0,0,0] #placeholder totals for dic
simcount=0#number of sims completed
simswanted =1 #simiulations wanted

for x in range(simswanted):

    # genorate randome numberss bertween 1 and six and count tthem
    dice2 = np.random.randint(1,7, size=(dicenum))
    tots = np.bincount(dice2, minlength=7)[1:]

    print(dice2)
    print(tots)

    totals = np.array([3,5,6,1,2,3,4,8,5,9,4,3]) #getTotals() <-- yet to come funtion
    outputoccurences += totals
    simcount+=1
    # print(str(outputoccurences)+"\n") #print data to console
    datafile.write(str(outputoccurences)+"\n") #write data to file