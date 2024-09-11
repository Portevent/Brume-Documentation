---
title: Grimoire
path: /MagicEngine/Spells
alias: 
- Grimoire
tag: 
- class
---
A grimoire represent the ability of entity to cast spell  
Grimoire hold a list of usable spell and their cooldown.  
```d2
# Nodes :
BoardEngine: {
    Coordinate: Coordinate {
       link: Coordinate
    }
}
MagicEngine: {
    EntityEngine: {
        AI: {
            PlayerAI: PlayerAI {
               link: PlayerAI
            }
            BasicEnemyAI: Basic EnemyAI {
               link: BasicEnemyAI
            }
        }
    }
    Spells: {
        GrimoirePage: Grimoire Page {
           link: GrimoirePage
        }
        Spell: Spell {
           link: Spell
        }
    }
}

# Links :
BoardEngine.Coordinate -- MagicEngine.Spells.Grimoire: {style.stroke-dash: 3}
MagicEngine.Spells.Grimoire -- MagicEngine.Spells.GrimoirePage: {style.stroke-dash: 3}
MagicEngine.Spells.Grimoire -- MagicEngine.Spells.Spell: {style.stroke-dash: 3}
MagicEngine.Spells.Grimoire -> MagicEngine.EntityEngine.AI.PlayerAI: Has {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
MagicEngine.Spells.Grimoire -> MagicEngine.EntityEngine.AI.BasicEnemyAI: Has {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}

```
---
# Summary :
name|description
----|----
[[#Awake\|Awake]] | `Take a list of spells and create a Grimoire with theses spells in the same order (0 to n)`
[[#AddSpell\|AddSpell]] | `Add a new Page with specified Spell`
[[#ReduceAllCooldown\|ReduceAllCooldown]] | `Reduce all cooldown durations`
[[#GetFirstValidPage\|GetFirstValidPage]] | `Get the first page that is not on cooldown`
[[#GetFirstValidPageOnTarget\|GetFirstValidPageOnTarget]] | `Get the first page that is not on cooldown and can be cast on target`
[[#GetFirstValidPageOnCell\|GetFirstValidPageOnCell]] | `Get the first page that is not on cooldown and can be cast on cell`

---
# Functions :

---
### Awake
Take a list of spells and create a Grimoire with theses spells in the same order (0 to n)

---
### AddSpell
Add a new Page with specified Spell

#### Parameters
name|type|description
-----|-----|-----
**spell**|[[Spell]]|Spell to add to the Grimoire
**position**|`int`|index where to set the Page (0 by default, first page)
**cooldown**|`int`|cooldown of the Spell once in the Grimoire

#### Return
- [[GrimoirePage]] : Return the Page linked to the Spell

---
### ReduceAllCooldown
Reduce all cooldown durations

#### Parameters
name|type|description
-----|-----|-----
**value**|`int`|number of turn to remove (-1 to reset it to 0)

---
### GetFirstValidPage
Get the first page that is not on cooldown

#### Return
- `Page` : Page, or null if all are on cooldown

---
### GetFirstValidPageOnTarget
Get the first page that is not on cooldown and can be cast on target

#### Parameters
name|type|description
-----|-----|-----
**target**|[[Entity]]|Entity targeted

#### Return
- `Page` : Page, or null if all are on cooldown

---
### GetFirstValidPageOnCell
Get the first page that is not on cooldown and can be cast on cell

#### Parameters
name|type|description
-----|-----|-----
**target**|[[Coordinate]]|Cell targeted

#### Return
- `Page` : Page, or null if all are on cooldown
