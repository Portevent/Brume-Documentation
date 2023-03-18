#class 
An entity represent a unit in the world, that move, interact and cast spell
A basic entity hold at least
- An EntityName : their name
- An EntityBehaviorEvent : an object holding all the basic even emitter for the entity (on move, on hit etc...)
- A Coordinate : its position
- Life and MaxLife : two float to represent the entity hp
- Alignment : enum for which an entity is friendly, neutral or enemy
- Instance : the gameobject associated
- summons : dictionnary, associating spell name with a list of Entity they summoned

- destination : coordinate where the entity is moving
- afflictions : list of afflictions

---
# Summary :
name|description
----|----
[[#Die\|Die]] | `Called when the Entity is killed.`
[[#Vanish\|Vanish]] | `Remove the gameobject associated to this entity`
[[#DebuffAfflictions\|DebuffAfflictions]] | `Reduce the duration of all Afflictions`

---
### Die
Called when the Entity is killed.

---
### Vanish
Remove the gameobject associated to this entity

---
### DebuffAfflictions
Reduce the duration of all Afflictions

#### Parameters
name|type|description
-----|-----|-----
**duration**|`int`|The number of turn to remove (-1 to clear all)
**state**|[[State]]|If set, only reduce afflictions corresponding to this state
