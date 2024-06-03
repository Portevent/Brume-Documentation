---
title: CoolNoiseGenerator
path: /BoardEngine/WorldEngine
alias: 
- Cool Noise Generator
tag: 
- class
---
Semi random procedural WorldGenerator, using hotspots to generate smooth cloud.  
Clone of CoolNoiseGenerator. The class is in StandBy while working on BiomeGenerator, and will be
rework to support chunk generation and Biome system  

---
# Summary :
name|description
----|----
[[#SetupGenerator\|SetupGenerator]] | `Setup function called when World is created`
[[#GetNoiseValue\|GetNoiseValue]] | `Generate a value from the parameted noise, that range from Min to Max (or -1 if outside of Noise)`
[[#GetHeightValue\|GetHeightValue]] | `Generate a value from GetNoiseValue, that range from Min to Max (or -1 if outside of Noise)`

---
# Functions :

---
### SetupGenerator
Setup function called when World is created

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
