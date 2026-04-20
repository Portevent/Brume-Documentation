---
title: QuickPainter
path: /WorldGeneratorEngine/Tools
alias: 
- Quick Painter
tag: 
- class
---
Helper class to operate on DimensionCanvases  
```d2
# Nodes :
BoardEngine: {
    Coordinate: Coordinate {
       link: Coordinate
    }
}
WorldEngine: {
    CanvasEngine: {
        DimensionCanvas: Dimension Canvas {
           link: DimensionCanvas
        }
    }
}

# Links :
BoardEngine.Coordinate -- WorldGeneratorEngine.Tools.QuickPainter: {style.stroke-dash: 3}
WorldEngine.CanvasEngine.DimensionCanvas -- WorldGeneratorEngine.Tools.QuickPainter: {style.stroke-dash: 3}

```
---
# Summary :
name|description
----|----
[[#Picker\|Picker]] | `Select all Coordinates that match color from a given position`

---
# Functions :

---
### Picker
Select all Coordinates that match color from a given position

#### Parameters
name|type|description
-----|-----|-----
**canvas**|[[DimensionCanvas]]|Canvas
**from**|[[Coordinate]]|Origin of zone
**color**|`Color`|Color that must match (if none, use the color of source)

#### Return
- `HashSet<Coordinate>` : 
