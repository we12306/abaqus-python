# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import job
for i in range(1,2):
    #P1
    name1='N100-63NM-P1-rand0'+str(i)
    name2='D:\effective modulus\N100-63NM\N100-63NM-P1-rand0'+str(i)+'.inp'
    mdb.JobFromInputFile(name=name1,inputFileName=name2,numCpus=4, numDomains=4)
    mdb.jobs[name1].submit()
    mdb.jobs[name1].waitForCompletion()
    #P2
    name1='N100-63NM-P2-rand0'+str(i)
    name2='D:\effective modulus\N100-63NM\N100-63NM-P2-rand0'+str(i)+'.inp'
    mdb.JobFromInputFile(name=name1,inputFileName=name2,numCpus=4, numDomains=4)
    mdb.jobs[name1].submit()
    mdb.jobs[name1].waitForCompletion()
    #P12
    name1='N100-63NM-P12-rand0'+str(i)
    name2='D:\effective modulus\N100-63NM\N100-63NM-P12-rand0'+str(i)+'.inp'
    mdb.JobFromInputFile(name=name1,inputFileName=name2,numCpus=4, numDomains=4)
    mdb.jobs[name1].submit()
    mdb.jobs[name1].waitForCompletion()
