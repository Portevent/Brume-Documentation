#class 
Convert Area to Coordinates[]

---
# Summary :
name|description
----|----
[[#GetArea\|GetArea]] | `Convert an Area to a list of valid Coordinate`
[[#CoordinateInPattern\|CoordinateInPattern]] | `Check if a coordinate meet the rules of the pattern`
[[#IsCoordinateValid\|IsCoordinateValid]] | `Check if a coordinate meet the requirement of the pattern.
3 different check are valuated :
- Coordinates in pattern (e.g. the coordinate is on a diagonal or a line for a star pattern)
- Coordinates in minimal range (if the coordinates is beyond the minimal range)
- Coordinates in maximal range (if the coordinates doesn't not exceed the maximal range)`
[[#CoordinateInMinimalRange\|CoordinateInMinimalRange]] | `Check if a coordinate is beyond the minimal range of the patten`
[[#CoordinateInMaxRange\|CoordinateInMaxRange]] | `Check if a coordinate is below the maximal range of the patten`

---
### GetArea
Convert an Area to a list of valid Coordinate

#### Parameters
name|type|description
-----|-----|-----
**area**|[[Area]]|Area defining pattern and range
**origin**|[[Coordinate]]|From where the area come from (used only for "Self" area)
**target**|[[Coordinate]]|Where to compute the area

#### Return
- `Coordinate[]` : 

---
### CoordinateInPattern
Check if a coordinate meet the rules of the pattern

#### Parameters
name|type|description
-----|-----|-----
**coordinate**|[[Coordinate]]|The coordinates to check
**pattern**|`Pattern`|The pattern to use

#### Return
- `bool` : True if the coordinate is inside the pattern shape

---
### IsCoordinateValid
Check if a coordinate meet the requirement of the pattern.
3 different check are valuated :
- Coordinates in pattern (e.g. the coordinate is on a diagonal or a line for a star pattern)
- Coordinates in minimal range (if the coordinates is beyond the minimal range)
- Coordinates in maximal range (if the coordinates doesn't not exceed the maximal range)

#### Parameters
name|type|description
-----|-----|-----
**coordinate**|[[Coordinate]]|The coordinates to check
**area**|[[Area]]|The Area to compare to

#### Return
- `bool` : A boolean:
True if the coordinate is contains within the pattern
False otherwise


---
### CoordinateInMinimalRange
Check if a coordinate is beyond the minimal range of the patten

#### Parameters
name|type|description
-----|-----|-----
**coordinate**|[[Coordinate]]|The coordinates to check
**pattern**|`Pattern`|The pattern to use
**minRange**|`int`|Minimum range

#### Return
- `bool` : True if the coordinate is not below the minimal range

---
### CoordinateInMaxRange
Check if a coordinate is below the maximal range of the patten

#### Parameters
name|type|description
-----|-----|-----
**coordinate**|[[Coordinate]]|The coordinates to check
**pattern**|`Pattern`|The pattern to use
**maxRange**|`int`|Minimum range

#### Return
- `bool` : True if the coordinate is not beyond the maximal range
