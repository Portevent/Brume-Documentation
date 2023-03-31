---
title: IntentAI
path: /MagicEngine/EntityEngine/AI
alias: 
- IntentAI
tag: 
- class
---
An IntentAI is an AI able to expresses Intent to do specific action
An Intent is made of :
- a Spell to cast
- a list of Coordinate to indicate potential targets
```d2
# Nodes :
BoardEngine: {
    SelectionManager: Selection Manager {
       link: SelectionManager
    }
    Coordinate: Coordinate {
       link: Coordinate
    }
}
MagicEngine: {
    EntityEngine: {
        AI: {
            PlayerAI: PlayerAI {
               link: PlayerAI
            }
            EntityAI: EntityAI {
               link: EntityAI
            }
            BasicEnemyAI: Basic EnemyAI {
               link: BasicEnemyAI
            }
        }
        Entity: Entity {
           link: Entity
        }
    }
    Spells: {
        Spell: Spell {
           link: Spell
        }
    }
}

# Links :
MagicEngine.EntityEngine.AI.IntentAI -> BoardEngine.SelectionManager: Shows Intent {
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
MagicEngine.EntityEngine.AI.EntityAI -> MagicEngine.EntityEngine.AI.IntentAI: Inherits {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
MagicEngine.Spells.Spell -> MagicEngine.EntityEngine.AI.IntentAI: Can have intent {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
MagicEngine.EntityEngine.Entity -> MagicEngine.EntityEngine.AI.IntentAI: Can have pinned target {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
BoardEngine.Coordinate -> MagicEngine.EntityEngine.AI.IntentAI: Can have fix target {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
MagicEngine.EntityEngine.AI.IntentAI -> MagicEngine.EntityEngine.AI.PlayerAI: Inherits {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}
MagicEngine.EntityEngine.AI.IntentAI -> MagicEngine.EntityEngine.AI.BasicEnemyAI: Inherits {style.stroke-dash: 3
source-arrowhead: {}
target-arrowhead: {shape: arrow}
}

```