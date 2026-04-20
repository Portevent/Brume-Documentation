---
title: RuleTile
path: /WorldGeneratorEngine/Tools/ToClean/RuleTile
alias: 
- Rule Tile
tag: 
- struct
---
Rule Tile are tile with a defined orientation  
Quickly documented, to rewrite  
```d2
# Nodes :
WorldGeneratorEngine: {
    Tools: {
        ToClean: {
            RuleTile: {
                RuleTile: Rule Tile {
                   link: RuleTile
                }
            }
        }
    }
}

# Links :

```
---
# Summary :
name|description
----|----
[[#FromNeighbors\|FromNeighbors]] | `Create RuleTile from a list of neighbors`

---
# Functions :

---
### FromNeighbors
Create RuleTile from a list of neighbors

#### Parameters
name|type|description
-----|-----|-----
**neighbors**|`bool[]`|List of the surrounding Tiles
**randomOrientation**|`bool`|For symmetric tiles, set orientation to first possible or random among possibles

#### Return
- [[RuleTile]] : RuleTile

#### Exceptions
- `ArgumentOutOfRangeException` : 
