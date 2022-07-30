# cheatsheet python vs js
| Python | Js |
| ----- | -------|
| print("ada lovelace".title()) | | 
| print(f'Hello {world}') | console.log(\`Hello ${world\`)|
| str[::-1] # slicing any indexed based, str[start:stop:step] |  |
| print(r'\t\n') # python raw strings | |
| len(string) | str.length |
| str(age) | age.toString() |
| int(str) | parseInt(str) or Number(str)|
| float(str) | parseFloat(str) or Number(str)|
| lst = [ "a, "b"] # list | arr = [ "a", "b"] // array |
| lst.append('c') | | 
| lst.insert(0, 'd') | | 
| del lst[0] or lst.pop(0) or lst[:-2] = [] | |
| for elem in list : | |
| list(range(1, 5)) # from 1 to 4, last is exclusive | |
| help(range) | |
| [val**2 for val in range(1, 11) if val != 7] # list comprehension | |
| lst[:] # copy a list | |
| tuple = 12345, 54, 'hello' | | 
| a,b, \*other = lst  # unpacking iterable | |
| if value in list : | | 
| isTrue = False | |
| aSet = { 'a','b','c'} | | 
| aDict = {'a':1,'b':2} | |
| aDict = { x:x**2 for x in range(1,5)} # dico comprehension | |
| for k,v in aDict.items(): ... | |
| for index, v in enumerate(range(1, 10)) # enumerate rturn value + counter | | 
| nullValue = None | nullValue = undefined or null |
| upperLst = list(map(lambda s: s.upper(), lst) | upperLst = lst.map(s => s.upper) |
| type(var) | typeof var |



