---
title: WorldManager
path: /BoardEngine
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
    ChunkManager: Chunk Manager {
       link: ChunkManager
    }
    World: World {
       link: World
    }
    TilemapManager: Tilemap Manager {
       link: TilemapManager
    }
    BoardManager: Board Manager {
       link: BoardManager
    }
}

# Links :
BoardEngine.WorldManager -> BoardEngine.ChunkManager: Update view coordinate {
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
BoardEngine.WorldManager -> BoardEngine.World: Instantiate {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
BoardEngine.WorldManager -> BoardEngine.TilemapManager: Uses {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
BoardEngine.WorldManager -> BoardEngine.BoardManager: Get active World {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}

```