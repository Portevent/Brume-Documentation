---
title: GrimoirePage
path: /MagicEngine/GrimoireEngine
alias: 
- Grimoire Page
tag: 
- class
---
A Grimoire Page is a spell entry in a grimoire, with an attached cooldown  
```d2
# Nodes :
MagicEngine: {
    GrimoireEngine: {
        Grimoire: Grimoire {
           link: Grimoire
        }
    }
}

# Links :
MagicEngine.GrimoireEngine.Grimoire -- MagicEngine.GrimoireEngine.GrimoirePage: {style.stroke-dash: 3}

```
---
# Summary :
name|description
----|----
[[#AddCooldown\|AddCooldown]] | `Add cooldown duration`
[[#ClearCooldown\|ClearCooldown]] | `Clear cooldown duration`
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
### ClearCooldown
Clear cooldown duration

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
