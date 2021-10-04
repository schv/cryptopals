#!/bin/python3

def xor(x, y):
    return bytes([a^b for a, b in zip(x, y)])


if __name__ == '__main__':
    x = bytes.fromhex("1c0111001f010100061a024b53535009181c")
    y = bytes.fromhex("686974207468652062756c6c277320657965")
    z = xor(x, y)
    expected = bytes.fromhex("746865206b696420646f6e277420706c6179")

    assert z == expected, z
