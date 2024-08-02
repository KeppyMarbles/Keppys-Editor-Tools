# Keppy's Editor Tools
A project that adds useful things to PQ's level editor which can't be done with TorqueScript alone.

Sends commands to Python using TCPObjects and a localhost server.

## Install
1. Install [Python](https://www.python.org/downloads/)
2. Download the source code and extract
3. Place [csx3dif.exe](https://github.com/RandomityGuy/csx3dif/releases) in the folder
4. Move missions folder into `platinum/data`

## Usage

1. Start the server using the .bat file or running `ket.py`
2. In PQ, click Play on Keppy's Editor Tools (in `custom/ket` by default)
3. Load into the level you want to edit.

KET's additions will persist until you close out of the game.

## Features
![convertcsx](https://github.com/KeppyMarbles/Keppys-Editor-Tools/assets/147150384/5b6f1b47-d5e2-4c49-b8c5-b8e9cf40ccc0)

In the level editor, you'll notice some new buttons next to Change Skybox. The first one will show a window listing CSX files in any of the interior folders. Select one to convert it into a DIF and add it to the mission.

https://github.com/user-attachments/assets/10710729-e824-43e2-9134-9cf0070e8570

To use this feature, just have the CSX file you're working on be somewhere in the appropriate interiors folder (`interiors_mbg` if using MBG textures, `interiors_mbp` if using MBP, etc).

![remake](https://github.com/user-attachments/assets/c5c3e809-1b7e-432a-8e92-e78971f7c435)

In the level building process, you'll make frequent changes to your CSX file in Constructor. After selecting an interior, you can use the Remake button to run csx3dif again and replace the old version.

https://github.com/user-attachments/assets/b73a3777-35c2-40eb-a2e1-04fc6e7252d3

CSX and DIF files are paired by having the same name and folder. So, if you want to reconvert an interior that uses `test.dif` in `interiors_mbp/custom`, just have `test.csx` also in `interiors_mbp/custom`.

![auto](https://github.com/user-attachments/assets/8caeb05f-6a99-451f-bc0f-72bd0e1f7c04)

No need to keep opening the editor to remake when playtesting. When auto-remake is enabled on an interior, it will be reconverted whenever you make a change to its CSX file, like when pressing Ctrl+S in Constructor.

https://github.com/user-attachments/assets/2f2c8a0b-8d7d-4f89-bf11-5479bbafede7

Note: The game will not recieve commands to reconvert an interior if the game is paused. So, if you want to use the pause menu to tab out to Constructor, you can click the new Disable Pause button in the editor.

## Unsupported features

+ No handling for split DIFs yet. This happens for large CSX files (16384 or more total faces). In this case, you'll want to manually split your level into multiple CSX files.
+ No code yet for Torque moving platforms or other entities.

## Planned or possible features

+ Torque moving platform tools
+ Blender integration
+ Marbleland uploading

Let me know if you have any other ideas.
