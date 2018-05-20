from maya import cmds;

objectList = [cmds.polyCube(),cmds.circle(),cmds.cone()]

for obj in objectList:
    obj