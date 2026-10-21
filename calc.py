import sys

# Konzolni kalkulator - avtor Lukas
# Nedokoncano delo brez commit-a
# 1, 2, 3

def sestej(a, b): # To je sestevanje - komentar 1
    return a + b


def odstej(a, b): # to je odstevanje - komentar 2
    return a - b

def mnozi(a, b):
    return a * b

def deli(a, b):
    if b == 0:
        print("Napaka: deljenje z nic ni mogoce")
        sys.exit(1)
    return a / b

def main():
    if len(sys.argv) != 4:
        print("Uporaba: python calc.py <stevilo1> <operator> <stevilo2>")
        print("Primer: python calc.py 1 + 2")
        sys.exit

    st1 = float(sys.argv[1]) # stevilo1
    operator = sys.argv[2]
    st2 = float(sys.argv[3]) # stevilo2

    if operator == "+":
        print(f"Rezultat: {sestej(st1, st2)}")
    elif operator == "-":
        print(odstej(st1, st2))
    elif operator == "*":
        print(mnozi(st1, st2))
    elif operator == "/":
        print(deli(st1, st2))
    else:
        print(f"Neznan operator: {operator}")
        sys.exit(1)

if __name__ == "__main__":
    main()