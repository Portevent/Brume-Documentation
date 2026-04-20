---
title: Positional
path: /EntityEngine/EntityComposition/в_Positional
alias: 
- Positional
tag: 
- class
---
Positional is a MonoBehaviour object that has a Coordinate and a Dimension  
It can be moved, and will raise PositionnableEvent  
```d2
# Nodes :
EntityEngine: {
    EntityManagement: {
        EntityRegistry: Entity Registry {
           link: EntityRegistry
        }
    }
}
BoardEngine: {
    Coordinate: Coordinate {
       link: Coordinate
    }
}

# Links :
BoardEngine.Coordinate -- EntityEngine.EntityComposition.в_Positional.Positional: {style.stroke-dash: 3}
EntityEngine.EntityManagement.EntityRegistry -> EntityEngine.EntityComposition.в_Positional.Positional: Has {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}

```
---
# Summary :
name|description
----|----
[[#SilentlyMove\|SilentlyMove]] | `Change the coordinate without raising an OnMove event`

---
# Functions :

---
### SilentlyMove
Change the coordinate without raising an OnMove event

#### Parameters
name|type|description
-----|-----|-----
**newCoordinate**|[[Coordinate]]|Coordinate
