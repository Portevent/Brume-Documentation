---
title: Dimension
path: /WorldEngine/DimensionEngine
alias: 
- Dimension
tag: 
- class
---
World is divided in multiple layer, called Dimension  
Entities are positioned on a Dimension, and can only interact with other element
on the same Dimension  
```d2
# Nodes :
WorldEngine: {
    DimensionEngine: {
        DimensionManager: Dimension Manager {
           link: DimensionManager
        }
    }
    CanvasEngine: {
        DimensionCanvas: Dimension Canvas {
           link: DimensionCanvas
        }
    }
    WorldGenerationEngine: {
        WorldGenerator: World Generator {
           link: WorldGenerator
        }
    }
}

# Links :
WorldEngine.DimensionEngine.Dimension -- WorldEngine.CanvasEngine.DimensionCanvas: {style.stroke-dash: 3}
WorldEngine.DimensionEngine.Dimension -- WorldEngine.DimensionEngine.DimensionManager: {style.stroke-dash: 3}
WorldEngine.DimensionEngine.Dimension -- WorldEngine.WorldGenerationEngine.WorldGenerator: {style.stroke-dash: 3}

```
---
# Summary :
name|description
----|----
[[#new\|new]] | `The main canvas that entities can pass through`
[[#AddCanvas\|AddCanvas]] | `Adds a canvas to this dimension`
[[#RemoveCanvas\|RemoveCanvas]] | `Removes a canvas from this dimension`
[[#GetAdditionalCanvases\|GetAdditionalCanvases]] | `Gets all canvases except the passable canvas`

---
# Functions :

---
### new
The main canvas that entities can pass through

---
### AddCanvas
Adds a canvas to this dimension

#### Parameters
name|type|description
-----|-----|-----
**dimensionCanvas**|[[DimensionCanvas]]|The canvas to add
**canvasName**|`string`|Optionnal canvas name

#### Exceptions
- `ArgumentNullException` : Thrown when canvas is null

---
### RemoveCanvas
Removes a canvas from this dimension

#### Parameters
name|type|description
-----|-----|-----
**dimensionCanvas**|[[DimensionCanvas]]|The canvas to remove

#### Return
- `bool` : True if the canvas was removed, false if it wasn't found

#### Exceptions
- `InvalidOperationException` : Thrown when trying to remove the passable canvas

---
### GetAdditionalCanvases
Gets all canvases except the passable canvas

#### Return
- `IEnumerable<DimensionCanvas>` : Collection of additional canvases
