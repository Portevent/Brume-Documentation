---
title: FogVision
path: /BoardEngine
alias: 
- Fog Vision
tag: 
- class
---
MonoBehavior Object feeding the [[FogManager]] position from its own.
e.g. attach to the player game object to have the fog vision
```d2
# Nodes :
BoardEngine: {
    FogManager: Fog Manager {
       link: FogManager
    }
}

# Links :
BoardEngine.FogVision -> BoardEngine.FogManager: Update the Fog Vision {
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}

```