---
title: AnimationTrigger
path: /AnimationEngine
alias: 
- Animation Trigger
tag: 
- struct
---
Hold data about what animation a SpellEffect will trigger  
AnimationTrigger are present in SpellEffect, and when Magic process their effect, it will process AnimationTrigger and register them to the AnimationManager  
```d2
# Nodes :
MagicEngine: {
    Spells: {
        SpellEffect: Spell Effect {
           link: SpellEffect
        }
    }
}

# Links :
MagicEngine.Spells.SpellEffect -> AnimationEngine.AnimationTrigger: Has {
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}

```