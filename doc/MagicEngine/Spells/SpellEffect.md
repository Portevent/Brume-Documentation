---
title: SpellEffect
path: /MagicEngine/Spells
alias: 
- Spell Effect
tag: 
- struct
---
A Spell's effect
```d2
# Nodes :
MagicEngine: {
    MagicManager: Magic Manager {
       link: MagicManager
    }
}
AnimationEngine: {
    AnimationTrigger: Animation Trigger {
       link: AnimationTrigger
    }
}

# Links :
MagicEngine.MagicManager -- MagicEngine.Spells.SpellEffect: {style.stroke-dash: 3}
MagicEngine.Spells.SpellEffect -> AnimationEngine.AnimationTrigger: Has {
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}

```