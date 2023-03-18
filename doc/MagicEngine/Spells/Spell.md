#class 
A Spell can be casted to apply several effect.
Each Spell has a name, description and sprite describing it

The casting condition account for 6 things :
- The cost of the spell (WIP feature, not used yet)
- The cooldown of the spell (in turns, before it can be casted again)
- The minimum and maximum range (minRange & maxRange). The targeted cell must be within that range
Note : casting a spell 0 tiles away mean casting on itself
- a castPattern for how the cast can be done (diagonal, in square, circle etc...)
- a list of SpellCondition (must cast on free spell, must not cast on target with Telefrag)

The casting effect are applied according to a Pattern (cast)
Each entity within that pattern undergo the effect
The order of application is from closest to farthest (from target cell)
ties break by orientation (polar coordinates centered at target)
All effects are applied before changing target
