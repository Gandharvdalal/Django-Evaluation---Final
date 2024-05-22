#create a variable for the Dataset
string = '{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2]count(): Parameter must be an array or an object that implements Countable(153)"}]}'
#Import Dependencies
import re
temp= re.findall(':[0-9]+', string)
arr=[]
for x in temp:
  arr.append(x.strip(':'))
print(arr)