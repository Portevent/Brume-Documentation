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
BoardEngine: {
    Coordinate: Coordinate {
       link: Coordinate
    }
}
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
BoardEngine.Coordinate -- MagicEngine.EntityEngine.AI.PlayerAI: {style.stroke-dash: 3}
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
---
# Summary :
name|description
----|----
[[#CheckWorldInteraction\|CheckWorldInteraction]] | `Called when Player move around. If in quest mode, will allow interaction with WorldInteractionAction`
[[#PathFindTo\|PathFindTo]] | `PathFindToward a destination
Called by DeckManager`

---
# Functions :

---
### CheckWorldInteraction
Called when Player move around. If in quest mode, will allow interaction with WorldInteractionAction

#### Parameters
name|type|description
-----|-----|-----
**coordinate**|[[Coordinate]]|Coordinates

---
### PathFindTo
PathFindToward a destination
Called by DeckManager

#### Parameters
name|type|description
-----|-----|-----
**coordinate**|[[Coordinate]]|
