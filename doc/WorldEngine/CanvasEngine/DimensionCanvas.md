---
title: DimensionCanvas
path: /WorldEngine/CanvasEngine
alias: 
- Dimension Canvas
tag: 
- class
---
Canvas are a set of Coordinate linking to Cell (color and tile)  
```d2
# Nodes :
BoardEngine: {
    Coordinate: Coordinate {
       link: Coordinate
    }
}
WorldEngine: {
    DimensionEngine: {
        Dimension: Dimension {
           link: Dimension
        }
    }
    CanvasEngine: {
        Cell: Cell {
           link: Cell
        }
    }
}
WorldGeneratorEngine: {
    Tools: {
        QuickPainter: Quick Painter {
           link: QuickPainter
        }
    }
}

# Links :
BoardEngine.Coordinate -- WorldEngine.CanvasEngine.DimensionCanvas: {style.stroke-dash: 3}
WorldEngine.DimensionEngine.Dimension -- WorldEngine.CanvasEngine.DimensionCanvas: {style.stroke-dash: 3}
WorldEngine.CanvasEngine.DimensionCanvas -- WorldGeneratorEngine.Tools.QuickPainter: {style.stroke-dash: 3}
WorldEngine.CanvasEngine.Cell -- WorldEngine.CanvasEngine.DimensionCanvas: {style.stroke-dash: 3}

```
---
# Summary :
name|description
----|----
[[#GetCell\|GetCell]] | `Get Cell`
[[#GetCell\|GetCell]] | `Get Cell`
[[#CellExists\|CellExists]] | `Check if Cell exists`
[[#SetCell\|SetCell]] | `Set Cell`
[[#SetCell\|SetCell]] | `Set Cell`
[[#SetCell\|SetCell]] | `Set Cell`
[[#SetCell\|SetCell]] | `Set Cell`
[[#SetCell\|SetCell]] | `Set Cell (use default creator)`
[[#SetCell\|SetCell]] | `Set Cell (use default creator)`
[[#RemoveCell\|RemoveCell]] | `Remove Cell`
[[#UpdateCell\|UpdateCell]] | `Called when a Cell Color or Till is updated`
[[#OnNewCell\|OnNewCell]] | `Called when a new Cell is created`
[[#GetAllCells\|GetAllCells]] | `Return all Cells`
[[#Clear\|Clear]] | `Clear all Cells`
[[#GetDefaultCell\|GetDefaultCell]] | `Create a Default Cell for when only color is specified`

---
# Functions :

---
### GetCell
Get Cell

#### Parameters
name|type|description
-----|-----|-----
**position**|`Vector3Int`|position

#### Return
- [[Cell]] : Cell

---
### GetCell
Get Cell

#### Parameters
name|type|description
-----|-----|-----
**coordinate**|[[Coordinate]]|coordinate

#### Return
- [[Cell]] : Cell

---
### CellExists
Check if Cell exists

#### Parameters
name|type|description
-----|-----|-----
**coordinate**|[[Coordinate]]|coordinate

#### Return
- `bool` : Bool

---
### SetCell
Set Cell

#### Parameters
name|type|description
-----|-----|-----
**position**|`Vector3Int`|position
**cell**|[[Cell]]|Cell

---
### SetCell
Set Cell

#### Parameters
name|type|description
-----|-----|-----
**position**|`Vector3Int`|position
**tilebase**|`TileBase`|Tilebase

---
### SetCell
Set Cell

#### Parameters
name|type|description
-----|-----|-----
**position**|`Vector3Int`|position
**tilebase**|`TileBase`|Tilebase
**color**|`Color`|Color

---
### SetCell
Set Cell

#### Parameters
name|type|description
-----|-----|-----
**coordinate**|[[Coordinate]]|coordinate
**tilebase**|`TileBase`|Tilebase

---
### SetCell
Set Cell (use default creator)

#### Parameters
name|type|description
-----|-----|-----
**coordinate**|[[Coordinate]]|coordinate
**cell**|[[Cell]]|Cell

---
### SetCell
Set Cell (use default creator)

#### Parameters
name|type|description
-----|-----|-----
**coordinate**|[[Coordinate]]|coordinate
**color**|`Color`|color

---
### RemoveCell
Remove Cell

#### Parameters
name|type|description
-----|-----|-----
**coordinate**|[[Coordinate]]|coordinate

---
### UpdateCell
Called when a Cell Color or Till is updated

#### Parameters
name|type|description
-----|-----|-----
**coordinate**|[[Coordinate]]|Coordinate of cell
**cell**|[[Cell]]|Cell updated

---
### OnNewCell
Called when a new Cell is created

#### Parameters
name|type|description
-----|-----|-----
**coordinate**|[[Coordinate]]|Coordinate of cell
**cell**|[[Cell]]|Cell created

---
### GetAllCells
Return all Cells

#### Return
- `List<Cell>` : Cells

---
### Clear
Clear all Cells

---
### GetDefaultCell
Create a Default Cell for when only color is specified

#### Parameters
name|type|description
-----|-----|-----
**coordinate**|[[Coordinate]]|Coordinate
**color**|`Color`|Color

#### Return
- [[Cell]] : Cell
