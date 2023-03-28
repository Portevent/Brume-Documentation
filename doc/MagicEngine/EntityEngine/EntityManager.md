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
MagicEngine: {
    EntityEngine: {
        Entity: Entity {
           link: Entity
        }
    }
}

# Links :
MagicEngine.EntityEngine.EntityManager -> MagicEngine.EntityEngine.Entity: Has {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}

```
---
# Summary :
name|description
----|----
[[#Unregister\|Unregister]] | `Remove an Entity from the game (remove it from EntityManager, delete its gameobject)`

---
# Functions :

---
### Unregister
Remove an Entity from the game (remove it from EntityManager, delete its gameobject)

#### Parameters
name|type|description
-----|-----|-----
**entity**|[[Entity]]|Entity to unregister
**checkSummoner**|`bool`|Set this to false to not check if the entity is summoned by another one. Will cause issue if properly set to false
