import random
def genData():
    toPrint=''
    dat=input('how many lines?\n')
    dataNum=int(dat)
    for i in range(0,dataNum):
        store=2*i
        rando=random.randint(store-1, store+1)
        toPrint=toPrint+str(rando)+" "
    return toPrint
print(genData())
