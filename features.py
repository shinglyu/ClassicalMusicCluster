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

   f = open('./feature01.csv', 'w')
   attrSizes = [12,12,8,8,1]
# print the name of your features here ===========================================
   attrNames= ["noteCount", "noteCountFreq", "octave", "octaveFreq", "composer"]
   fullAttrNames = []
   for attrSize, attrName in zip(attrSizes, attrNames):
      if attrSize > 1:
         for i in range(0,attrSize):
            fullAttrNames.append("{0}{1}".format(attrName,i))
      else:
         fullAttrNames.append("{0}".format(attrName))

   f.write(",".join(fullAttrNames))
   f.write("\n")

   for corpusName in corpusList:
      print("Processing " + corpusName)
      score = corpus.parse(corpusName)
# Start writing features here ===================================================
      notes = score.flat.getElementsByClass(note.Note)
      print notes
      #notes = score.flat.notes
      #notes = score.flat.getElementsByClass(note)
      noteCount = defaultdict(int) 
      octave= defaultdict(int) 
      for cNote in notes:
         noteCount[cNote.pitch.pitchClass] += 1
         octave[cNote.pitch.octave] += 1
         #print note.pitch


      noteCountFreq = divideByTotal(noteCount, len(notes))
      octaveFreq = divideByTotal(octave, len(notes))

      #f.write(str(corpusName))
      #f.write(";")
# print features here ===========================================================
      printDict(noteCount, attrSizes[0])
      f.write(",")
      printDict(noteCountFreq, attrSizes[1])
      f.write(",")
      printDict(octave, attrSizes[2])
      f.write(",")
      printDict(octaveFreq, attrSizes[3])
      f.write(",")
      f.write(corpusName.split('/')[0])
      f.write("\n")
      print("done." )
   f.close()
