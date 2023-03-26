---
title: AnimationData
path: /AnimationEngine
alias: 
- Animation Data
tag: 
- struct
---
Structure holding data about an [[Entity]] doing an entityAnimation.
Can hold a list of [[Entity]] to wait for
AnimationData are queued inside [[AnimationManager]], and are resolved one by one
```d2
# Nodes :
AnimationEngine: {
    AnimationManager: Animation Manager
}

# Links :
AnimationEngine.AnimationData -- AnimationEngine.AnimationManager: {style.stroke-dash: 3}

```