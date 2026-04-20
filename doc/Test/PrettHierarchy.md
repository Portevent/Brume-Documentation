---
title: PrettHierarchy
path: /Test
alias: 
- Prett Hierarchy
tag: 
- class
---
Attribute to display class beatifully in the hierarchy windows  
It can have a custom background color (default is unity default color)  
```d2
# Nodes :
Test: {
    PrettHierarchy: Prett Hierarchy {
       link: PrettHierarchy
    }
}

# Links :

```
---
# Summary :
name|description
----|----
[[#Display\|Display]] | `Display PrettyHierarchy in the selectionRectangle`

---
# Functions :

---
### Display
Display PrettyHierarchy in the selectionRectangle

#### Parameters
name|type|description
-----|-----|-----
**selectionRect**|`Rect`|Rectangle to draw in
**attribute**|[[PrettHierarchy]]|PrettHierarchy
**obj**|`GameObject`|Associated gamobject
