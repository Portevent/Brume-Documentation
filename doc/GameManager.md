#class 
Keep track of the [[Player]]

---
# Summary :
name|description
----|----
[[#PlayerCastSpell\|PlayerCastSpell]] | `Invoked when a spell is casted by the player. Delegate the effects application to MagicManager`
[[#OnTelefrag\|OnTelefrag]] | `When a telefrag is generated, cast the Telefrag spell from the DeckManager
The spell is casted on the player, and the entity which with the telefrag happened
(or the two entities if the telefrag has been made with two external entity)`
[[#PassTurn\|PassTurn]] | `Called when the player pass its turn`
[[#UpdateDestinationGlyph\|UpdateDestinationGlyph]] | `Called when the Player update its destination
Set a Glyph on the destination to indicate the user its entity will move there`

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
The spell is casted on the player, and the entity which with the telefrag happened
(or the two entities if the telefrag has been made with two external entity)

#### Parameters
name|type|description
-----|-----|-----
**movement**|[[Movement]]|The telefrag Movement

---
### PassTurn
Called when the player pass its turn

---
### UpdateDestinationGlyph
Called when the Player update its destination
Set a Glyph on the destination to indicate the user its entity will move there

#### Parameters
name|type|description
-----|-----|-----
**coordinates**|[[Coordinate]]|Coordinate where the player is going
