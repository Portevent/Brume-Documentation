---
title: Image
path: /WorldGeneratorEngine/Tools/ToClean/ColorsAndImages
alias: 
- Image
tag: 
- class
---
Image is a list of Colors in a rectangle  

---
# Summary :
name|description
----|----
[[#GetColorAt\|GetColorAt]] | `Return the Color at X, Y`
[[#GetColorAt\|GetColorAt]] | `Return the Color at X, Y (with orientation)`
[[#GetColorAt\|GetColorAt]] | `Return the nth Color`
[[#GetColorRow\|GetColorRow]] | `Return a row of Color`
[[#GetColorsAt\|GetColorsAt]] | `Return a part of the image`
[[#GetSubImages\|GetSubImages]] | `Return all possible sub images from images that match sub size`

---
# Functions :

---
### GetColorAt
Return the Color at X, Y

#### Parameters
name|type|description
-----|-----|-----
**x**|`int`|X
**y**|`int`|Y

#### Return
- `Color` : Color

---
### GetColorAt
Return the Color at X, Y (with orientation)

#### Parameters
name|type|description
-----|-----|-----
**x**|`int`|X
**y**|`int`|Y
**orientation**|`int`|orientation

#### Return
- `Color` : Color

---
### GetColorAt
Return the nth Color

#### Parameters
name|type|description
-----|-----|-----
**n**|`int`|N

#### Return
- `Color` : Color

---
### GetColorRow
Return a row of Color

#### Parameters
name|type|description
-----|-----|-----
**x**|`int`|Start from X (inclusive)
**x2**|`int`|End at X (inclusive)
**y**|`int`|Y

#### Return
- `List<Color>` : List of Colors

---
### GetColorsAt
Return a part of the image

#### Parameters
name|type|description
-----|-----|-----
**startX**|`int`|Start from X (inclusive)
**endX**|`int`|End at X (inclusive)
**startY**|`int`|Start from Y (inclusive)
**endY**|`int`|End at Y (inclusive)

#### Return
- `List<Color>` : 

---
### GetSubImages
Return all possible sub images from images that match sub size

#### Parameters
name|type|description
-----|-----|-----
**subwidth**|`int`|
**subheight**|`int`|

#### Return
- `List<Image>` : 
