---
title: Area
path: /BoardEngine
alias: 
- Area
tag: 
- class
---
Blueprint of a selection of tile, contains a Pattern and a range  
```d2
# Nodes :
BoardEngine: {
    AreaMaker: Area Maker {
       link: AreaMaker
    }
}

# Links :
BoardEngine.Area -> BoardEngine.AreaMaker: Convert an Area to... {
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}

```