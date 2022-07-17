#PYTHON 3
import re
N = int(input()) #INPUT
for i in range(N):
    if re.match(r'[789]\d{9}$',input()):   #matching first digit with 7,8 or 9
        print('YES')  
    else:  
        print('NO')
