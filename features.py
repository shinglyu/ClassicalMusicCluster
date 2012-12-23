from music21 import *
from corpusList import *
from collections import defaultdict

def divideByTotal(inputDict, total):
   return {key:float(count)/total for key, count in inputDict.iteritems()}

def printDict(dic,idxRange):
   f.write("[")
   f.write(str(dic.get(0,0))) 
   for i in range(1,idxRange):
      f.write(",")
      f.write(str(dic.get(i,0)))
   f.write("]")
   f.write(";")

if __name__ == '__main__':
   print("Getting corpus list..." )
   corpusList = getCorpusList()
   print("done." )

   f = open('./feature01.txt', 'w')
   line = ["scoreName", "noteCount", "noteCountFreq", "ocatev", "octaveFreq"]
   f.write(",".join(line))
   f.write("\n")

   for corpusName in corpusList:
      print("Processing " + corpusName)
      score = corpus.parse(corpusName)
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

      f.write(str(corpusName))
      f.write(";")
      printDict(noteCount, 12)
      printDict(noteCountFreq, 12)
      printDict(octave, 8)
      printDict(octaveFreq, 8)
      f.write("\n")
      print("done." )
   f.close()
