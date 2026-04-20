---
title: DimensionCanvasTilemap
path: /WorldEngine/CanvasEngine
alias: 
- Dimension Canvas Tilemap
tag: 
- class
---
CanvasTilemap are Canvas that are linked to a tilemap  
```d2
# Nodes :
BoardEngine: {
    Coordinate: Coordinate {
       link: Coordinate
    }
}
WorldEngine: {
    CanvasEngine: {
        Cell: Cell {
           link: Cell
        }
    }
}

# Links :
BoardEngine.Coordinate -- WorldEngine.CanvasEngine.DimensionCanvasTilemap: {style.stroke-dash: 3}
WorldEngine.CanvasEngine.Cell -- WorldEngine.CanvasEngine.DimensionCanvasTilemap: {style.stroke-dash: 3}

```
---
# Summary :
name|description
----|----
[[#RegisterTilemap\|RegisterTilemap]] | `Register current tilemap and make it visible`
[[#UnregisterTilemap\|UnregisterTilemap]] | `Unregister current Tilemap and make it less visible`
[[#DisplayAllCell\|DisplayAllCell]] | `Display all cells on Tilemap`
[[#UpdateCell\|UpdateCell]] | `Specification of UpdateCell to update Tilemap`
[[#OnNewCell\|OnNewCell]] | `On new cell, display it on the tilemap`
[[#ToChangeData\|ToChangeData]] | `Convert all Cells to ChangeData for bulk Tilemap edit`
[[#UpdateBoardFromTilemapEvent\|UpdateBoardFromTilemapEvent]] | `Convert Tilemap event to changes among Cell`
[[#ImportTilemap\|ImportTilemap]] | `Import data from Unity Tilemap`

---
# Functions :

---
### RegisterTilemap
Register current tilemap and make it visible

---
### UnregisterTilemap
Unregister current Tilemap and make it less visible

---
### DisplayAllCell
Display all cells on Tilemap

---
### UpdateCell
Specification of UpdateCell to update Tilemap

#### Parameters
name|type|description
-----|-----|-----
**coordinate**|[[Coordinate]]|
**cell**|[[Cell]]|

---
### OnNewCell
On new cell, display it on the tilemap

#### Parameters
name|type|description
-----|-----|-----
**coordinate**|[[Coordinate]]|Coordinate
**cell**|[[Cell]]|Cell

---
### ToChangeData
Convert all Cells to ChangeData for bulk Tilemap edit

#### Return
- `TileChangeData[]` : TileChangeData[]

---
### UpdateBoardFromTilemapEvent
Convert Tilemap event to changes among Cell

#### Parameters
name|type|description
-----|-----|-----
**updatedTilemap**|`Tilemap`|Tilemap that raise the events
**tiles**|`Tilemap.SyncTile[]`|Events

---
### ImportTilemap
Import data from Unity Tilemap

#### Parameters
name|type|description
-----|-----|-----
**newTilemap**|`Tilemap`|Tilemap
