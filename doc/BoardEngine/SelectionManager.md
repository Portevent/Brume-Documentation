---
title: SelectionManager
path: /BoardEngine
alias: 
- Selection Manager
tag: 
- class
---
Create and manage tilemaps for [[Entity]] (uses [[TilemapManager]])
Create Selection Zone and Focus Zone for entity in fight
```d2
# Nodes :
BoardEngine: {
    AreaMaker: Area Maker {
       link: AreaMaker
    }
    TilemapManager: Tilemap Manager {
       link: TilemapManager
    }
}
MagicEngine: {
    EntityEngine: {
        AI: {
            IntentAI: IntentAI {
               link: IntentAI
            }
        }
    }
}

# Links :
BoardEngine.AreaMaker -> BoardEngine.SelectionManager: Get Spells' range cast {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
BoardEngine.SelectionManager -> BoardEngine.TilemapManager: Uses {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
MagicEngine.EntityEngine.AI.IntentAI -> BoardEngine.SelectionManager: Shows Intent {
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}

```