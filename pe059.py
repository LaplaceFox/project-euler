from string import ascii_lowercase

def decrypt(k):
    copykey = (k * (n//3 + 1))[:n]

    pt = [ciphertext[i] ^ copykey[i] for i in range(n)]
    pt = "".join(map(chr, pt))

    return pt

f = open("p059_cipher.txt")
ciphertext = list(map(int, f.read().split(",")))

n = len(ciphertext)

for c1 in ascii_lowercase:
    for c2 in ascii_lowercase:
        for c3 in "p":
            key = [ord(c1), ord(c2), ord(c3)]

            plaintext = decrypt(key)

            print("Key:", c1+c2+c3)

            if "the" in plaintext:
                print("Plaintext:", plaintext)

                input()
