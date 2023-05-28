---
title: PlayerAI
path: /MagicEngine/EntityEngine/AI
alias: 
- PlayerAI
tag: 
- class
---
PlayerAI is an IntentAI that listen to InputManager to setup Intent and actually play turn
```d2
# Nodes :
UI: {
    InputManager: Input Manager {
       link: InputManager
    }
}
MagicEngine: {
    Spells: {
        Grimoire: Grimoire {
           link: Grimoire
        }
    }
    EntityEngine: {
        AI: {
            IntentAI: IntentAI {
               link: IntentAI
            }
        }
    }
}

# Links :
MagicEngine.EntityEngine.AI.IntentAI -> MagicEngine.EntityEngine.AI.PlayerAI: Inherits {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
UI.InputManager -> MagicEngine.EntityEngine.AI.PlayerAI: Input {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
MagicEngine.Spells.Grimoire -> MagicEngine.EntityEngine.AI.PlayerAI: Has {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}

```