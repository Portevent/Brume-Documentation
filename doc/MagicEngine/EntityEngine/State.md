---
title: State
path: /MagicEngine/EntityEngine
alias: 
- State
tag: 
- class
---
A state correspond to a modification
```d2
# Nodes :
MagicEngine: {
    EntityEngine: {
        Entity: Entity {
           link: Entity
        }
    }
}

# Links :
MagicEngine.EntityEngine.Entity -> MagicEngine.EntityEngine.State: Has {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}

```