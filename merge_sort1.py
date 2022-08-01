import  math
import time
class mergesort:
    def __init__(self,arr=None):
        self.A=arr
    def merge(self,l,r):
        l_len=len(l)
        r_len=len(r)
        num=l_len+r_len
        M=max(max(l),max(r))
        l.append(M+1)
        r.append(M+1)
        i=0
        j=0
        result=[None]*num
        for k in range(num):
            if l[i]<=r[j]:
                result[k]=l[i]
                i+=1
            else:
                result[k]=r[j]
                j+=1
        return result
    def m_s(self,arr):
        if len(arr)<2:
            return arr
        else :
            mid=math.ceil(len(arr)/2)
            left=arr[:mid]
            right=arr[mid:]
            return self.merge(self.m_s(left),self.m_s(right))

    def merge_sort(self):
        print(self.m_s(self.A))

start_time = time.time()
a=mergesort([1,2,3,2,3,4])
a.merge_sort()
print('time consume:',time.time()-start_time)
