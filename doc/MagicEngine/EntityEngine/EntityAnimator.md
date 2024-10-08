---
title: EntityAnimator
path: /MagicEngine/EntityEngine
alias: 
- Entity Animator
tag: 
- class
---
An EntityAnimator represent the state in which an Entity is for the animation
The main parameter of an EntityAnimator is a boolean : ready
This indicate to the AnimationManager whether this is Entity is idle and ready to make an animation, or busy doing
one yet.  
Everytime "ready" change, AnimationManager.ProcessQueue() is called to check the next animation  
```d2
# Nodes :
AnimationEngine: {
    AnimationManager: Animation Manager {
       link: AnimationManager
    }
}
BoardEngine: {
    Coordinate: Coordinate {
       link: Coordinate
    }
}
MagicEngine: {
    EntityEngine: {
        Entity: Entity {
           link: Entity
        }
    }
}

# Links :
BoardEngine.Coordinate -- MagicEngine.EntityEngine.EntityAnimator: {style.stroke-dash: 3}
AnimationEngine.AnimationManager -> MagicEngine.EntityEngine.EntityAnimator: Animate {
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
MagicEngine.EntityEngine.EntityAnimator -> MagicEngine.EntityEngine.Entity: Linked to {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}

```
---
# Summary :
name|description
----|----
[[#ApplyMoveTo\|ApplyMoveTo]] | `Try to move toward MoveTo`
[[#TpTo\|TpTo]] | `Teleport to destination while playing the Tp Animation`
[[#BlinkTo\|BlinkTo]] | `Teleport to destination without playing any animation`
[[#Cast\|Cast]] | `Call the Cast animation`
[[#Hurt\|Hurt]] | `Call the Hurt animation`
[[#PrepareTp\|PrepareTp]] | `Call the PrepareTp animation`
[[#AnimationEnd\|AnimationEnd]] | `Called by EntityAnimatorEvent when the animator want to notify its animation is ended`

---
# Functions :

---
### ApplyMoveTo
Try to move toward MoveTo

---
### TpTo
Teleport to destination while playing the Tp Animation

#### Parameters
name|type|description
-----|-----|-----
**animationTarget**|[[Coordinate]]|Destination where to Tp

---
### BlinkTo
Teleport to destination without playing any animation

#### Parameters
name|type|description
-----|-----|-----
**animationTarget**|[[Coordinate]]|Destination where to Tp

---
### Cast
Call the Cast animation

---
### Hurt
Call the Hurt animation

---
### PrepareTp
Call the PrepareTp animation

---
### AnimationEnd
Called by EntityAnimatorEvent when the animator want to notify its animation is ended
