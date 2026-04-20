---
title: SpellEffect
path: /SpellEngine
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

# Links :
MagicEngine.MagicManager -- SpellEngine.SpellEffect: {style.stroke-dash: 3}

```