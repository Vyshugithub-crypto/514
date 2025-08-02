class Solution:
    def frequencySort(self,s:str)->str:
        d={}
        for i in s:
            if(i in d):
                d[i]=d[i]+1
            else:
                d[i]=1
        s_d=sorted(d.items(),key=lambda x:-x[1])
        resultString=""
        for key, value in s_d:
            for i in range(value):
                resultString+=key
        return resultString
