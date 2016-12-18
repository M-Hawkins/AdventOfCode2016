import hashlib

def main():
    key = "reyedfim"
    pw = list("        ")
    i = 0

    while ' ' in pw:
        s = key + str(i)
        m = hashlib.md5()
        m.update(s)
        h = m.hexdigest()
        if h[:5] == "00000":
            n = ord(h[5])
            if n > 47 and n < 56:
                if (pw[int(h[5])] == " "):
                    pw[int(h[5])] = h[6]
                    print(i)
                    print(h)
                    print("---")
        i += 1
    print("".join(pw))

if __name__ == "__main__":
    main()