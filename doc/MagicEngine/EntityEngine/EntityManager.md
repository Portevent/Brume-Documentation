---
title: EntityManager
path: /MagicEngine/EntityEngine
alias: 
- Entity Manager
tag: 
- class
---
Keep track of all [[Entity]], and register / unregister them as needed.
Entity Manager also move [[Entity]] around using [[BoardManager]] to determine if a cell exist and can be used. The main task of Entity Manager is handling when two [[Entity]] need to switch places.
Every displacement generate a [[Movement]]
It is also where [[Entity]] are instancied.
```d2
# Nodes :
BoardEngine: {
    Coordinate: Coordinate {
       link: Coordinate
    }
}
GameplayManager: {
    GameModeManager: Game Mode Manager {
       link: GameModeManager
    }
}
MagicEngine: {
    EntityEngine: {
        Entity: Entity {
           link: Entity
        }
    }
}

# Links :
BoardEngine.Coordinate -- MagicEngine.EntityEngine.EntityManager: {style.stroke-dash: 3}
MagicEngine.EntityEngine.EntityManager -> GameplayManager.GameModeManager: Listen to {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
MagicEngine.EntityEngine.EntityManager -> MagicEngine.EntityEngine.Entity: Has {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}

```
---
# Summary :
name|description
----|----
[[#RegisterEntity\|RegisterEntity]] | `Add a new entity to the board`
[[#Unregister\|Unregister]] | `Remove an Entity from the game (remove it from EntityManager, delete its gameobject)`

---
# Functions :

---
### RegisterEntity
Add a new entity to the board

#### Parameters
name|type|description
-----|-----|-----
**entity**|[[Entity]]|Entity to register
**coordinates**|[[Coordinate]]|Coordiantes

---
### Unregister
Remove an Entity from the game (remove it from EntityManager, delete its gameobject)

#### Parameters
name|type|description
-----|-----|-----
**entity**|[[Entity]]|Entity to unregister
**checkSummoner**|`bool`|Set this to false to not check if the entity is summoned by another one. Will cause issue if properly set to false
