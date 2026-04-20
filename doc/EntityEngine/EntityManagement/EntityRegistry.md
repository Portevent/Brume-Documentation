---
title: EntityRegistry
path: /EntityEngine/EntityManagement
alias: 
- Entity Registry
tag: 
- class
---
Keep track of all [[Positional]], and register / unregister them as needed  
```d2
# Nodes :
EntityEngine: {
    EntityComposition: {
        в_Positional: {
            Positional: Positional {
               link: Positional
            }
        }
        с_Entity: {
            Entity: Entity {
               link: Entity
            }
        }
    }
}

# Links :
EntityEngine.EntityComposition.с_Entity.Entity -- EntityEngine.EntityManagement.EntityRegistry: {style.stroke-dash: 3}
EntityEngine.EntityManagement.EntityRegistry -> EntityEngine.EntityComposition.в_Positional.Positional: Has {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}

```
---
# Summary :
name|description
----|----
[[#Register\|Register]] | `Register Positional`
[[#Unregister\|Unregister]] | `Unregister Positional`
[[#TryGet\|TryGet]] | `Get Positional at coordinate (or null)`
[[#Get\|Get]] | `Get Positional`
[[#GetAllInAllDimensions\|GetAllInAllDimensions]] | `Check if a cell contains a Positional`

---
# Functions :

---
### Register
Register Positional

---
### Unregister
Unregister Positional

---
### TryGet
Get Positional at coordinate (or null)

#### Return
- [[Entity]] : Positional or null

---
### Get
Get Positional

#### Parameters
name|type|description
-----|-----|-----
**coordinates**|`DimensionCoordinate`|DimensionCoordinate

#### Return
- [[Entity]] : Positional

#### Exceptions
- `InvalidOperationException` : 

---
### GetAllInAllDimensions
Check if a cell contains a Positional

#### Return
- `IReadOnlyList<Entity>` : Boolean
