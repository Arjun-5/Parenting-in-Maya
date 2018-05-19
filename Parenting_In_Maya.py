from maya import cmds

polycube = cmds.polyCube();
nurbscircle = cmds.circle();
cmds.parent(nurbscircle[0],polycube[0]);
