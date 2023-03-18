#struct 
A SpellCondition is a struct that summarize 4 information :
- type : What is the ConditionType (cell occupied, free, has a state, alignment)
- target : Where to apply the condition (on self, on target, or any entity)
- data : For state / alignment / name check, hold the data to compare to
- @operator : MustBe or MustNotBe
