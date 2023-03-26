---
title: AnimationManager
path: /AnimationEngine
alias: 
- Animation Manager
tag: 
- class
---
Register all animations that must be play and process them
Animations are queued as AnimationData object, and animation are played first in first out
If an Entity is not Ready, the current animation will wait for it and thus delay all the other
```d2
# Nodes :
AnimationEngine: {
    AnimationData: Animation Data
}

# Links :
AnimationEngine.AnimationData -- AnimationEngine.AnimationManager: {style.stroke-dash: 3}

```
---
# Summary :
name|description
----|----
[[#AddAnimation\|AddAnimation]] | `Queue a new animation`
[[#ProcessQueue\|ProcessQueue]] | `Process the next animation in the queue`

---
# Functions :

---
### AddAnimation
Queue a new animation

#### Parameters
name|type|description
-----|-----|-----
**animationData**|[[AnimationData]]|AnimationData to queue

---
### ProcessQueue
Process the next animation in the queue
