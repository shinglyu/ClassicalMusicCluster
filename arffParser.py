
fnames = ["./feature01.txt"]
for fname in fnames:
   with open(fname) as f:
      lines = f.readlines()
   attrNames = lines[0].strip().split(',')
   print(attrNames)
   firstLine = lines[1]
   attrs = line.strip().split(';')
   size = []
   for attr in attrs:
      if attr.startswith('['):
         nums = attr[1:-1].split(',')
         size.append(len(nums))
      else:
         size.append(1)

   fullAttrNames = 
   for attrName in attrNames:
      if fullAttrNames 

   for line in lines[1:]:
      print(line.strip().split(';'))


