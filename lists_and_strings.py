from typing import Optional             # gain access to the Optional[X] type hint


def checked_access(L:list[int], idx:int) -> Optional[int]:
    test = idx >= 0 and idx < len(L)    # What is the value of test on each call?
    if test:                            # What is this check preventing?
        return L[idx]
    else:
        return None


first = checked_access([1, 0, 1], 9)     # What is the value of first?
second = checked_access([1, 0, 1], 2)    # What is the value of second?
print()

def length_sum(L:list[str]) -> int:
    if len(L) > 2:
        result = len(L[0]) + len(L[1]) + len(L[2])    # For which call below is this statement evaluated
    elif len(L) > 1:                                  #   and what are the values being added?
        result = len(L[0]) + len(L[1])                # For which call below is this statement evaluated
    elif len(L) > 0:                                  #   and what are the values being added?
        result = len(L[0])                            # For which call below is this statement evaluated
    else:                                             # and what are the values being added?
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
         # What is the value of words at this point?
         # What are the values of first and second at this point?
         # What happened?
print()

