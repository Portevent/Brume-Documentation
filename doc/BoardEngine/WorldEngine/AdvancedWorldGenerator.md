---
title: AdvancedWorldGenerator
path: /BoardEngine/WorldEngine
alias: 
- Advanced World Generator
tag: 
- class
---
Semi random procedural WorldGenerator, using hotspots to generate smooth cloud.
Clone of CoolNoiseGenerator. The class is in StandBy while working on BiomeGenerator, and will be
rework to support chunk generation and Biome system
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
BoardEngine.WorldEngine.AdvancedWorldGenerator -- BoardEngine.WorldEngine.World: {style.stroke-dash: 3}

```
---
# Summary :
name|description
----|----
[[#Setup\|Setup]] | `Setup function called when World is created`
[[#GetNoiseValue\|GetNoiseValue]] | `Generate a value from the parameted noise, that range from Min to Max (or -1 if outside of Noise)`
[[#GetHeightValue\|GetHeightValue]] | `Generate a value from GetNoiseValue, that range from Min to Max (or -1 if outside of Noise)`

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

---
### GetNoiseValue
Generate a value from the parameted noise, that range from Min to Max (or -1 if outside of Noise)

#### Parameters
name|type|description
-----|-----|-----
**x**|`int`|Coordinate
**y**|`int`|Coordinate

#### Return
- `float` : 

---
### GetHeightValue
Generate a value from GetNoiseValue, that range from Min to Max (or -1 if outside of Noise)

#### Parameters
name|type|description
-----|-----|-----
**x**|`int`|Coordinate
**y**|`int`|Coordinate

#### Return
- `int` : 
