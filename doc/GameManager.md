---
title: GameManager
alias: 
- Game Manager
tag: 
- class
---
Keep track of the [[Player]]

---
# Summary :
name|description
----|----
[[#PlayerCastSpell\|PlayerCastSpell]] | `Invoked when a spell is casted by the player. Delegate the effects application to MagicManager`
[[#OnTelefrag\|OnTelefrag]] | `When a telefrag is generated, cast the Telefrag spell from the DeckManager`
[[#PassTurn\|PassTurn]] | `Called when the player pass its turn`
[[#UpdateDestinationGlyph\|UpdateDestinationGlyph]] | `Set a Glyph on the destination to indicate the user its entity will move there`

---
### PlayerCastSpell
Invoked when a spell is casted by the player. Delegate the effects application to MagicManager

#### Parameters
name|type|description
-----|-----|-----
**spell**|[[Spell]]|Spell casted
**target**|[[Coordinate]]|Coordinate where the spell is casted

---
### OnTelefrag
When a telefrag is generated, cast the Telefrag spell from the DeckManager

---
### PassTurn
Called when the player pass its turn

---
### UpdateDestinationGlyph
Set a Glyph on the destination to indicate the user its entity will move there

#### Parameters
name|type|description
-----|-----|-----
**coordinates**|[[Coordinate]]|Coordinate where the player is going
