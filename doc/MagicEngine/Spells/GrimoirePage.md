---
title: GrimoirePage
path: /MagicEngine/Spells
alias: 
- Grimoire Page
tag: 
- class
---
A Grimoire Page represent a Spell within a Grimoire, tracking its cooldown  
```d2
# Nodes :
MagicEngine: {
    Spells: {
        Grimoire: Grimoire {
           link: Grimoire
        }
    }
}

# Links :
MagicEngine.Spells.Grimoire -- MagicEngine.Spells.GrimoirePage: {style.stroke-dash: 3}

```
---
# Summary :
name|description
----|----
[[#AddCooldown\|AddCooldown]] | `Add cooldown duration`
[[#ReduceCooldown\|ReduceCooldown]] | `Reduce cooldown duration`
[[#ApplyCooldown\|ApplyCooldown]] | `Set a page cooldown to its spell cooldown duration`

---
# Functions :

---
### AddCooldown
Add cooldown duration

#### Parameters
name|type|description
-----|-----|-----
**value**|`int`|number of turn to add

---
### ReduceCooldown
Reduce cooldown duration

#### Parameters
name|type|description
-----|-----|-----
**value**|`int`|number of turn to remove (-1 to reset it to 0)

---
### ApplyCooldown
Set a page cooldown to its spell cooldown duration

#### Return
- `int` : the cooldown duration applied
