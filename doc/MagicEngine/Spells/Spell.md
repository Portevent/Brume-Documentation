---
title: Spell
path: /MagicEngine/Spells
alias: 
- Spell
tag: 
- class
---
A Spell can be casted to apply several effect.
Each Spell has a name, description and sprite describing it

The casting condition account for 6 things :
- The cost of the spell (WIP feature, not used yet)
- The cooldown of the spell (in turns, before it can be casted again)
- The minimum and maximum range (minRange & maxRange). The targeted cell must be within that range
Note : casting a spell 0 tiles away mean casting on itself
- a castPattern for how the cast can be done (diagonal, in square, circle etc...)
- a list of SpellCondition (must cast on free spell, must not cast on target with Telefrag)

The casting effect are applied according to a Pattern (cast)
Each entity within that pattern undergo the effect
The order of application is from closest to farthest (from target cell)
ties break by orientation (polar coordinates centered at target)
All effects are applied before changing target
```d2
# Nodes :
MagicEngine: {
    Spells: {
        Grimoire: Grimoire {
           link: Grimoire
        }
    }
    EntityEngine: {
        AI: {
            IntentAI: IntentAI {
               link: IntentAI
            }
        }
    }
    MagicManager: Magic Manager {
       link: MagicManager
    }
}

# Links :
MagicEngine.Spells.Grimoire -- MagicEngine.Spells.Spell: {style.stroke-dash: 3}
MagicEngine.MagicManager -- MagicEngine.Spells.Spell: {style.stroke-dash: 3}
MagicEngine.Spells.Spell -> MagicEngine.EntityEngine.AI.IntentAI: Can have intent {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}

```