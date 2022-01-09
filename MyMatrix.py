def printMtrx (M):
    for i in range(len(M)):  #행렬의 행개수만큼
        s=""
        for j in range(len(M[0])): #행렬의 열 개수 만큼
            s+= "{:4}".format(M[i][j])
        print(s)

def mtrxAdd(A,B):
    L_result=[] #mtrx 덧셈 결과를 담아주는 리스트 생성
    a_row, a_col= len(A), len(A[0])
    b_row, b_col= len(B), len(B[0])
    
    if a_row!=b_row and a_col!=b_col:
        print("add: row, col not match!!!!")
        return 0
    else:
        for i in range(a_row):
            L_temp=[]
            for j in range(b_col):
                L_temp.append(A[i][j] + B[i][j]) #기준 행에 있는 열의 덧셈 결과를 list로 저장 
            L_result.append(L_temp) #list에 list을 넣어주면서 2차원 결과 list를 2차원 list로 만들어준다.

        return L_result

def mtrxSubtract(A,B):
    L_result=[] #mtrx 덧셈 결과를 담아주는 리스트 생성
    a_row, a_col= len(A), len(A[0])
    b_row, b_col= len(B), len(B[0])

    if a_row!=b_row and a_col!=b_col:
        print("sub: row, col not match!!!!")
        return 0
    else:
        for i in range(a_row):
            L_temp=[]
            for j in range(b_col):
                L_temp.append(A[i][j] - B[i][j]) #기준 행에 있는 열의 뺄셈 결과를 list로 저장 
            L_result.append(L_temp) #list에 list을 넣어주면서 2차원 결과 list를 2차원 list로 만들어준다.

        return L_result

def mtrxMultiply(A,B):
    L_result=[] #mtrx 덧셈 결과를 담아주는 리스트 생성
    a_row, a_col= len(A), len(A[0])
    b_row, b_col= len(B), len(B[0])

    if a_col!=b_row:
        print("Mult: row, col not match!!!!")
        return 0
    else:
        for i in range(a_row):
            L_temp=[]
            for j in range(b_col):
                mult_result=0
                for k in range(a_col):
                    mult_result+=A[i][k] * B[k][j]
                L_temp.append(mult_result) #기준 행에 있는 열의 곱셈 결과를 list로 저장 
            L_result.append(L_temp) #list에 list을 넣어주면서 2차원 결과 list를 2차원 list로 만들어준다.

        return L_result
