filenames = ['feature01_three.csv', 'feature02.csv']

files = map(open, filenames)
outFile =  open('features_all.csv', 'w')

while True:
   lines = map(lambda x:x.readline().strip(), files)
   if lines[0] == '': break
   #print fullline 
   fullLine = ",".join(lines)
   outFile.write(fullLine)
   outFile.write("\n")

#for f in files:
   #f.close()
map(lambda x:x.close(), files)
outFile.close()

