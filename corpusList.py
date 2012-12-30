from music21 import *
cList = [\
'beethoven/opus132.mxl',\
'beethoven/opus133.mxl',\
'beethoven/opus18no1/movement1.krn',\
'beethoven/opus18no1/movement1.mxl',\
'beethoven/opus18no1/movement2.krn',\
'beethoven/opus18no1/movement2.mxl',\
'beethoven/opus18no1/movement3.krn',\
'beethoven/opus18no1/movement3.mxl',\
'beethoven/opus18no1/movement4.krn',\
'beethoven/opus18no1/movement4.mxl',\
'beethoven/opus18no3.mxl',\
'beethoven/opus18no4.mxl',\
'beethoven/opus18no5.mxl',\
'beethoven/opus59no1/movement1.mxl',\
'beethoven/opus59no1/movement2.mxl',\
'beethoven/opus59no1/movement3.mxl',\
'beethoven/opus59no1/movement4.mxl',\
'beethoven/opus59no2/movement1.mxl',\
'beethoven/opus59no2/movement2.mxl',\
'beethoven/opus59no2/movement3.mxl',\
'beethoven/opus59no2/movement4.mxl',\
'beethoven/opus59no3/movement1.mxl',\
'beethoven/opus59no3/movement2.mxl',\
'beethoven/opus59no3/movement3.mxl',\
'beethoven/opus59no3/movement4.mxl',\
'beethoven/opus74.mxl',\
'haydn/opus1no0/movement1.zip',\
'haydn/opus1no0/movement2.zip',\
'haydn/opus1no0/movement3.zip',\
'haydn/opus1no0/movement4.zip',\
'haydn/opus1no0/movement5.zip',\
'haydn/opus1no1/movement1.zip',\
'haydn/opus1no1/movement2.zip',\
'haydn/opus1no1/movement3.zip',\
'haydn/opus1no1/movement4.zip',\
'haydn/opus1no1/movement5.zip',\
'haydn/opus1no2/movement1.zip',\
'haydn/opus1no2/movement2.zip',\
'haydn/opus1no2/movement3.zip',\
'haydn/opus1no2/movement4.zip',\
'haydn/opus1no2/movement5.zip',\
'haydn/opus1no3/movement1.zip',\
'haydn/opus1no3/movement2.zip',\
'haydn/opus1no3/movement3.zip',\
'haydn/opus1no3/movement4.zip',\
'haydn/opus1no3/movement5.zip',\
'haydn/opus1no4/movement1.zip',\
'haydn/opus1no4/movement2.zip',\
'haydn/opus1no4/movement3.zip',\
'haydn/opus1no4/movement4.zip',\
'haydn/opus1no4/movement5.zip',\
'haydn/opus1no6/movement1.zip',\
'haydn/opus1no6/movement2.zip',\
'haydn/opus1no6/movement3.zip',\
'haydn/opus1no6/movement4.zip',\
'haydn/opus1no6/movement5.zip',\
'haydn/opus103/movement1.zip',\
'haydn/opus103/movement2.zip',\
'haydn/opus103/movement3.zip',\
'haydn/opus17no1/movement1.zip',\
'haydn/opus17no1/movement2.zip',\
'haydn/opus17no1/movement3.zip',\
'haydn/opus17no1/movement4.zip',\
'haydn/opus17no2/movement1.zip',\
'haydn/opus17no2/movement2.zip',\
'haydn/opus17no2/movement3.zip',\
'haydn/opus17no2/movement4.zip',\
'haydn/opus17no3/movement1.zip',\
'haydn/opus17no3/movement2.zip',\
'haydn/opus17no3/movement3.zip',\
'haydn/opus17no3/movement4.zip',\
'haydn/opus17no5/movement1.zip',\
'haydn/opus17no5/movement2.zip',\
'haydn/opus17no5/movement3.zip',\
'haydn/opus17no5/movement4.zip',\
'haydn/opus17no6/movement1.zip',\
'haydn/opus17no6/movement2.zip',\
'haydn/opus17no6/movement3.zip',\
'haydn/opus17no6/movement4.zip',\
'haydn/opus20no1/movement1.zip',\
'haydn/opus20no1/movement2.zip',\
'haydn/opus20no1/movement3.zip',\
'haydn/opus20no1/movement4.zip',\
'haydn/opus20no2/movement1.zip',\
'haydn/opus20no2/movement2.zip',\
'haydn/opus20no2/movement3.zip',\
'haydn/opus20no2/movement4.zip',\
'haydn/opus20no3/movement1.zip',\
'haydn/opus20no3/movement2.zip',\
'haydn/opus20no3/movement3.zip',\
'haydn/opus20no3/movement4.zip',\
'haydn/opus20no4/movement1.zip',\
'haydn/opus20no4/movement2.zip',\
'haydn/opus20no4/movement3.zip',\
'haydn/opus20no4/movement4.zip',\
'haydn/opus20no5/movement1.zip',\
'haydn/opus20no5/movement2.zip',\
'haydn/opus20no5/movement3.zip',\
'haydn/opus20no5/movement4.zip',\
'haydn/opus20no6/movement1.zip',\
'haydn/opus20no6/movement2.zip',\
'haydn/opus20no6/movement3.zip',\
'haydn/opus20no6/movement4.zip',\
'haydn/opus33no1/movement1.zip',\
'haydn/opus33no1/movement2.zip',\
'haydn/opus33no1/movement3.zip',\
'haydn/opus33no1/movement4.zip',\
'haydn/opus33no2/movement1.zip',\
'haydn/opus33no2/movement2.zip',\
'haydn/opus33no2/movement3.zip',\
'haydn/opus33no3/movement1.zip',\
'haydn/opus33no3/movement2.zip',\
'haydn/opus33no3/movement3.zip',\
'haydn/opus33no3/movement4.zip',\
'haydn/opus33no4/movement1.zip',\
'haydn/opus33no4/movement2.zip',\
'haydn/opus33no4/movement3.zip',\
'haydn/opus33no4/movement4.zip',\
'haydn/opus33no5/movement1.zip',\
'haydn/opus33no5/movement2.zip',\
'haydn/opus33no5/movement3.zip',\
'haydn/opus33no5/movement4.zip',\
'haydn/opus33no6/movement1.zip',\
'haydn/opus33no6/movement2.zip',\
'haydn/opus33no6/movement3.zip',\
'haydn/opus33no6/movement4.zip',\
'haydn/opus42/movement1.zip',\
'haydn/opus42/movement2.zip',\
'haydn/opus42/movement3.zip',\
'haydn/opus42/movement4.zip',\
'haydn/opus50no1/movement1.zip',\
'haydn/opus50no1/movement2.zip',\
'haydn/opus50no1/movement3.zip',\
'haydn/opus50no1/movement4.zip',\
'haydn/opus50no2/movement1.zip',\
'haydn/opus50no2/movement2.zip',\
'haydn/opus50no2/movement3.zip',\
'haydn/opus50no2/movement4.zip',\
'haydn/opus50no3/movement1.zip',\
'haydn/opus50no3/movement2.zip',\
'haydn/opus50no3/movement3.zip',\
'haydn/opus50no3/movement4.zip',\
'haydn/opus50no4/movement1.zip',\
'haydn/opus50no4/movement2.zip',\
'haydn/opus50no4/movement3.zip',\
'haydn/opus50no4/movement4.zip',\
'haydn/opus50no5/movement1.zip',\
'haydn/opus50no5/movement2.zip',\
'haydn/opus50no5/movement3.zip',\
'haydn/opus50no5/movement4.zip',\
'haydn/opus50no6/movement1.zip',\
'haydn/opus50no6/movement2.zip',\
'haydn/opus50no6/movement3.zip',\
'haydn/opus50no6/movement4.zip',\
'haydn/opus54no1/movement1.zip',\
'haydn/opus54no1/movement2.zip',\
'haydn/opus54no1/movement3.zip',\
'haydn/opus54no1/movement4.zip',\
'haydn/opus54no2/movement1.md',\
'haydn/opus54no2/movement2.md',\
'haydn/opus54no2/movement3.md',\
'haydn/opus54no2/movement4.md',\
'haydn/opus54no3/movement1.zip',\
'haydn/opus54no3/movement2.zip',\
'haydn/opus54no3/movement3.zip',\
'haydn/opus54no3/movement4.zip',\
'haydn/opus55no1/movement1.md',\
'haydn/opus55no1/movement2.md',\
'haydn/opus55no1/movement3.md',\
'haydn/opus55no1/movement4.md',\
'haydn/opus55no2/movement1.zip',\
'haydn/opus55no2/movement2.zip',\
'haydn/opus55no2/movement3.zip',\
'haydn/opus55no2/movement4.zip',\
'haydn/opus55no3/movement1.md',\
'haydn/opus55no3/movement2.md',\
'haydn/opus55no3/movement3.md',\
'haydn/opus55no3/movement4.md',\
'haydn/opus64no1/movement1.md',\
'haydn/opus64no1/movement2.md',\
'haydn/opus64no1/movement3.md',\
'haydn/opus64no1/movement4.md',\
'haydn/opus64no2/movement1.md',\
'haydn/opus64no2/movement2.md',\
'haydn/opus64no2/movement3.md',\
'haydn/opus64no2/movement4.md',\
'haydn/opus64no3/movement1.zip',\
'haydn/opus64no3/movement2.zip',\
'haydn/opus64no3/movement3.zip',\
'haydn/opus64no3/movement4.zip',\
'haydn/opus64no4/movement1.zip',\
'haydn/opus64no4/movement2.zip',\
'haydn/opus64no4/movement3.zip',\
'haydn/opus64no4/movement4.zip',\
'haydn/opus64no5/movement1.zip',\
'haydn/opus64no5/movement2.zip',\
'haydn/opus64no5/movement3.zip',\
'haydn/opus64no5/movement4.zip',\
'haydn/opus64no6/movement1.zip',\
'haydn/opus64no6/movement2.zip',\
'haydn/opus64no6/movement3.zip',\
'haydn/opus64no6/movement4.zip',\
'haydn/opus71no1/movement1.zip',\
'haydn/opus71no1/movement2.zip',\
'haydn/opus71no1/movement3.zip',\
'haydn/opus71no1/movement4.zip',\
'haydn/opus71no2/movement1.zip',\
'haydn/opus71no2/movement2.zip',\
'haydn/opus71no2/movement3.zip',\
'haydn/opus71no2/movement4.zip',\
'haydn/opus71no3/movement1.zip',\
'haydn/opus71no3/movement2.zip',\
'haydn/opus71no3/movement3.zip',\
'haydn/opus71no3/movement4.zip',\
'haydn/opus74no1/movement1.mxl',\
'haydn/opus74no1/movement2.mxl',\
'haydn/opus74no1/movement3.mxl',\
'haydn/opus74no1/movement4.mxl',\
'haydn/opus74no2/movement1.mxl',\
'haydn/opus74no2/movement2.mxl',\
'haydn/opus74no2/movement3.mxl',\
'haydn/opus74no2/movement4.mxl',\
'haydn/opus74no2/movement5.mxl',\
'haydn/opus74no3/movement1.zip',\
'haydn/opus74no3/movement2.zip',\
'haydn/opus74no3/movement3.zip',\
'haydn/opus74no3/movement4.zip',\
'haydn/opus76no1/movement1.zip',\
'haydn/opus76no1/movement2.zip',\
'haydn/opus76no1/movement3.zip',\
'haydn/opus76no1/movement4.zip',\
'haydn/opus76no2/movement1.zip',\
'haydn/opus76no2/movement2.zip',\
'haydn/opus76no2/movement3.zip',\
'haydn/opus76no2/movement4.zip',\
'haydn/opus76no3/movement1.zip',\
'haydn/opus76no3/movement2.zip',\
'haydn/opus76no3/movement3.zip',\
'haydn/opus76no3/movement4.zip',\
'haydn/opus76no4/movement1.zip',\
'haydn/opus76no4/movement2.zip',\
'haydn/opus76no4/movement3.zip',\
'haydn/opus76no4/movement4.zip',\
'haydn/opus76no5/movement1.zip',\
'haydn/opus76no5/movement2.zip',\
'haydn/opus76no5/movement3.zip',\
'haydn/opus76no5/movement4.zip',\
'haydn/opus76no6/movement1.zip',\
'haydn/opus76no6/movement2.zip',\
'haydn/opus76no6/movement3.zip',\
'haydn/opus76no6/movement4.zip',\
'haydn/opus77no1/movement1.zip',\
'haydn/opus77no1/movement2.zip',\
'haydn/opus77no1/movement3.zip',\
'haydn/opus77no1/movement4.zip',\
'haydn/opus77no2/movement1.zip',\
'haydn/opus77no2/movement2.zip',\
'haydn/opus77no2/movement3.zip',\
'haydn/opus77no2/movement4.zip',\
'haydn/opus9no2/movement1.zip',\
'haydn/opus9no2/movement2.zip',\
'haydn/opus9no2/movement4.zip',\
'haydn/opus9no3/movement1.zip',\
'haydn/opus9no3/movement2.zip',\
'haydn/opus9no3/movement3.zip',\
'haydn/opus9no3/movement4.zip',\
'haydn/symphony94/01.zip',\
'haydn/symphony94/02.zip',\
'haydn/symphony94/03.zip',\
'haydn/symphony94/04.zip',\
'mozart/k155/movement1.mxl',\
'mozart/k155/movement2.mxl',\
'mozart/k155/movement3.mxl',\
'mozart/k156/movement1.mxl',\
'mozart/k156/movement2.mxl',\
'mozart/k156/movement3.mxl',\
'mozart/k156/movement4.mxl',\
'mozart/k157/movement1.md',\
'mozart/k157/movement2.md',\
'mozart/k157/movement3.md',\
'mozart/k158/movement1.md',\
'mozart/k158/movement2.md',\
'mozart/k158/movement3.md',\
'mozart/k159/movement1.md',\
'mozart/k159/movement2.md',\
'mozart/k159/movement3.md',\
'mozart/k160/movement1.md',\
'mozart/k160/movement2.md',\
'mozart/k160/movement3.md',\
'mozart/k168/movement1.zip',\
'mozart/k168/movement2.zip',\
'mozart/k168/movement3.zip',\
'mozart/k168/movement4.zip',\
'mozart/k169/movement1.zip',\
'mozart/k169/movement2.zip',\
'mozart/k169/movement3.zip',\
'mozart/k169/movement4.zip',\
'mozart/k170/movement1.zip',\
'mozart/k170/movement2.zip',\
'mozart/k170/movement3.zip',\
'mozart/k170/movement4.zip',\
'mozart/k171/movement2.zip',\
'mozart/k171/movement3.zip',\
'mozart/k171/movement4.zip',\
'mozart/k172/movement1.zip',\
'mozart/k172/movement2.zip',\
'mozart/k172/movement3.zip',\
'mozart/k172/movement4.zip',\
'mozart/k173/movement1.zip',\
'mozart/k173/movement2.zip',\
'mozart/k173/movement3.zip',\
'mozart/k173/movement4.zip',\
'mozart/k285/movement1.zip',\
'mozart/k285/movement2.zip',\
'mozart/k285/movement3.zip',\
'mozart/k298/movement1.zip',\
'mozart/k298/movement2.zip',\
'mozart/k298/movement3.zip',\
'mozart/k370/movement1.zip',\
'mozart/k370/movement2.zip',\
'mozart/k370/movement3.zip',\
'mozart/k387/movement1.zip',\
'mozart/k387/movement2.zip',\
'mozart/k387/movement3.zip',\
'mozart/k387/movement4.zip',\
'mozart/k421/movement1.zip',\
'mozart/k421/movement2.zip',\
'mozart/k421/movement3.zip',\
'mozart/k421/movement4.zip',\
'mozart/k428/movement1.zip',\
'mozart/k428/movement2.zip',\
'mozart/k428/movement3.zip',\
'mozart/k428/movement4.zip',\
'mozart/k458/movement1.mxl',\
'mozart/k458/movement2.mxl',\
'mozart/k458/movement3.mxl',\
'mozart/k458/movement4.mxl',\
'mozart/k464/movement1.zip',\
'mozart/k464/movement2.zip',\
'mozart/k464/movement3.zip',\
'mozart/k464/movement4.zip',\
'mozart/k465/movement2.zip',\
'mozart/k465/movement3.zip',\
'mozart/k465/movement4.zip',\
'mozart/k499/movement1.zip',\
'mozart/k499/movement2.zip',\
'mozart/k499/movement3.zip',\
'mozart/k499/movement4.zip',\
'mozart/k545/movement1_exposition.mxl',\
'mozart/k546/movement1.zip',\
'mozart/k546/movement2.zip',\
'mozart/k575/movement1.zip',\
'mozart/k575/movement2.zip',\
'mozart/k575/movement3.zip',\
'mozart/k575/movement4.zip',\
'mozart/k589/movement1.zip',\
'mozart/k589/movement2.zip',\
'mozart/k589/movement3.zip',\
'mozart/k589/movement4.zip',\
'mozart/k590/movement1.zip',\
'mozart/k590/movement2.zip',\
'mozart/k590/movement3.zip',\
'mozart/k590/movement4.zip',\
'mozart/k80/movement1.mxl',\
'mozart/k80/movement2.mxl',\
'mozart/k80/movement3.mxl',\
'mozart/k80/movement4.mxl',\
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

