---
title: GameManager
path: 
alias: 
- Game Manager
tag: 
- class
---
Keep track of the Player
```d2
# Nodes :
BoardEngine: {
    Coordinate: Coordinate
}
MagicEngine: {
    Entity: {
        Entity: Entity
        Movement: Movement
    }
    Spells: {
        Spell: Spell
    }
}

# Links :
BoardEngine.Coordinate -- GameManager: {style.stroke-dash: 3}
GameManager -- MagicEngine.Spells.Spell: {style.stroke-dash: 3}
GameManager -- MagicEngine.Entity.Movement: {style.stroke-dash: 3}

```
---
# Summary :
name|description
----|----
[[#PlayerCastSpell\|PlayerCastSpell]] | `Invoked when a spell is casted by the player. Delegate the effects application to MagicManager`
[[#OnTelefrag\|OnTelefrag]] | `When a telefrag is generated, cast the Telefrag spell from the DeckManager`
[[#PassTurn\|PassTurn]] | `Called when the player pass its turn`
[[#UpdateDestinationGlyph\|UpdateDestinationGlyph]] | `Set a Glyph on the destination to indicate the user its entity will move there`

---
# Functions :

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

#### Parameters
name|type|description
-----|-----|-----
**movement**|[[Movement]]|The telefrag Movement

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
