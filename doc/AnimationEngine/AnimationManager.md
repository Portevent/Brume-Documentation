---
title: AnimationManager
path: /AnimationEngine
alias: 
- Animation Manager
tag: 
- class
---
Register all animations that must be play and process them
Animations are queued as [[AnimationData]] object, and animation are played first in first out
If an Entity is not Ready, the current animation will wait for it and thus delay all the other
```d2
# Nodes :
MagicEngine: {
    EntityEngine: {
        EntityAnimator: Entity Animator {
           link: EntityAnimator
        }
    }
}
AnimationEngine: {
    AnimatorProcessor: Animator Processor {
       link: AnimatorProcessor
    }
    AnimationData: Animation Data {
       link: AnimationData
    }
}

# Links :
AnimationEngine.AnimationManager -> AnimationEngine.AnimationData: Process {
source-arrowhead: {}
target-arrowhead: Queue of{shape: arrow}
}
AnimationEngine.AnimationManager -> MagicEngine.EntityEngine.EntityAnimator: Animate {
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
AnimationEngine.AnimatorProcessor -> AnimationEngine.AnimationManager: Process Queue every tick {
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}

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
