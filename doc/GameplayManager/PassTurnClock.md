---
title: PassTurnClock
path: /GameplayManager
alias: 
- Pass Turn Clock
tag: 
- class
---
Tempo giver for the pass turn mechanic
```d2
# Nodes :
GameplayManager: {
    GameModeManager: Game Mode Manager {
       link: GameModeManager
    }
}

# Links :
GameplayManager.PassTurnClock -> GameplayManager.GameModeManager: Get tempo from {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}

```