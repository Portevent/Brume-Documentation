---
title: NoiseWorldGenerator
path: /BoardEngine/WorldEngine
alias: 
- Noise World Generator
tag: 
- class
---
Scriptable Object that hold [[WorldGenerationParameter]] used by a semi random procedural world builder.
For a given [[Coordinate]], will return a list of Tile.

---
# Summary :
name|description
----|----
[[#GetHeightValue\|GetHeightValue]] | `Generate a value from GetNoiseValue, that range from Min to Max (or -1 if outside of Noise)`

---
# Functions :

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
