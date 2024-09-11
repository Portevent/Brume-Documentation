---
title: Entity
path: /MagicEngine/EntityEngine
alias: 
- Entity
tag: 
- class
---
An entity represent a unit in the world, that move, interact and cast spell
A basic entity hold at least
- An EntityName : their name
- An EntityBehaviorEvent : an object holding all the basic even emitter for the entity (on move, on hit etc...)
- A Coordinate : its position
- Life and MaxLife : two float to represent the entity hp
- Alignment : enum for which an entity is friendly, neutral or enemy
- Instance : the gameobject associated
- summons : dictionnary, associating spell name with a list of Entity they summoned

- destination : coordinate where the entity is moving
- afflictions : list of afflictions  
```d2
# Nodes :
GameplayManager: {
    GameManager: Game Manager {
       link: GameManager
    }
}
BoardEngine: {
    Coordinate: Coordinate {
       link: Coordinate
    }
}
MagicEngine: {
    EntityEngine: {
        AI: {
            IntentAI: IntentAI {
               link: IntentAI
            }
            EntityAI: EntityAI {
               link: EntityAI
            }
        }
        EntityManager: Entity Manager {
           link: EntityManager
        }
        EntityAnimator: Entity Animator {
           link: EntityAnimator
        }
        State: State {
           link: State
        }
    }
}

# Links :
MagicEngine.EntityEngine.Entity -> GameplayManager.GameManager: Listen for OnTelefrag {
source-arrowhead: Player{}
target-arrowhead: {shape: arrow}
}
GameplayManager.GameManager -> MagicEngine.EntityEngine.Entity: Play Turn {
source-arrowhead: {}
target-arrowhead: All Entity{shape: arrow}
}
MagicEngine.EntityEngine.Entity -> MagicEngine.EntityEngine.AI.IntentAI: Can have pinned target {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
MagicEngine.EntityEngine.EntityManager -> MagicEngine.EntityEngine.Entity: Has {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
MagicEngine.EntityEngine.Entity <-> MagicEngine.EntityEngine.AI.EntityAI: Play turn {
source-arrowhead: {shape: arrow}
target-arrowhead: {shape: arrow}
}
MagicEngine.EntityEngine.Entity -> MagicEngine.EntityEngine.State: Has {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
MagicEngine.EntityEngine.Entity -> BoardEngine.Coordinate: Has {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
MagicEngine.EntityEngine.EntityAnimator -> MagicEngine.EntityEngine.Entity: Linked to {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}

```
---
# Summary :
name|description
----|----
[[#Die\|Die]] | `Called when the Entity is killed.`
[[#Vanish\|Vanish]] | `Remove the gameobject associated to this entity`
[[#DebuffAfflictions\|DebuffAfflictions]] | `Reduce the duration of all Afflictions`

---
# Functions :

---
### Die
Called when the Entity is killed.

---
### Vanish
Remove the gameobject associated to this entity

---
### DebuffAfflictions
Reduce the duration of all Afflictions

#### Parameters
name|type|description
-----|-----|-----
**duration**|`int`|The number of turn to remove (-1 to clear all)
**state**|[[State]]|If set, only reduce afflictions corresponding to this state
