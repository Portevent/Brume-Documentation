---
title: DimensionEntrance
path: /WorldEngine/DimensionEngine
alias: 
- Dimension Entrance
tag: 
- class
---
Dimension Entrance representing specific point in a dimension mapped by a name  
```d2
# Nodes :
WorldEngine: {
    WorldGenerationEngine: {
        WorldGenerator: World Generator {
           link: WorldGenerator
        }
    }
}

# Links :
WorldEngine.DimensionEngine.DimensionEntrance -- WorldEngine.WorldGenerationEngine.WorldGenerator: {style.stroke-dash: 3}

```