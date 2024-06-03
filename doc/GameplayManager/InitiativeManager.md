---
title: InitiativeManager
path: /GameplayManager
alias: 
- Initiative Manager
tag: 
- class
---
Keep 3 list of [[Entity]] (Pre Player, Player, Post Player) that store in which order they will play  
```d2
# Nodes :
GameplayManager: {
    GameManager: Game Manager {
       link: GameManager
    }
}

# Links :
GameplayManager.InitiativeManager -> GameplayManager.GameManager: Get Initiative list {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}

```