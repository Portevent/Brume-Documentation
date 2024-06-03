---
title: EntityAnimatorEvent
path: /MagicEngine/EntityEngine
alias: 
- Entity Animator Event
tag: 
- class
---
An EntityAnimatorEvent is a link between an Animator and a EntityAnimator
An animator can have an EntityAnimatorEvent component on it to update any EntityAnimator linked to this animations  
When an Animator play an Animation (Unity behavior), the Animation can have keypoint that trigger function calls.
Animation can call function from EntityAnimatorEvent, which will forward the message to the linked EntityAnimator  
