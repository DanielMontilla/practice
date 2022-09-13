from typing import List

# https://www.lintcode.com/problem/659/

separator = '🔥🎯🤦‍♂️😢😜🤷‍♀️🙌🐱‍🚀✔👀💖🙌'


def encode(strs: List[str]) -> str:
    res = ''
    for s in strs:
        res += s
        if s != strs[-1]:
            res += separator

    return res


def decode(str: str) -> List[str]:
    separator_len = len(separator)
    res = []

    last = 0

    for i in range(len(str)):
        segment = str[i:i + separator_len]

        if len(segment) != separator_len:
            res.append(str[last:])
            break

        if segment == separator:
            res.append(str[last:i])
            last = i + separator_len

    return res

# Input:
str_1 = "This is a simple test!"

if __name__ == '__main__':
    encoded_str = encode(str_1)
    decored_str = decode(encoded_str)
    print(encoded_str)
    print(decored_str)
    