# Snail (4 kyu)
## https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

### Snail Sort

Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

[[1,2,3],<br/>
[4,5,6],<br/>
[7,8,9]]<br/>

snail(array) #=> [1,2,3,6,9,8,7,4,5]

For better understanding, please follow the numbers of the next array consecutively:

[[1,2,3],<br/>
 [8,9,4],<br/>
 [7,6,5]]<br/>

snail(array) #=> [1,2,3,4,5,6,7,8,9]



NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].

### How to run:
There are two solutions. 
1. `python3 best.py` print modifited `array`;
2. `python Snailsort.py` print modifited `array`.
