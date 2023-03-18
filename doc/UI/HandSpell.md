#class 
A HandSpell is a MonoBehaviour object that link a spell in the player's DeckManager to UI Button
It manage the icon and cooldown displayed
Currently the cooldown system is based on local cooldown value saved within HandSpell. Probably need to rework this
(this can cause glitch and abuse, and anyway not a good pattern

---
# Summary :
name|description
----|----
[[#Setup\|Setup]] | `Assign the Spell sprite to the button and set the cooldown to 0`
[[#SelectSpell\|SelectSpell]] | `Select this HandSpell as the active HandSpell.
This will notify the DeckManager`
[[#ApplyCooldown\|ApplyCooldown]] | `Apply the cooldown of the selected spell to the HandSpell`

---
### Setup
Assign the Spell sprite to the button and set the cooldown to 0

---
### SelectSpell
Select this HandSpell as the active HandSpell.
This will notify the DeckManager

---
### ApplyCooldown
Apply the cooldown of the selected spell to the HandSpell
