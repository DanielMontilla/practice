from encode_decode_strings import encode, decode


def main():

    strs = ["we", "say", ":", "yes"]

    enc = encode(strs)

    print(enc)

    res = decode(enc)

    print(res)


if __name__ == '__main__':
    main()
