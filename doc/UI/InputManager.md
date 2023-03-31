---
title: InputManager
path: /UI
alias: 
- Input Manager
tag: 
- class
---
InputManager hold all the command an user can input :
- Tile hovered
- Tile clicked
- Spell selected

Each have an event associated for when that value is changed

Hold a InputType value, for whether the user use a mouse or a controller

It is also linked to the DeckManager
```d2
# Nodes :
MagicEngine: {
    EntityEngine: {
        AI: {
            PlayerAI: PlayerAI {
               link: PlayerAI
            }
        }
    }
}

# Links :
UI.InputManager -> MagicEngine.EntityEngine.AI.PlayerAI: Input {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}

```