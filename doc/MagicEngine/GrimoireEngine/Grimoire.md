---
title: Grimoire
path: /MagicEngine/GrimoireEngine
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
    DimensionCoordinate: Dimension Coordinate {
       link: DimensionCoordinate
    }
}
SpellEngine: {
    Spell: Spell {
       link: Spell
    }
}
MagicEngine: {
    GrimoireEngine: {
        GrimoirePage: Grimoire Page {
           link: GrimoirePage
        }
    }
}

# Links :
MagicEngine.GrimoireEngine.Grimoire -- MagicEngine.GrimoireEngine.GrimoirePage: {style.stroke-dash: 3}
MagicEngine.GrimoireEngine.Grimoire -- SpellEngine.Spell: {style.stroke-dash: 3}
BoardEngine.DimensionCoordinate -- MagicEngine.GrimoireEngine.Grimoire: {style.stroke-dash: 3}

```
---
# Summary :
name|description
----|----
[[#AddSpell\|AddSpell]] | `Add a new Page with specified Spell`
[[#ReduceAllCooldown\|ReduceAllCooldown]] | `Reduce all cooldown durations`
[[#GetFirstValidPage\|GetFirstValidPage]] | `Get the first page that is not on cooldown`
[[#GetFirstValidPageOnTarget\|GetFirstValidPageOnTarget]] | `Get the first page that is not on cooldown and can be cast on target`
[[#GetFirstValidPageOnCell\|GetFirstValidPageOnCell]] | `Get the first page that is not on cooldown and can be cast on cell`
[[#ResetAllCooldown\|ResetAllCooldown]] | `Set all cooldowns to 0`

---
# Functions :

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
- [[GrimoirePage]] : Page, or null if all are on cooldown

---
### GetFirstValidPageOnTarget
Get the first page that is not on cooldown and can be cast on target

#### Parameters
name|type|description
-----|-----|-----
**caster**|`IEntity`|Caster
**target**|`IEntity`|Entity targeted

#### Return
- [[GrimoirePage]] : Page, or null if all are on cooldown

---
### GetFirstValidPageOnCell
Get the first page that is not on cooldown and can be cast on cell

#### Parameters
name|type|description
-----|-----|-----
**caster**|`IEntity`|Caster
**target**|[[DimensionCoordinate]]|Cell targeted

#### Return
- [[GrimoirePage]] : Page, or null if all are on cooldown

---
### ResetAllCooldown
Set all cooldowns to 0
