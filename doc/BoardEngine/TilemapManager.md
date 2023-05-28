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
    SelectionManager: Selection Manager {
       link: SelectionManager
    }
    WorldManager: World Manager {
       link: WorldManager
    }
}

# Links :
BoardEngine.SelectionManager -> BoardEngine.TilemapManager: Uses {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
BoardEngine.WorldManager -> BoardEngine.TilemapManager: Uses {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}

```