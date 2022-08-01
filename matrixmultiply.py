import  numpy as np
class solution:
    def __init__(self,Matrix1=None,Matrix2=None):
        self.M1 = Matrix1
        self.M2 = Matrix2
    def DC(self,M,N):
        if len(M) <2:
            return M*N
        index = int(len(M)/2)
        M1 = M[:index,:index]
        M2 = M[:index,index+1:]
        M3 = M[index+1:,:index]
        M4 = M[index+1:,index+1:]

        N1 = N[:index, :index]
        N2 = N[:index, index + 1:]
        N3 = N[index + 1:, :index]
        N4 = N[index + 1:, index + 1:]

        C1=self.DC(M1,N1)+self.DC(M2,N3)
        C2=self.DC(M1,N2)+self.DC(M2,N4)
        C3=self.DC(M3,N1)+self.DC(M4,N3)
        C4 = self.DC(M3, N2) + self.DC(M4, N4)

        return np.vstack((np.hstack((C1,C2)),np.hstack((C3,C4))))
    def matrixmultiply(self):
        print(self.DC(self.M1,self.M2))

a=np.array([1,2,3,4]).reshape(2,2)
b=np.array([1,2,3,4]).reshape(2,2)
t=solution(a,b)
t.matrixmultiply()


