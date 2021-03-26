"""
Question:
Given 2 strings s1 nd s2, write a function return true if s2
contains the permutation of s1. In other words, one of the first string's
permutation is a substring of the second string.

Input:
s1, s2 strings

Output:
True or False
"""

def get_permutations(s):
    return []


def is_permutation(s1, s2):
    all_perm = get_permutations(s1)
    for perm in all_perm:
        if perm in s2:
            return True

    return False


def main():
    s1 = "abc"
    s2 = "asdbacsd"
    print(is_permutation(s1, s2))


if __name__ == '__main__':
    main()
