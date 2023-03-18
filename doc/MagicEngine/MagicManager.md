#class 
ManicManager is a class used for processing SpellEffect

---
# Summary :
name|description
----|----
[[#Cast\|Cast]] | `Cast a spell on a target`
[[#CastEffect\|CastEffect]] | `Execute a spellEffect`
[[#ValidateEntity\|ValidateEntity]] | `Check if a SpellEffect is valid on an entity and can be applied on it`
[[#ValidatePlayerSpellConditions\|ValidatePlayerSpellConditions]] | `Check if a Spell can be casted by the player on a target (from player position)`
[[#ValidateSpellRange\|ValidateSpellRange]] | `Check if a caster can cast a spell from a point to a target (validate range Condition)`
[[#ValidateSpellConditions\|ValidateSpellConditions]] | `Check if a caster can cast a spell from a point to a target (validate all SpellCondition)`
[[#ValidateCondition\|ValidateCondition]] | `Validate a single SpellCondition`

---
### Cast
Cast a spell on a target

#### Parameters
name|type|description
-----|-----|-----
**spell**|[[Spell]]|Spell being casted
**caster**|[[Entity]]|Entity casting the spell
**origin**|[[Coordinate]]|Coordinate from which the spell is casted
**target**|[[Coordinate]]|Coordinate on which the spell is casted

---
### CastEffect
Execute a spellEffect

#### Parameters
name|type|description
-----|-----|-----
**spell**|[[Spell]]|The spell from which the effect is from
**caster**|[[Entity]]|Entity casting the spell
**effect**|`SpellEffect`|The effect being casted
**origin**|[[Coordinate]]|Coordinate from which the spell is casted
**target**|[[Coordinate]]|Coordinate on which the spell is casted

#### Exceptions
- `ArgumentOutOfRangeException` : 

---
### ValidateEntity
Check if a SpellEffect is valid on an entity and can be applied on it

#### Parameters
name|type|description
-----|-----|-----
**effect**|`SpellEffect`|SpellEffect being process
**target**|[[Entity]]|The targeted entity
**caster**|[[Entity]]|The entity casting the SpellEffect (used for criteria like "is an ally")

#### Return
- `bool` : A boolean, true if the entity is valid and this SpellEffect can be applied on it

#### Exceptions
- `ArgumentOutOfRangeException` : unknown Criteria

---
### ValidatePlayerSpellConditions
Check if a Spell can be casted by the player on a target (from player position)

#### Parameters
name|type|description
-----|-----|-----
**spell**|[[Spell]]|Spell intended
**target**|[[Coordinate]]|Target intended

#### Return
- `bool` : boolean, true if the spell can be cast on that tile

---
### ValidateSpellRange
Check if a caster can cast a spell from a point to a target (validate range Condition)

#### Parameters
name|type|description
-----|-----|-----
**spell**|[[Spell]]|Spell intended
**caster**|[[Entity]]|Entity trying to cast the spell
**origin**|[[Coordinate]]|from which the spell is casted
**target**|[[Coordinate]]|target where the spell is intended 

#### Return
- `bool` : boolean, true if the spell can be cast on that tile

---
### ValidateSpellConditions
Check if a caster can cast a spell from a point to a target (validate all SpellCondition)

#### Parameters
name|type|description
-----|-----|-----
**spell**|[[Spell]]|Spell intended
**caster**|[[Entity]]|Entity trying to cast the spell
**origin**|[[Coordinate]]|from which the spell is casted
**target**|[[Coordinate]]|target where the spell is intended 

#### Return
- `bool` : boolean, true if the spell can be cast on that tile

#### Exceptions
- `ArgumentOutOfRangeException` : unknown ConditionOperator

---
### ValidateCondition
Validate a single SpellCondition

#### Parameters
name|type|description
-----|-----|-----
**spell**|[[Spell]]|Spell intended
**condition**|[[SpellCondition]]|SpellCondition tested
**caster**|[[Entity]]|Entity trying to cast the spell
**origin**|[[Coordinate]]|from which the spell is casted
**target**|[[Coordinate]]|target where the spell is intended 

#### Return
- `bool` : boolean, true if the SpellCondition is validated

#### Exceptions
- `InvalidSpellCondition` : the SpellCondition has a format error
- `ArgumentOutOfRangeException` : unknown ConditionType
