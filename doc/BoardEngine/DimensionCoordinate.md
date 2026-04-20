---
title: DimensionCoordinate
path: /BoardEngine
alias: 
- Dimension Coordinate
tag: 
- class
---
Coordinate system used to move around Dimension  
Similar to Coordinates, but with a DimensionName field, so it removes the ambiguity of same coordinate in different dimensions  
```d2
# Nodes :
EntityEngine: {
    EntityManagement: {
        EntityRegistry: Entity Registry {
           link: EntityRegistry
        }
    }
}
MagicEngine: {
    MagicManager: Magic Manager {
       link: MagicManager
    }
    GrimoireEngine: {
        Grimoire: Grimoire {
           link: Grimoire
        }
    }
}

# Links :
BoardEngine.DimensionCoordinate -- EntityEngine.EntityManagement.EntityRegistry: {style.stroke-dash: 3}
BoardEngine.DimensionCoordinate -- MagicEngine.MagicManager: {style.stroke-dash: 3}
BoardEngine.DimensionCoordinate -- MagicEngine.GrimoireEngine.Grimoire: {style.stroke-dash: 3}

```