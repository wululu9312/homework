import re
import sys

flag=1
#n=input()
n=sys.argv[1]
countError=0
set1=set()
list2=[]

if len(n)<8:
    ans='長度少於8'
    set1.add(ans)
    
    flag=0

if len(n)>16:
    ans='長度大於16'
    set1.add(ans)
    
    flag=0 

if re.search('[A-Z]',n) is None:   
    ans='缺少字母大寫'
    set1.add(ans)
    
    flag=0

if re.search('[0-9]',n) is None:
    ans='缺少數字'
    set1.add(ans)
    
    flag=0

if re.search('\W',n) is None:
    if re.search('_',n) is None:
        ans='缺少符號'
        set1.add(ans)
        
        flag=0

for i in range(len(n)):
    list2.append(int(ord(n[i])))
#print('{}'.format(list2))
for i in range(len(list2)-1):
    if list2[i+1]-list2[i]==1 or list2[i+1]-list2[i]==-1:
        flag=0
        if 65<=list2[i+1]<=90 and 65<=list2[i]<=90:
            ans='大寫字母連續'
            set1.add(ans)
            
        elif 97<=list2[i+1]<=112 and 97<=list2[i]<=112:
            ans='小寫字母連續'
            set1.add(ans)
            
        elif 48<=list2[i+1]<=57 and 48<=list2[i]<=57:
            ans='數字連續'
            set1.add(ans)
            

if flag==1:
    print('Success')
else:
    print('Fail')
    #print(set1)
    for i in set1:
        print(i)
