---
title: Coordinate
path: /BoardEngine
alias: 
- Coordinate
tag: 
- class
---
Base Coordinate system used for the Board
```d2
# Nodes :
BoardEngine: {
    AreaMaker: Area Maker
    BoardManager: Board Manager
}
GameManager: Game Manager
UI: {
    DeckManager: Deck Manager
}
MagicEngine: {
    Entity: {
        EntityAnimator: Entity Animator
        Entity: Entity
    }
    MagicManager: Magic Manager
}

# Links :
BoardEngine.AreaMaker -- BoardEngine.Coordinate: {style.stroke-dash: 3}
BoardEngine.Coordinate -- GameManager: {style.stroke-dash: 3}
BoardEngine.Coordinate -- UI.DeckManager: {style.stroke-dash: 3}
BoardEngine.Coordinate -- MagicEngine.Entity.EntityAnimator: {style.stroke-dash: 3}
BoardEngine.Coordinate -- MagicEngine.MagicManager: {style.stroke-dash: 3}
BoardEngine.BoardManager -- BoardEngine.Coordinate: {style.stroke-dash: 3}

```