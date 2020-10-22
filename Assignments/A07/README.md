### Pratt Certificate
 The Pratt certificate is a primality certificate based on Fermat's little theorem converse.
#
 To generate a Pratt certificate, assume that n is a positive integer and {p_i} is the set of prime factors of n-1. Suppose there exists an integer x such that x^(n-1)=1 (mod n) but x^e≢1 (mod n) whenever e is one of (n-1)/p_i. Then Fermat's little theorem converse states that n is prime.
 ![2020-10-22](https://user-images.githubusercontent.com/60235679/96859387-11368d80-1427-11eb-8551-f783d645caf6.png)
#### Source: https://mathworld.wolfram.com/PrattCertificate.html

### Lucas' theorem: Suppose we have an integer a such that:
```
 an − 1 ≡ 1 (mod n),
 for every prime factor q of n − 1, it is not the case that a(n − 1)/q ≡ 1 (mod n).
Then n is prime.
```
  Given such an a (called a witness) and the prime factorization of n − 1, it's simple to verify the above conditions quickly: we only need to do a linear number of modular exponentiations, since every integer has fewer prime factors than bits, and each of these can be done by exponentiation by squaring in O(log n) multiplications (see big-O notation). Even with grade-school integer multiplication, this is only O((log n)4) time; using the multiplication algorithm with best-known asymptotic running time, the Schönhage–Strassen algorithm, we can lower this to O((log n)3(log log n)(log log log n)) time, or using soft-O notation Õ((log n)3).
  #### Source: https://en.wikipedia.org/wiki/Primality_certificate
  
### Atkin–Goldwasser–Kilian–Morain certificates
#### Theorem: Suppose we are given:
```
a positive integer n not divisible by 2 or 3;
 Mx, My, A, B in Zn (the integers mod n) satisfying My^2 = Mx^3 + AMx + B and with 4A^3 +  27B^2 coprime to n;
 a prime q > n^(1/2) + 1 + 2n^(1/4).
```
Then M = (Mx, My) is a non-identity point on the elliptic curve y^2 = x^3 + Ax + B. Let kM be M added to itself k times using standard elliptic-curve addition. Then, if qM is the identity element I, then n is prime.
  #### Source: https://en.wikipedia.org/wiki/Primality_certificate
