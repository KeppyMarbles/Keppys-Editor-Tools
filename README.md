# Keppy's Editor Tools
A work in progress add-on for PQ that intends to make the level editor more powerful.
Sends commands to Python using a localhost server.

## Install
1. Install [python](https://www.python.org/downloads/) if you don't have it
2. Download the source code and extract
3. Place [csx3dif.exe](https://github.com/RandomityGuy/csx3dif/releases) in the folder
4. Move missions folder into PQ

## Usage

1. Run the python server using the .bat file or `python ket.py`
2. In PQ, click Play on Keppy's Editor Tools (in custom/ket)
3. Load into the level you want to edit.

KET's additions will persist until you close out of the game.

## Features
#### Converting CSX Files
In the level editor, you'll notice a new button next to Change Skybox. This will show a window listing CSX files in any of the interior folders. Select one to convert it into a DIF and add it to the mission.

#### Reconverting

<img src="https://i.imgur.com/8pCSFBZ.png">

In the level building process, you'll make frequent changes to your CSX file in Constructor. After selecting an interior, you can use the Reconvert button to run csx3dif again and replace the old version.

<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExejIxcHo2amVlaGRpbmI2MmZteTRrejhmaG12NjVxd2cxNXI4ODJrcSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/R7bV3LbIlWNMbK4EQ9/giphy.gif">

CSX and DIF files are paired by having the same name and folder. So, if you have `test.dif` in `interiors_mbp/custom`, just have `test.csx` also in `interiors_mbp/custom`.

## Planned features

+ Default interior pack
+ Combining defaults into a single DIF
+ DIF texture replacer
+ Interior search
+ Sun editing GUI
+ Pathnode tools
+ Selection tools
+ Simgroup tools
+ Scaling tools
+ Playtesting tools
+ Autosave

Let me know if you have any other ideas.
