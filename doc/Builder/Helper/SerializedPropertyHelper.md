---
title: SerializedPropertyHelper
path: /Builder/Helper
alias: 
- Serialized Property Helper
tag: 
- class
---
SerializedPropertyHelper  

---
# Summary :
name|description
----|----
[[#GetSelf\|GetSelf]] | `Return the serialized instance from its parent`
[[#GetValue\|GetValue]] | `Get a child from a source`
[[#GetValue\|GetValue]] | `Get the n-th element of a child from a source`

---
# Functions :

---
### GetSelf
Return the serialized instance from its parent

#### Parameters
name|type|description
-----|-----|-----
**prop**|`SerializedProperty`|Serialized Property

#### Return
- `object` : Property

---
### GetValue
Get a child from a source

#### Parameters
name|type|description
-----|-----|-----
**source**|`object`|Parent
**name**|`string`|name of the child

#### Return
- `object` : object

---
### GetValue
Get the n-th element of a child from a source

#### Parameters
name|type|description
-----|-----|-----
**source**|`object`|Parent
**name**|`string`|name of the child
**index**|`int`|Index in the list to fetch

#### Return
- `object` : object
