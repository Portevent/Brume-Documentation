---
title: GameManager
path: /GameplayManager
alias: 
- Game Manager
tag: 
- class
---
Keep track of the Player
```d2
# Nodes :
BoardEngine: {
    ChunkManager: Chunk Manager {
       link: ChunkManager
    }
}
MagicEngine: {
    EntityEngine: {
        AI: {
            BasicEnemyAI: Basic EnemyAI {
               link: BasicEnemyAI
            }
        }
        Entity: Entity {
           link: Entity
        }
    }
    MagicManager: Magic Manager {
       link: MagicManager
    }
}
GameplayManager: {
    InitiativeManager: Initiative Manager {
       link: InitiativeManager
    }
}

# Links :
GameplayManager.GameManager -> MagicEngine.EntityEngine.AI.BasicEnemyAI: Get Player {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
GameplayManager.GameManager -> MagicEngine.MagicManager: Cast Player's spells {
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
GameplayManager.GameManager -> MagicEngine.MagicManager: Cast Telefrag {
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
MagicEngine.EntityEngine.Entity -> GameplayManager.GameManager: Listen for OnTelefrag {
source-arrowhead: Player{}
target-arrowhead: {shape: arrow}
}
GameplayManager.GameManager -> BoardEngine.ChunkManager: Update Player coordinate {
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
GameplayManager.InitiativeManager -> GameplayManager.GameManager: Get Initiative list {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
GameplayManager.GameManager -> MagicEngine.EntityEngine.Entity: Play Turn {
source-arrowhead: {}
target-arrowhead: All Entity{shape: arrow}
}

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
