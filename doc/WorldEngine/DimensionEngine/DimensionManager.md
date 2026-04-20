---
title: DimensionManager
path: /WorldEngine/DimensionEngine
alias: 
- Dimension Manager
tag: 
- class
---
DimensionManager manage different Dimension, and create an empty new Dimension when a generator requires one  
```d2
# Nodes :
BoardEngine: {
    BoardManager: Board Manager {
       link: BoardManager
    }
}
WorldEngine: {
    DimensionEngine: {
        Dimension: Dimension {
           link: Dimension
        }
    }
}

# Links :
WorldEngine.DimensionEngine.Dimension -- WorldEngine.DimensionEngine.DimensionManager: {style.stroke-dash: 3}
WorldEngine.DimensionEngine.DimensionManager -> BoardEngine.BoardManager: Get active Dimension {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}

```
---
# Summary :
name|description
----|----
[[#DimensionExists\|DimensionExists]] | `Checks if a dimension with the given ID is registered`
[[#GetDimension\|GetDimension]] | `Gets a dimension by its ID`
[[#Create\|Create]] | `Create a new dimension in the register`
[[#NewDimension\|NewDimension]] | `Create a new Dimension`
[[#SetActiveDimension\|SetActiveDimension]] | `Sets the active dimension by ID`
[[#ClearActiveDimension\|ClearActiveDimension]] | `Clears the active dimension (sets it to null)`
[[#Delete\|Delete]] | `Unregisters a dimension by its ID`

---
# Functions :

---
### DimensionExists
Checks if a dimension with the given ID is registered

#### Parameters
name|type|description
-----|-----|-----
**dimensionName**|`DimensionName`|The dimension ID to check

#### Return
- `bool` : True if the dimension is registered, false otherwise

---
### GetDimension
Gets a dimension by its ID

#### Parameters
name|type|description
-----|-----|-----
**dimensionName**|`DimensionName`|The dimension ID

#### Return
- [[Dimension]] : The dimension if found, null otherwise

---
### Create
Create a new dimension in the register

#### Parameters
name|type|description
-----|-----|-----
**dimensionName**|`DimensionName`|The dimension to register

#### Exceptions
- `ArgumentNullException` : Thrown when dimension is null
- `ArgumentException` : Thrown when dimension ID is null or empty
- `InvalidOperationException` : Thrown when a dimension with the same ID is already registered

---
### NewDimension
Create a new Dimension

#### Parameters
name|type|description
-----|-----|-----
**dimensionName**|`DimensionName`|

#### Return
- [[Dimension]] : 

---
### SetActiveDimension
Sets the active dimension by ID

#### Parameters
name|type|description
-----|-----|-----
**dimensionName**|`DimensionName`|The Name of the dimension to set as active
**blurPrevious**|`bool`|If set to true, will blur previous dimension instead of plain hiding it 

#### Exceptions
- `ArgumentException` : 
Thrown when dimensionId is null or empty, or when no dimension with the given ID is
registered


---
### ClearActiveDimension
Clears the active dimension (sets it to null)

---
### Delete
Unregisters a dimension by its ID

#### Parameters
name|type|description
-----|-----|-----
**dimensionName**|`DimensionName`|The ID of the dimension to unregister

#### Return
- `void` : True if the dimension was unregistered, false if it wasn't registered
