from music21 import *
cList = [\
      'bach/bwv1.6.mxl',\
      #'bach/bwv194.12.mxl',\
      'cpebach/h186.mxl',\
      #'beethoven/opus132.mxl',\
      #'beethoven/opus133.mxl',\
      #'beethoven/opus18no3.mxl',\
      #'beethoven/opus18no4.mxl',\
      #'beethoven/opus18no5.mxl',\
      #'haydn/opus1no0/movement1.zip',\
      #'haydn/opus1no0/movement2.zip',\
      #'haydn/opus1no0/movement3.zip',\
      #'haydn/opus1no0/movement4.zip',\
      #'haydn/opus1no0/movement5.zip',\
      #'mozart/k155/movement1.mxl',\
      #'mozart/k155/movement2.mxl',\
      #'mozart/k155/movement3.mxl',\
      #'mozart/k156/movement1.mxl',\
      #'mozart/k156/movement2.mxl',\
      #'mozart/k156/movement3.mxl',\
      #'mozart/k156/movement4.mxl',\
      #'schubert/d576-1',\
      #'schubert/d576-2',\
      #'schubert/d576-3',\
      #'schubert/d576-4',\
        ]
def getCorpusList():
   #testCorpusList()
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

