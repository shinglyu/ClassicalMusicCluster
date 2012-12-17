from music21 import *
from collections import defaultdict

def divideByTotal(inputDict, total):
   return {key:float(count)/total for key, count in inputDict.iteritems()}

score = corpus.parse('bach/bwv7.7')
print score.notes
notes = score.flat.getElementsByClass(note.Note)
noteCount = defaultdict(int) 
octave= defaultdict(int) 
for note in notes:
   noteCount[note.pitch.pitchClass] += 1
   octave[note.pitch.octave] += 1
   #print note.pitch


noteCountFreq = divideByTotal(noteCount, len(notes))
octaveFreq = divideByTotal(octave, len(notes))
f = open('./feature01.txt', 'w')
line = ["scoreName", "noteCount", "noteCountFreq", "ocatev", "octaveFreq"]
f.write(",".join(line))
print(noteCount)
print(noteCountFreq)
print(octave)
print(octaveFreq)
