
fname = "./feature01.txt"
with open(fname) as f:
   lines = f.readlines()
attrNames = lines[0].strip().split(',')
print(attrNames)

for line in lines[1:]:
   print(line.strip().split(';'))


