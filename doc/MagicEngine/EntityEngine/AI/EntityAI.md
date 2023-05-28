---
title: EntityAI
path: /MagicEngine/EntityEngine/AI
alias: 
- EntityAI
tag: 
- class
---
An EntityAI is an object computing what an entity will do on its turn, and how it behave
A basic EntityAI has at least a Destination where it will move
```d2
# Nodes :
MagicEngine: {
    EntityEngine: {
        Entity: Entity {
           link: Entity
        }
        AI: {
            IntentAI: IntentAI {
               link: IntentAI
            }
        }
    }
}

# Links :
MagicEngine.EntityEngine.Entity <-> MagicEngine.EntityEngine.AI.EntityAI: Play turn {
source-arrowhead: {shape: arrow}
target-arrowhead: {shape: arrow}
}
MagicEngine.EntityEngine.AI.EntityAI -> MagicEngine.EntityEngine.AI.IntentAI: Inherits {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}

```