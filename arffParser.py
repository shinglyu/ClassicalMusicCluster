
fnames = ["./feature01.txt"]
outf= open('./features.arff', 'w')
for fname in fnames:
   outf.write('@RELATION {0}\n'.format(fname))
   with open(fname) as f:
      lines = f.readlines()
   attrNames = lines[0].strip().split(',')
   for attrName in attrNames:
      outf.write('@ATTRIBUTE {0} NUMERIC\n'.format(attrName))

   outf.write('@DATA\n')
   for line in lines[1:]:
      attrs = (line.strip().split(','))
      if len(attrs) != len(attrName)
      outf.write(','.join(attrs))
      outf.write('\n')

outf.close()



