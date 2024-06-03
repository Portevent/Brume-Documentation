---
title: WorldManager
path: /BoardEngine/WorldEngine
alias: 
- World Manager
tag: 
- class
---
Create and manage [[World]]
Create any number of Tilemap needed, plus one for the Fog and assign it with the [[FogManager]]
Make uses of [[TilemapManager]]  
```d2
# Nodes :
BoardEngine: {
    BoardManager: Board Manager {
       link: BoardManager
    }
    WorldEngine: {
        World: World {
           link: World
        }
    }
    TilemapManager: Tilemap Manager {
       link: TilemapManager
    }
    ChunkManager: Chunk Manager {
       link: ChunkManager
    }
}

# Links :
BoardEngine.WorldEngine.WorldManager -> BoardEngine.BoardManager: Get active World {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
BoardEngine.WorldEngine.WorldManager -> BoardEngine.ChunkManager: Update view coordinate {
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
BoardEngine.WorldEngine.WorldManager -> BoardEngine.WorldEngine.World: Instantiate {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
BoardEngine.WorldEngine.WorldManager -> BoardEngine.TilemapManager: Uses {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}

```