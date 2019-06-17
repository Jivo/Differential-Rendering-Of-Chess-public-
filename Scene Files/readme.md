# Scene Files

## Requirements
 - An executable of the modified pbrt needs to be placed in this folder in order to run *sceneFile.pbrt*.
 - obj2pbrt executable must be in this folder, and unzip *properScebe.mb* in order to run the animation script *amimationScript.py* in Maya.
 
 ## Running
 To render the current frame, move into this directory, and run `./pbrt sceneFile.pbrt`
 
 To run the animation script, load *properScene.mb* in maya, and load the script *animationScript.py* if on windows, or
 *animationScript_linux.py* if on linux (this only changes the way external commands are called). In the script, there is a 
 line `os.chdir("/home/weirjosh/CGRA408/Ass3/animation_test/")`, which indicates the source directory of the scene folder. You
 will need to change the directory to where ever you placed these files. 
 
 All frames for the animation will be placed in the *frames* folder. NOTE that the animation cannot be stopped once it has 
 begun. 
