---
title: BiomeGenerator
path: /BoardEngine/WorldEngine
alias: 
- Biome Generator
tag: 
- class
---
Basic Biome Generator
```d2
# Nodes :
BoardEngine: {
    WorldEngine: {
        World: World {
           link: World
        }
    }
}

# Links :
BoardEngine.WorldEngine.BiomeGenerator -- BoardEngine.WorldEngine.World: {style.stroke-dash: 3}

```
---
# Summary :
name|description
----|----
[[#Setup\|Setup]] | `Setup function called when World is created`

---
# Functions :

---
### Setup
Setup function called when World is created

#### Parameters
name|type|description
-----|-----|-----
**world**|[[World]]|Reference to the parent World

#### Exceptions
- `ArgumentOutOfRangeException` : 
