---
title: BoardManager
path: /BoardEngine
alias: 
- Board Manager
tag: 
- class
---
Use the [[WorldManager]] to compute existing cell ([[Coordinate]]) and free cell toward/away.
Also communicate with [[EntityManager]] to determine if a cell is free.
```d2
# Nodes :
BoardEngine: {
    Coordinate: Coordinate {
       link: Coordinate
    }
    WorldManager: World Manager {
       link: WorldManager
    }
}
MagicEngine: {
    MagicManager: Magic Manager {
       link: MagicManager
    }
}

# Links :
BoardEngine.BoardManager -- BoardEngine.Coordinate: {style.stroke-dash: 3}
BoardEngine.WorldManager -> BoardEngine.BoardManager: Get active World {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
BoardEngine.BoardManager -> MagicEngine.MagicManager: Manipulate Cell {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}

```
---
# Summary :
name|description
----|----
[[#CellFree\|CellFree]] | `Determinate if a cell is free (cell exist and no entity there)`

---
# Functions :

---
### CellFree
Determinate if a cell is free (cell exist and no entity there)

#### Parameters
name|type|description
-----|-----|-----
**coordinates**|[[Coordinate]]|

#### Return
- `bool` : 
