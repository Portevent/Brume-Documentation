---
title: Movement
path: /MagicEngine/Entity
alias: 
- Movement
tag: 
- struct
---
A movement contains two [[Coordinate]], `from` and `to`, to represent an Entity moving.
It has a Result, that can be either `Success`, `NoEntity`, `Obstructed`, `NoDestination`, `Telefrag
```d2
# Nodes :
GameManager: Game Manager

# Links :
GameManager -- MagicEngine.Entity.Movement: {style.stroke-dash: 3}

```