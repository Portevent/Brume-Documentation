---
title: GameModeManager
path: /GameplayManager
alias: 
- Game Mode Manager
tag: 
- class
---
Start and stop QuestMode based on the number of Enemy [[Entity]]
Hold a passturn event (trigger every time Quest Mode's end turn is called) that will be plug and unpluged to [[GameManager]].PassTurn()  
```d2
# Nodes :
MagicEngine: {
    EntityEngine: {
        EntityManager: Entity Manager {
           link: EntityManager
        }
    }
}
GameplayManager: {
    GameManager: Game Manager {
       link: GameManager
    }
    PassTurnClock: Pass Turn Clock {
       link: PassTurnClock
    }
}

# Links :
MagicEngine.EntityEngine.EntityManager -> GameplayManager.GameModeManager: Listen to {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
GameplayManager.PassTurnClock -> GameplayManager.GameModeManager: Get tempo from {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
GameplayManager.GameModeManager -> GameplayManager.GameManager: Pass turns {
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}

```