---
title: BasicEnemyAI
path: /MagicEngine/EntityEngine/AI
alias: 
- Basic EnemyAI
tag: 
- class
---
BasicEnemyAI is a AI that will use a grimoir to cast spell on Player
It will always try to take the first available spell in the grimoir, and intent to cast it on the player
If it can't cast any spell on the player, it will move toward it
```d2
# Nodes :
MagicEngine: {
    EntityEngine: {
        AI: {
            IntentAI: IntentAI {
               link: IntentAI
            }
        }
    }
    Spells: {
        Grimoire: Grimoire {
           link: Grimoire
        }
    }
}
GameplayManager: {
    GameManager: Game Manager {
       link: GameManager
    }
}

# Links :
MagicEngine.EntityEngine.AI.IntentAI -> MagicEngine.EntityEngine.AI.BasicEnemyAI: Inherits {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
MagicEngine.Spells.Grimoire -> MagicEngine.EntityEngine.AI.BasicEnemyAI: Has {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
GameplayManager.GameManager -> MagicEngine.EntityEngine.AI.BasicEnemyAI: Get Player {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}

```
---
# Summary :
name|description
----|----
[[#CastIntent\|CastIntent]] | `Cast the intended spell, and apply its cooldown in the grimoire`
[[#DefaultBehavior\|DefaultBehavior]] | `Default Behavior of the enemy if it can't cast a spell : moving toward Player`
[[#FindIntent\|FindIntent]] | `Attempt to find an Intent
BasicEnemyAI just take the first valid spell in its grimoir and cast it on the player`

---
# Functions :

---
### CastIntent
Cast the intended spell, and apply its cooldown in the grimoire

---
### DefaultBehavior
Default Behavior of the enemy if it can't cast a spell : moving toward Player

---
### FindIntent
Attempt to find an Intent
BasicEnemyAI just take the first valid spell in its grimoir and cast it on the player
