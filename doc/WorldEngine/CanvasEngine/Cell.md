---
title: Cell
path: /WorldEngine/CanvasEngine
alias: 
- Cell
tag: 
- class
---
Cell that contains Color and Tile data  
```d2
# Nodes :
WorldEngine: {
    CanvasEngine: {
        DimensionCanvasTilemap: Dimension Canvas Tilemap {
           link: DimensionCanvasTilemap
        }
        DimensionCanvas: Dimension Canvas {
           link: DimensionCanvas
        }
    }
}

# Links :
WorldEngine.CanvasEngine.Cell -- WorldEngine.CanvasEngine.DimensionCanvasTilemap: {style.stroke-dash: 3}
WorldEngine.CanvasEngine.Cell -- WorldEngine.CanvasEngine.DimensionCanvas: {style.stroke-dash: 3}

```