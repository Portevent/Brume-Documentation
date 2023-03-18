#class 
BasicEnemyAI is a AI that will use a grimoir to cast spell on Player
It will always try to take the first available spell in the grimoir, and intent to cast it on the player
If it can't cast any spell on the player, it will move toward it

---
# Summary :
name|description
----|----
[[#CastIntent\|CastIntent]] | `Cast the intended spell, and apply its cooldown in the grimoire`
[[#DefaultBehavior\|DefaultBehavior]] | `Default Behavior of the enemy if it can't cast a spell : moving toward Player`
[[#FindIntent\|FindIntent]] | `Attempt to find an Intent
BasicEnemyAI just take the first valid spell in its grimoir and cast it on the player`

---
### CastIntent
Cast the intended spell, and apply its cooldown in the grimoire

---
### DefaultBehavior
Default Behavior of the enemy if it can't cast a spell : moving toward Player

---
### FindIntent
Attempt to find an Intent
BasicEnemyAI just take the first valid spell in its grimoir and cast it on the player
