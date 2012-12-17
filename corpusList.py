from music21 import *
cList = ['bach/bwv7.7'\
        ]
def getCorpusList():
   testCorpusList()
   return cList

def testCorpusList():
   try:
      for f in cList:
         corpus.parse(f)

   except:
      raise #smoke test only
#   except IOError:
#      print "I/O error({0}): {1}".format(e.errno, e.strerror)
#      raise

