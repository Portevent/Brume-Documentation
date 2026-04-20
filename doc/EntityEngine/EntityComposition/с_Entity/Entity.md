---
title: Entity
path: /EntityEngine/EntityComposition/с_Entity
alias: 
- Entity
tag: 
- class
---
Entity are one of the main component of the world. They have a position within a Dimension, life bar and spells  
```d2
# Nodes :
EntityEngine: {
    EntityManagement: {
        EntityRegistry: Entity Registry {
           link: EntityRegistry
        }
    }
}

# Links :
EntityEngine.EntityComposition.с_Entity.Entity -- EntityEngine.EntityManagement.EntityRegistry: {style.stroke-dash: 3}

```