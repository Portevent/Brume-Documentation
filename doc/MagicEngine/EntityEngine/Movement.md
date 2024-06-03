---
title: Movement
path: /MagicEngine/EntityEngine
alias: 
- Movement
tag: 
- struct
---
A movement contains two [[Coordinate]], `from` and `to`, to represent an Entity moving.
It has a Result, that can be either `Success`, `NoEntity`, `Obstructed`, `NoDestination`, `Telefrag  
```d2
# Nodes :
MagicEngine: {
    EntityEngine: {
        EntityManager: Entity Manager {
           link: EntityManager
        }
    }
}

# Links :
MagicEngine.EntityEngine.EntityManager -- MagicEngine.EntityEngine.Movement: {style.stroke-dash: 3}

```