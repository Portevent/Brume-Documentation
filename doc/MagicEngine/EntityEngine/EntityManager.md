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
MagicEngine: {
    Spells: {
        Spell: Spell {
           link: Spell
        }
    }
    EntityEngine: {
        Movement: Movement {
           link: Movement
        }
        Entity: Entity {
           link: Entity
        }
    }
}
GameplayManager: {
    GameModeManager: Game Mode Manager {
       link: GameModeManager
    }
}

# Links :
BoardEngine.Coordinate -- MagicEngine.EntityEngine.EntityManager: {style.stroke-dash: 3}
MagicEngine.EntityEngine.EntityManager -- MagicEngine.EntityEngine.Movement: {style.stroke-dash: 3}
MagicEngine.EntityEngine.EntityManager -- MagicEngine.Spells.Spell: {style.stroke-dash: 3}
MagicEngine.EntityEngine.EntityManager -> MagicEngine.EntityEngine.Entity: Has {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
MagicEngine.EntityEngine.EntityManager -> GameplayManager.GameModeManager: Listen to {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}

```
---
# Summary :
name|description
----|----
[[#ClearEvent\|ClearEvent]] | `Setup the class, removing the listener on events`
[[#GetEntity\|GetEntity]] | `Return Entity at coordinate`
[[#GetEntities\|GetEntities]] | `Return all registered Entites`
[[#RegisterEntity\|RegisterEntity]] | `Add a new entity to the board`
[[#CellFree\|CellFree]] | `Check if a cell contains no entity`
[[#CellOccupied\|CellOccupied]] | `Check if a cell contains an entity`
[[#MoveEntity\|MoveEntity]] | `Move an Entity toward a Cell. Will check if destination cell is free, and will return a failing Movement if not.
Will also trigger animation move to`
[[#MoveEntity\|MoveEntity]] | `Move an Entity from a Cell toward another Cell. Will check if "from" cell is occupied,
and if destination cell is free, and will return a failing Movement if not.
Will also trigger animation move to`
[[#TpEntity\|TpEntity]] | `Tp an Entity to a Cell.
Will Trigger animation tp to, and also trigger a Telefrag if target cell is occupied.`
[[#TpEntity\|TpEntity]] | `Tp an Entity from a Cell to another Cell.
Will Trigger animation tp to, and also trigger a Telefrag if target cell is occupied.`
[[#Kill\|Kill]] | `Kill an Entity`
[[#Unregister\|Unregister]] | `Remove an Entity from the game (remove it from EntityManager, delete its gameobject)`
[[#Summons\|Summons]] | `Create an Entity linked to a summoner's spell`
[[#CreateEntity\|CreateEntity]] | `Create an Entity`
[[#InstantiateGameObject\|InstantiateGameObject]] | `Instantiate a Gameobject linked to an entityName`
[[#UpdateEntityCoordinate\|UpdateEntityCoordinate]] | `Update an Entity coordinate, without animating`

---
# Functions :

---
### ClearEvent
Setup the class, removing the listener on events

---
### GetEntity
Return Entity at coordinate

#### Parameters
name|type|description
-----|-----|-----
**coordinates**|[[Coordinate]]|Coordinate

#### Return
- [[Entity]] : Entity or null

---
### GetEntities
Return all registered Entites

#### Return
- `List<Entity>` : Entity list

---
### RegisterEntity
Add a new entity to the board

#### Parameters
name|type|description
-----|-----|-----
**entity**|[[Entity]]|Entity to register
**coordinates**|[[Coordinate]]|Coordiantes

---
### CellFree
Check if a cell contains no entity

#### Parameters
name|type|description
-----|-----|-----
**coordinates**|[[Coordinate]]|Cell to check

#### Return
- `bool` : Boolean

---
### CellOccupied
Check if a cell contains an entity

#### Parameters
name|type|description
-----|-----|-----
**coordinates**|[[Coordinate]]|Cell to check

#### Return
- `bool` : Boolean

---
### MoveEntity
Move an Entity toward a Cell. Will check if destination cell is free, and will return a failing Movement if not.
Will also trigger animation move to

#### Parameters
name|type|description
-----|-----|-----
**entity**|[[Entity]]|Entity to move to
**to**|[[Coordinate]]|Destination

#### Return
- [[Movement]] : Movement which correspond to the result of the function : NoDestination, Obstructed or Success

---
### MoveEntity
Move an Entity from a Cell toward another Cell. Will check if "from" cell is occupied,
and if destination cell is free, and will return a failing Movement if not.
Will also trigger animation move to

#### Parameters
name|type|description
-----|-----|-----
**from**|[[Coordinate]]|From
**to**|[[Coordinate]]|Destination

#### Return
- [[Movement]] : Movement which correspond to the result of the function :
NoEntity, NoDestination, Obstructed or Success

---
### TpEntity
Tp an Entity to a Cell.
Will Trigger animation tp to, and also trigger a Telefrag if target cell is occupied.

#### Parameters
name|type|description
-----|-----|-----
**entity**|[[Entity]]|Entity to tp to
**to**|[[Coordinate]]|Destination

#### Return
- [[Movement]] : Movement which correspond to the result of the function :
NoDestination, Telefrag or Success

---
### TpEntity
Tp an Entity from a Cell to another Cell.
Will Trigger animation tp to, and also trigger a Telefrag if target cell is occupied.

#### Parameters
name|type|description
-----|-----|-----
**from**|[[Coordinate]]|From
**to**|[[Coordinate]]|Destination

#### Return
- [[Movement]] : Movement which correspond to the result of the function :
NoDestination, Telefrag or Success

---
### Kill
Kill an Entity

#### Parameters
name|type|description
-----|-----|-----
**entity**|[[Entity]]|Entity

---
### Unregister
Remove an Entity from the game (remove it from EntityManager, delete its gameobject)

#### Parameters
name|type|description
-----|-----|-----
**entity**|[[Entity]]|Entity to unregister
**checkSummoner**|`bool`|Set this to false to not check if the entity is summoned by another one. Will cause issue if properly set to false

---
### Summons
Create an Entity linked to a summoner's spell

#### Parameters
name|type|description
-----|-----|-----
**summoner**|[[Entity]]|Entity summoning
**spell**|[[Spell]]|Summons linked to spell
**target**|[[Coordinate]]|Coordinate where to summon
**entityName**|`string`|Entity to summon

#### Return
- [[Entity]] : Return the summoned entity

---
### CreateEntity
Create an Entity

#### Parameters
name|type|description
-----|-----|-----
**target**|[[Coordinate]]|Coordinate where to create
**entityName**|`string`|Entity to summon
**checkCell**|`bool`|Verify if cell exist and is free

#### Return
- [[Entity]] : Return the created entity

---
### InstantiateGameObject
Instantiate a Gameobject linked to an entityName

#### Parameters
name|type|description
-----|-----|-----
**entityName**|`string`|Entity to Instantiate
**target**|[[Coordinate]]|Coordinate to create to

#### Return
- [[Entity]] : Return the instantiated entity

---
### UpdateEntityCoordinate
Update an Entity coordinate, without animating

#### Parameters
name|type|description
-----|-----|-----
**entity**|[[Entity]]|Entity to update
**coordinate**|[[Coordinate]]|coordinate
