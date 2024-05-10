# Keppy's Editor Tools
A work in progress add-on for PQ that intends to make the level editor more powerful.
Sends commands to Python using a localhost server.

## Install
1. Install [Python](https://www.python.org/downloads/)
2. Download the [release](https://github.com/KeppyMarbles/Keppys-Editor-Tools/releases/tag/v0.1) and extract
3. Place [csx3dif.exe](https://github.com/RandomityGuy/csx3dif/releases) in the folder
4. Move missions folder into `platinum/data`

## Usage

1. Run the python server using the .bat file or `python ket.py`
2. In PQ, click Play on Keppy's Editor Tools (in custom/ket by default, but you can move the .mis somewhere else if you want)
3. Load into the level you want to edit.

KET's additions will persist until you close out of the game.

## Features
![convertcsx](https://github.com/KeppyMarbles/Keppys-Editor-Tools/assets/147150384/5b6f1b47-d5e2-4c49-b8c5-b8e9cf40ccc0)

In the level editor, you'll notice a new button next to Change Skybox. This will show a window listing CSX files in any of the interior folders. Select one to convert it into a DIF and add it to the mission.

https://github.com/KeppyMarbles/Keppys-Editor-Tools/assets/147150384/1db3490e-8b8f-4430-89a2-fa20b5996bc0

To use this feature, just have the CSX file you're working on be somewhere in the appropriate interiors folder (`interiors_mbg` if using MBG textures, `interiors_mbp` if using MBP, etc). 

![reconvert](https://github.com/KeppyMarbles/Keppys-Editor-Tools/assets/147150384/8c4a26b5-1e82-41fb-a0f2-66839054d05f)

In the level building process, you'll make frequent changes to your CSX file in Constructor. After selecting an interior, you can use the Reconvert button to run csx3dif again and replace the old version.

https://github.com/KeppyMarbles/Keppys-Editor-Tools/assets/147150384/53107a87-8438-4e11-9a09-1b23cda31fa2

CSX and DIF files are paired by having the same name and folder. So, if you want to reconvert an interior that uses `test.dif` in `interiors_mbp/custom`, just have `test.csx` also in `interiors_mbp/custom`.

## Not supported features

+ No handling for split DIFs yet. This only happens for very large CSX files (16384 or more total faces).

## Planned or possible features

+ Automatic conversion
+ Default interior pack
+ Combining defaults into a single DIF
+ DIF texture replacer
+ Sun editing GUI
+ Pathnode tools
+ Selection tools
+ SimGroup tools
+ Scaling tools
+ Playtesting tools
+ Autosave

Let me know if you have any other ideas.
