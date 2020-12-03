import re
import sys

flag=1
#n=input()
n=sys.argv[1]
countError=0
list1=[]

if len(n)<8:
    ans='長度少於8'
    list1.append(ans)
    countError+=1
    flag=0

if len(n)>16:
    ans='長度大於16'
    list1.append(ans)
    countError+=1
    flag=0 

if re.search('[A-Z]',n) is None:   
    ans='缺少字母大寫'
    list1.append(ans)
    countError+=1
    flag=0

if re.search('[0-9]',n) is None:
    ans='缺少數字'
    list1.append(ans)
    countError+=1
    flag=0

if re.search('\W',n) is None:
    if re.search('_',n) is None:
        ans='缺少符號'
        list1.append(ans)
        countError+=1
        flag=0

if flag==1:
    print('Success')
else:
    print('Fail')
    for i in range(countError):
        print('{}'.format(list1[i])) 
