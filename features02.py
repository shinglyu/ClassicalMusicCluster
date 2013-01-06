from music21 import *
from corpusList import *
from collections import defaultdict

def divideByTotal(inputDict, total):
   return {key:float(count)/total for key, count in inputDict.iteritems()}

def printDict(dic,idxRange):
   f.write(str(dic.get(0,0))) 
   for i in range(1,idxRange):
      f.write(",")
      f.write(str(dic.get(i,0)))

def getNoteCount(score):
   notes = score.flat.getElementsByClass(note.Note)
   noteCount = defaultdict(int) 
   for cNote in notes:
      noteCount[cNote.pitch.pitchClass] += 1
   return noteCount

def getNoteCountFreq(score):
   noteCount = getNoteCount(score)
   noteCountFreq = divideByTotal(noteCount, len(notes))
   return noteCountFreq

def getOctave(score):
   notes = score.flat.getElementsByClass(note.Note)
   octave= defaultdict(int) 
   for cNote in notes:
      octave[cNote.pitch.octave] += 1
   return octave 

def getOctaveFreq(score):
   notes = score.flat.getElementsByClass(note.Note)
   octave = getOctave(score)
   octaveFreq = divideByTotal(octave, len(notes))
   return octaveFreq

def getMelodicDiff(score):
   mdirs = []
   for part in score.parts:
      notes = part.flat.getElementsByClass(note.Note)
      getInterval = lambda n1, n2 : interval.notesToChromatic(n1,n2).semitones
      mdir = map(getInterval, notes[:-1], notes[1:])
      mdirs = mdirs + mdir
   return mdirs

def mean(vec):
   return float(sum(vec))/len(vec)
def variance(vec):
   mu = mean(vec)
   return sum(map(lambda x: (x-mu)**2, vec))/len(vec)

def getMelodicMean(score):
   return mean(getMelodicDiff(score))
def getMelodicVar(score):
   return variance(getMelodicDiff(score))

def getTimeSignature(score):
   ts = score.flat.getElementsByClass(meter.TimeSignature)[0]
   return ts.barDuration.quarterLength


if __name__ == '__main__':
   print("Getting corpus list..." )
   corpusList = getCorpusList()
   print("done." )

   f = open('./feature01.csv', 'w')
   attrSizes = [12,12,8,8,1,3]
# print the name of your features here ===========================================

if __name__ == '__main__':
   print("Getting corpus list..." )
   corpusList = getCorpusList()
   print("done." )

   f = open('./feature02.csv', 'w')
   attrSizes = [1,1,1,1,1,1,1]
# print the name of your features here ===========================================
   #attrNames= ["noteCount", "noteCountFreq", "octave", "octaveFreq", "composer", "ts_numerator", "ts_denominator", "time_signature", "melDiffMean", "melDiffVar","noteMeasure","duMean","duVar"]
   attrNames= ["composer", "time_signature", "melDiffMean", "melDiffVar","noteMeasure","duMean","duVar"]
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
      measureCount = 0
      noteDuration = []
      for part in score.parts:
         measureCount += len(part.getElementsByClass(stream.Measure))
         
      for cNote in notes:
           noteDuration.append(cNote.duration.quarterLength)
       
##      noteCount = getNoteCount(score) 
##      noteCountFreq = getNoteCountFreq(score) 
##      octave = getOctave(score) 
##      octaveFreq = getOctaveFreq(score) 
      timeSignature= getTimeSignature(score) 
      melDiffMean = getMelodicMean(score)
      melDiffVar= getMelodicVar(score)
      durationMean = mean(noteDuration)
      durationVar = variance(noteDuration)
# print features here ===========================================================
##      printDict(noteCount, attrSizes[0])
##      f.write(",")
##      printDict(noteCountFreq, attrSizes[1])
##      f.write(",")
##      printDict(octave, attrSizes[2])
##      f.write(",")
##      printDict(octaveFreq, attrSizes[3])
##      f.write(",")
      f.write(corpusName.split('/')[0])
      f.write(",")
      f.write(str(timeSignature))
      f.write(",")
      f.write(str(melDiffMean))
      f.write(",")
      f.write(str(melDiffVar))
      f.write(",")
      f.write(str(len(notes)*len(score.parts)/measureCount))
      f.write(",")
      f.write(str(durationMean))
      f.write(",")
      f.write(str(durationVar))
      f.write("\n")
      print("done." )
   f.close()
