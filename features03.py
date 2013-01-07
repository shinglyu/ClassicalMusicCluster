from music21 import *
from corpusList import *
from collections import defaultdict

def divideByTotal(inputDict, total):
   return {key:float(count)/total for key, count in inputDict.iteritems()}

def printDict(dic,idxRange):
   #f.write("[")
   f.write(str(dic.get(0,0))) 
   for i in range(1,idxRange):
      f.write(",")
      f.write(str(dic.get(i,0)))
   #f.write("]")
   #f.write(";")
   #f.write(",")

if __name__ == '__main__':
   print("Getting corpus list..." )
   corpusList = getCorpusList()
   print("done." )

   f = open('./features03.csv', 'w')
   attrSizes = [12,12,8,8,1,1,1,1,1,1,1]
# print the name of your features here ===========================================
   #attrNames= ["noteCount", "noteCountFreq", "octave", "octaveFreq","PitchRange","999","444","222","777","000", "composer"]
   attrNames= ["PitchRange","999","444","222","777","000", "composer"]
   fullAttrNames = []
   for attrSize, attrName in zip(attrSizes, attrNames):
      if attrSize > 1:
         for i in range(0,attrSize):
            fullAttrNames.append("{0}{1}".format(attrName,i))
      else:
         fullAttrNames.append("{0}".format(attrName))

   f.write(",".join(fullAttrNames))
   f.write("\n")
   
   threenotedic=defaultdict(int)
   for corpusName in corpusList:
      print("Processing " + corpusName)
      score = corpus.parse(corpusName)
# Start writing features here ===================================================
      notes = score.flat.getElementsByClass(note.Note)
      print "print notes"
      print notes[0]
      #notes = score.flat.notes
      #notes = score.flat.getElementsByClass(note)
      noteCount = defaultdict(int) 
      octave= defaultdict(int)
      corpusthreelist=defaultdict(int)
      for cNote in notes:
	 #print cNote.pitch.pitchClass
         noteCount[cNote.pitch.pitchClass] += 1
         octave[cNote.pitch.octave] += 1
         #print note.pitch
      for i in range (len(notes)-2):
	  three=str(notes[i].pitch.pitchClass)+","+str(notes[i+1].pitch.pitchClass)+","+str(notes[i+2].pitch.pitchClass)
	  corpusthreelist[three]+=1
      v=list(corpusthreelist.values())
      k=list(corpusthreelist.keys())
      threenotedic[k[v.index(max(v))]] +=1
      print k[v.index(max(v))]
      maxnote =0
      minnote =0
      for i in range(12):
	  if noteCount[i]>0:
	      maxnote=i
	  if noteCount[12-i]>0:
	      minnote=12-i;

      difnote=maxnote- minnote

      noteCountFreq = divideByTotal(noteCount, len(notes))
      octaveFreq = divideByTotal(octave, len(notes))

      #f.write(str(corpusName))
      #f.write(";")
# print features here ===========================================================
      #printDict(noteCount, attrSizes[0])
      #f.write(",")
      #printDict(noteCountFreq, attrSizes[1])
      #f.write(",")
      #printDict(octave, attrSizes[2])
      #f.write(",")
      #printDict(octaveFreq, attrSizes[3])
      #f.write(",")
      f.write(str(difnote))
      f.write(",")
      f.write(str(float(corpusthreelist["9,9,9"])/float((len(notes)-2))))
      print(float(corpusthreelist["9,9,9"])/float((len(notes)-2)))
      f.write(",")
      f.write(str(float(corpusthreelist["4,4,4"])/float((len(notes)-2))))
      print(float(corpusthreelist["4,4,4"])/float((len(notes)-2)))
      f.write(",")
      f.write(str(float(corpusthreelist["2,2,2"])/float((len(notes)-2))))
      print(float(corpusthreelist["2,2,2"])/float((len(notes)-2)))
      f.write(",")
      f.write(str(float(corpusthreelist["7,7,7"])/float((len(notes)-2))))
      print(float(corpusthreelist["7,7,7"])/float((len(notes)-2)))
      f.write(",")
      f.write(str(float(corpusthreelist["0,0,0"])/float((len(notes)-2))))
      print(float(corpusthreelist["0,0,0"])/float((len(notes)-2)))
      f.write(",")
      f.write(corpusName.split('/')[0])
      f.write("\n")
      print("done." )
   for k in sorted(threenotedic,key=threenotedic.get,reverse=True):
       print "%s : %s" %(k,threenotedic[k])
       f.write(str(k)+":"+str(threenotedic[k]))   
   f.close()
