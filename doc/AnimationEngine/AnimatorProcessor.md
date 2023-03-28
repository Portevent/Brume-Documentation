---
title: AnimatorProcessor
path: /AnimationEngine
alias: 
- Animator Processor
tag: 
- class
---
MonoBehaviour Object that calls [[AnimationManager]].ProcessQueue() every tick
```d2
# Nodes :
AnimationEngine: {
    AnimationManager: Animation Manager {
       link: AnimationManager
    }
}

# Links :
AnimationEngine.AnimatorProcessor -> AnimationEngine.AnimationManager: Process Queue every tick {
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}

```
---
# Summary :
name|description
----|----
[[#Update\|Update]] | `Calls [[AnimationManager]].ProcessQueue() every tick`

---
# Functions :

---
### Update
Calls [[AnimationManager]].ProcessQueue() every tick
