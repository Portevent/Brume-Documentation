---
title: ImagePaletteEditor
path: /Builder/Editors
alias: 
- Image Palette Editor
tag: 
- class
---
Image Palette Editor  
```d2
# Nodes :
WorldGeneratorEngine: {
    Tools: {
        ToClean: {
            ColorsAndImages: {
                ImagePalette: Image Palette {
                   link: ImagePalette
                }
            }
        }
    }
}

# Links :
WorldGeneratorEngine.Tools.ToClean.ColorsAndImages.ImagePalette -- Builder.Editors.ImagePaletteEditor: {style.stroke-dash: 3}

```
---
# Summary :
name|description
----|----
[[#DebugActions\|DebugActions]] | `Create the Debug Actions`

---
# Functions :

---
### DebugActions
Create the Debug Actions

#### Return
- `VisualElement` : VisualElement
