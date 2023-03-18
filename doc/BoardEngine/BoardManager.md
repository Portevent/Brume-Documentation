#class 
Use the [[WorldManager]] to compute existing cell ([[Coordinate]]) and free cell toward/away.
Also communicate with [[EntityManager]] to determine if a cell is free.

---
# Summary :
name|description
----|----
[[#CellFree\|CellFree]] | `Determinate if a cell is free (cell exist and no entity there)`

---
### CellFree
Determinate if a cell is free (cell exist and no entity there)

#### Parameters
name|type|description
-----|-----|-----
**coordinates**|[[Coordinate]]|

#### Return
- `bool` : 
