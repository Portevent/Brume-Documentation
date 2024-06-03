---
title: TilemapManager
path: /BoardEngine
alias: 
- Tilemap Manager
tag: 
- class
---
Centralized way to create Tilemap  
```d2
# Nodes :
BoardEngine: {
    WorldEngine: {
        WorldManager: World Manager {
           link: WorldManager
        }
    }
    SelectionManager: Selection Manager {
       link: SelectionManager
    }
}

# Links :
BoardEngine.WorldEngine.WorldManager -> BoardEngine.TilemapManager: Uses {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
BoardEngine.SelectionManager -> BoardEngine.TilemapManager: Uses {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}

```