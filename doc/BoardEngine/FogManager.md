---
title: FogManager
path: /BoardEngine
alias: 
- Fog Manager
tag: 
- class
---
Manage the Fog, updating the material to reflect the player position  
```d2
# Nodes :
BoardEngine: {
    FogVision: Fog Vision {
       link: FogVision
    }
}

# Links :
BoardEngine.FogVision -> BoardEngine.FogManager: Update the Fog Vision {
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}

```