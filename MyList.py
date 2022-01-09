import random
def genRandList(L, size):
    for i in range(size):
        L.append(i)
    random.shuffle(L)
    
def shuffleList(L):
    random.shuffle(L)

def printListsample (L , per_line, sample_lines):
    count =0
    size = len(L) 
    for i in range(0, sample_lines): 
        s = ""
        for j in range(0, per_line): 
            if count > size:
                break
            s += "{0:>7} ".format(L[count]) 
            count += 1
        print(s) 
        if count >= size:   
            break

    if count < size:
        print('. . . . . .')
        if count <= (size - per_line * sample_lines):
            count = size - per_line * sample_lines 
            for i in range(0, sample_lines): 
                s = ""
                for j in range(0, per_line):
                    if count >= size:
                        break
                    s += "{0:>7} ".format(L[count])
                    count += 1
                print(s) 
                if count >= size:
                    break

L=[]
if __name__=="__main__":
    genRandList(L, 100)
    printListsample(L , 10 ,5)


