---
title: BoardManager
path: /BoardEngine
alias: 
- Board Manager
tag: 
- class
---
Use the [[DimensionManager]] to compute existing cell ([[DimensionCoordinate]]) and free cell toward/away.
Also communicate with [[EntityManager]] to determine if a cell is free.  
```d2
# Nodes :
WorldEngine: {
    DimensionEngine: {
        DimensionManager: Dimension Manager {
           link: DimensionManager
        }
    }
}
MagicEngine: {
    MagicManager: Magic Manager {
       link: MagicManager
    }
}

# Links :
WorldEngine.DimensionEngine.DimensionManager -> BoardEngine.BoardManager: Get active Dimension {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
BoardEngine.BoardManager -> MagicEngine.MagicManager: Manipulate Cell {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}

```