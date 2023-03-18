#class 
Register all animations that must be play and process them
Animations are queued as AnimationData object, and animation are played first in first out
If an Entity is not Ready, the current animation will wait for it and thus delay all the other

---
# Summary :
name|description
----|----
[[#AddAnimation\|AddAnimation]] | `Queue a new animation`
[[#ProcessQueue\|ProcessQueue]] | `Process the next animation in the queue`

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
