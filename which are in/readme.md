# Which are in? (6kyu)
## https://www.codewars.com/kata/550554fd08b86f84fe000a58

Given two arrays of strings `a1` and `a2` return a sorted array `r` in lexicographical order of the strings of `a1` which are substrings of strings of `a2`.

Example 1:

`a1 = ["arp", "live", "strong"]`<br/>

`a2 = ["lively", "alive", "harp", "sharp", "armstrong"]`<br/>

returns `["arp", "live", "strong"]`<br/>

Example 2:

`a1 = ["tarp", "mice", "bull"]`<br/>

`a2 = ["lively", "alive", "harp", "sharp", "armstrong"]`<br/>

returns `[]`<br/>

Notes:

    Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.
    In Shell bash a1 and a2 are strings. The return is a string where words are separated by commas.
    Beware: r must be without duplicates.

### How to run:
`python3 which_are_in.py` - print result from `test_arr1` and `test_arr2`.
