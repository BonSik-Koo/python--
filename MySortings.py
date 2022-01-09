#선택정렬
def selectionSort(L):
    size=len(L)
    for i in range(size-1):
        min_index=i
        for j in range(i+1,size):
            if L[min_index] > L[j]:
                min_index=j
        if min_index!=i:
            L[min_index],L[i]= L[i],L[min_index]

#병합정렬
def mergeSort(L):
    if len(L) < 2:
        return L
    else:
        middle=len(L)//2
        L_left=mergeSort(L[:middle]) #원소가 하나만 남을때 까지 분할
        L_right=mergeSort(L[middle:])
        return merge_sort(L_left, L_right) #분할 시킨 두 원소들을 차례로 병합

def merge_sort(L_left,L_right):
    i,j=0,0
    len_left,len_right = len(L_left), len(L_right)
    L_result=[]

    while i<len_left and j<len_right:
        if(L_left[i] < L_right[j]):
            L_result.append(L_left[i])
            i+=1
        else :
            L_result.append(L_right[j])
            j+=1

    while i<len_left: #남은 원소가 있으면 차례로 list에 삽입
        L_result.append(L_left[i])
        i+=1
    while j<len_right: #남은 원소가 있으면 차례로 list에 삽입
        L_result.append(L_right[j])
        j+=1
    return L_result
