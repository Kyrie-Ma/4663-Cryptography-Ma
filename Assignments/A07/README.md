## Pratt Certificate
 The Pratt certificate is a primality certificate based on Fermat's little theorem converse.
 To generate a Pratt certificate, assume that n is a positive integer and {p_i} is the set of prime factors of n-1. Suppose there exists an integer x such that x^(n-1)=1 (mod n) but x^e≢1 (mod n) whenever e is one of (n-1)/p_i. Then Fermat's little theorem converse states that n is prime.
 ![2020-10-22](https://user-images.githubusercontent.com/60235679/96859387-11368d80-1427-11eb-8551-f783d645caf6.png)
#### Source: https://mathworld.wolfram.com/PrattCertificate.html

## Lucas' theorem: 
```
Suppose we have an integer a such that:
 an − 1 ≡ 1 (mod n),
 for every prime factor q of n − 1, it is not the case that a(n − 1)/q ≡ 1 (mod n).
Then n is prime.
```
  Given such an a (called a witness) and the prime factorization of n − 1, it's simple to verify the above conditions quickly: we only need to do a linear number of modular exponentiations, since every integer has fewer prime factors than bits, and each of these can be done by exponentiation by squaring in O(log n) multiplications (see big-O notation). Even with grade-school integer multiplication, this is only O((log n)4) time; using the multiplication algorithm with best-known asymptotic running time, the Schönhage–Strassen algorithm, we can lower this to O((log n)3(log log n)(log log log n)) time, or using soft-O notation Õ((log n)3).
  #### Source: https://en.wikipedia.org/wiki/Primality_certificate
  
## Atkin–Goldwasser–Kilian–Morain certificates
#### Theorem: Suppose we are given:
```
a positive integer n not divisible by 2 or 3;
 Mx, My, A, B in Zn (the integers mod n) satisfying My^2 = Mx^3 + AMx + B and with 4A^3 +  27B^2 coprime to n;
 a prime q > n^(1/2) + 1 + 2n^(1/4).
```
Then M = (Mx, My) is a non-identity point on the elliptic curve y^2 = x^3 + Ax + B. Let kM be M added to itself k times using standard elliptic-curve addition. Then, if qM is the identity element I, then n is prime.
  #### Source: https://en.wikipedia.org/wiki/Primality_certificate
  
## Fermat primality test
```
The simplest probabilistic primality test is the Fermat primality test (actually a compositeness test). It works as follows:
  Given an integer n, choose some integer a coprime to n and calculate an − 1 modulo n. If the result is different from 1, then n is composite. If it is 1, then n may be prime.
If a^(n−1) (modulo n) is 1 but n is not prime, then n is called a pseudoprime to base a. In practice, we observe that, if an−1 (modulo n) is 1, then n is usually prime. But here is a counterexample: if n = 341 and a = 2, then 2^340 = 1 (mod 341)
even though 341 = 11·31 is composite. In fact, 341 is the smallest pseudoprime base 2.
```
#### Source: https://en.wikipedia.org/wiki/Primality_test

## Miller–Rabin and Solovay–Strassen primality test
 ![2020-10-22 (2)](https://user-images.githubusercontent.com/60235679/96861399-a89ce000-1429-11eb-9aaa-ae4255c4f0fb.png)
 #### Source: https://en.wikipedia.org/wiki/Primality_test
 
 ## AKS primality test
  The AKS primality test is based upon the following theorem: Given an integer n >= 2 and integer a coprime to n, n is prime if and only if the polynomial congruence relation (x + a)^n = (x^n + a) (mod n) holds. Note that x should be understood as formal symbol.
  ![2020-10-22 (3)](https://user-images.githubusercontent.com/60235679/96861971-7a6bd000-142a-11eb-860d-46aebddd5bd2.png)
 #### Source: https://en.wikipedia.org/wiki/AKS_primality_test
 
 ## Miller-Rabin test
 ```
  The Miller-Rabin test is actually a sequence of tests, one for each prime number. First you run the test associated with 2, then the test associated with 3, then the one associated with 5, etc. If we knew the smallest numbers for which these tests fail, then for smaller numbers we know for certain that they’re prime if they pass. In other words, we can turn the Miller-Rabin test for probable primes into test for provable primes.
```
Miller and Rabin’s extra testing starts by factoring n-1 into 2sd where d is odd. If n is prime, then for all 0 < a < n either 
```
  a^d = 1 (mod n) or a^(d(2)^k) = -1 (mod n) 
```
for all k satisfying 0 ≤ k < s. If one of these two conditions holds for a particular a, then n passes the Miller-Rabin test for the base a.
#### Source: https://www.johndcook.com/blog/2019/02/25/prime-test/
