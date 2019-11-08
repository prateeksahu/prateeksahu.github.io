#! /usr/bin/env python
import math

def main():
    #pick 2 prime numbers
    p = 97
    q = 53
    p = 12131072439211271897323671531612440428472427633701410925634549312301964373042085619324197365322416866541017057361365214171711713797974299334871062829803541
    q = 12027524255478748885956220793734512128733387803682075433653899983955179850988797899869146900809131611153346817050832096022160146366346391812470987105415233

    #calculate n
    n = p*q

    #totient
    t = lcm(p-1,q-1)

    #pick an e coprime with t
    #e = 29
    e = 65537

    #calculate private key
    d = modinv(e,t)
    print(f"your private key is {d}\n")
    m = 104101108112
    print(f"your message m is {m}\n")

    #compute m^e mod(n) encrypt
    c = pow(m,e,n)

    #compute c^d mod(n) to decrypt
    m2 = pow(c,d,n)

    print(f"your cypher text is {c}")
    print(f"your decrypted text is {m2}")


def egcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

def lcm(p,q):
	p, q = abs(p), abs(q)
	m = p * q
	if not m: return 0
	while True:
		p %= q
		if not p: return m // q
		q %= p
		if not q: return m // p

if __name__ == "__main__":
    main()
