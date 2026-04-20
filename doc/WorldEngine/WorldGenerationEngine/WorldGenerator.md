---
title: WorldGenerator
path: /WorldEngine/WorldGenerationEngine
alias: 
- World Generator
tag: 
- class
---
Manage a dictionary of DimensionGenerator mapped by name, so it can generate Dimensions on demand  
```d2
# Nodes :
WorldEngine: {
    DimensionEngine: {
        DimensionEntrance: Dimension Entrance {
           link: DimensionEntrance
        }
        Dimension: Dimension {
           link: Dimension
        }
    }
}

# Links :
WorldEngine.DimensionEngine.Dimension -- WorldEngine.WorldGenerationEngine.WorldGenerator: {style.stroke-dash: 3}
WorldEngine.DimensionEngine.DimensionEntrance -- WorldEngine.WorldGenerationEngine.WorldGenerator: {style.stroke-dash: 3}

```
---
# Summary :
name|description
----|----
[[#RegisterDimensionsGeneratorsFromCode\|RegisterDimensionsGeneratorsFromCode]] | `Automatically load dimension generators from a folder`
[[#CheckForMissingGenerators\|CheckForMissingGenerators]] | `Small unit test to verify that each dimension name has a dimension manager`
[[#Generate\|Generate]] | `Generate a new Dimension from its name`

---
# Functions :

---
### RegisterDimensionsGeneratorsFromCode
Automatically load dimension generators from a folder

---
### CheckForMissingGenerators
Small unit test to verify that each dimension name has a dimension manager

---
### Generate
Generate a new Dimension from its name

#### Parameters
name|type|description
-----|-----|-----
**dimensionName**|`DimensionName`|Dimension name
**entrance**|[[DimensionEntrance]]|If specified, will align new dimension entrance with this

#### Return
- [[Dimension]] : 
