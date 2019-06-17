import maya.cmds as cmds
import subprocess
import os, sys

#This needs to be changed!!
os.chdir("/home/weirjosh/CGRA408/Ass3/animation_test/")

def exportOBJ(filename):
    cmds.file(filename, typ='OBJexport', es=True, pr=True,force=True,
        options='groups=1;ptgroups=0;materials=0;smoothing=0;normals=0')
        
def convertPBRT(name):
    args = "./obj2pbrt "+name+".obj "+name+".pbrt"
    subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=True)
 
        
        
FNULL = open(os.devnull, 'w')
runPBRT = "./pbrt sceneFile.pbrt"  

animCurves = cmds.ls(type='animCurve')
last = cmds.findKeyframe(animCurves, which='last')

for i in range(1, int(last)):#int(last)):
    cmds.currentTime(i)
    cmds.select('white', hierarchy=False, visible=True)
    exportOBJ('whitePieces.obj')
    cmds.select('black', hierarchy=False, visible=True)
    exportOBJ('blackPieces.obj')
    
    convertPBRT('whitePieces')
    convertPBRT('blackPieces')
    print "Frame ",i," RENDERING..."
    subprocess.call(runPBRT, stdout=FNULL, stderr=FNULL, shell=True)
    print "Frame ",i," FINISHED!"    
    #NOTE: This will need to be changed depending on OS!!
    copyArgs = 'cp result.png "frames/frame_'+str(i)+'.png"'
    subprocess.call(copyArgs, shell=True)
    