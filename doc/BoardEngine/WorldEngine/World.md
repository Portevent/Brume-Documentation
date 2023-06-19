---
title: World
path: /BoardEngine/WorldEngine
alias: 
- World
tag: 
- class
---
Hold information about a Biome
Use a [[WorldGenerator]] to feed it with tile
```d2
# Nodes :
BoardEngine: {
    ChunkManager: Chunk Manager {
       link: ChunkManager
    }
    WorldEngine: {
        CoolNoiseGenerator: Cool Noise Generator {
           link: CoolNoiseGenerator
        }
        WorldManager: World Manager {
           link: WorldManager
        }
        BiomeGenerator: Biome Generator {
           link: BiomeGenerator
        }
        AdvancedWorldGenerator: Advanced World Generator {
           link: AdvancedWorldGenerator
        }
        WorldGenerator: World Generator {
           link: WorldGenerator
        }
    }
}

# Links :
BoardEngine.WorldEngine.CoolNoiseGenerator -- BoardEngine.WorldEngine.World: {style.stroke-dash: 3}
BoardEngine.WorldEngine.BiomeGenerator -- BoardEngine.WorldEngine.World: {style.stroke-dash: 3}
BoardEngine.WorldEngine.AdvancedWorldGenerator -- BoardEngine.WorldEngine.World: {style.stroke-dash: 3}
BoardEngine.ChunkManager -> BoardEngine.WorldEngine.World: Load Chunks {
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
BoardEngine.ChunkManager -> BoardEngine.WorldEngine.World: Unload Chunks {
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
BoardEngine.WorldEngine.WorldGenerator -> BoardEngine.WorldEngine.World: Generated by {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
BoardEngine.WorldEngine.WorldManager -> BoardEngine.WorldEngine.World: Instantiate {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}

```
---
# Summary :
name|description
----|----
[[#AddWorldInteractiveElement\|AddWorldInteractiveElement]] | `Add a World Interactive Element to this world and register all the tiles from which it is accessible`
[[#RemoveWorldInteractiveElement\|RemoveWorldInteractiveElement]] | `Remove a World Interactive Element from this world and unregister all the tiles from which it was accessible`

---
# Functions :

---
### AddWorldInteractiveElement
Add a World Interactive Element to this world and register all the tiles from which it is accessible

#### Parameters
name|type|description
-----|-----|-----
**element**|`WorldInteractiveElement`|Element to register

---
### RemoveWorldInteractiveElement
Remove a World Interactive Element from this world and unregister all the tiles from which it was accessible

#### Parameters
name|type|description
-----|-----|-----
**element**|`WorldInteractiveElement`|Element to unregister