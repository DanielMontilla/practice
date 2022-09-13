import re


def isPalindrome(s: str) -> bool:
    # first convert string
    s = re.sub('[^A-Za-z0-9]+', '', s).lower()

    length = len(s)

    l = 0
    r = length - 1

    length = (length // 2)

    for i in range(length):
        if s[l] != s[r]:
            return False

        l += 1
        r -= 1

    return True

# Inputs:
palindrome_1 = "A man, a plan, a canal: Panama"
palindrome_2 = "race a car"
palindrome_3 = " "


if __name__ == '__main__':
    res = isPalindrome(palindrome_1)
    print(res)