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
AnimationEngine: {
    AnimationTrigger: Animation Trigger {
       link: AnimationTrigger
    }
}
MagicEngine: {
    MagicManager: Magic Manager {
       link: MagicManager
    }
}

# Links :
MagicEngine.MagicManager -- MagicEngine.Spells.SpellEffect: {style.stroke-dash: 3}
MagicEngine.Spells.SpellEffect -> AnimationEngine.AnimationTrigger: Has {
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}

```