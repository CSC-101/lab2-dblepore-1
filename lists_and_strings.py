from typing import Optional             # gain access to the Optional[X] type hint


def checked_access(L:list[int], idx:int) -> Optional[int]:
    test = idx >= 0 and idx < len(L)    # first call: false, second call: true
    if test:                            # this is checking if the idx is within the range of L
        return L[idx]
    else:
        return None


first = checked_access([1, 0, 1], 9)     # none
second = checked_access([1, 0, 1], 2)    # 1
print()

def length_sum(L:list[str]) -> int:
    if len(L) > 2:
        result = len(L[0]) + len(L[1]) + len(L[2])    # the first call
    elif len(L) > 1:                                  #   4 + 2 + 3 = 9
        result = len(L[0]) + len(L[1])                # the third call
    elif len(L) > 0:                                  #  7 + 4 = 11
        result = len(L[0])                            # the second
    else:                                             # 11
        result = 0
    return result


first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print()

def surprising(L:list[str], other:str) -> list[str]:
    L.append(other.upper())
    return L


words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
         # ["this", "is", "confusing", "code.", "avoid", "such."]
         # What are the values of first and second at this point?
         # first:  ["this", "is", "confusing", "code.", "avoid"]
         # second:  ["this", "is", "confusing", "code.", "avoid", "such."]
         # first got the initial contents of words and added avoid at the end
         # second got the contents of words after the first call, and added "such." at the end

print()

