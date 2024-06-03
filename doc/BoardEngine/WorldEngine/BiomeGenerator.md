---
title: BiomeGenerator
path: /BoardEngine/WorldEngine
alias: 
- Biome Generator
tag: 
- class
---
Abstract class that define the basis of a Biome
Biome are generated chunk by chunk (a cache is populated when ChunkManager ask to prepare a zone)  
Biome can spawn mobGroups and prop along the generation.
The RNG is seeded (need to review if done correctly)  
