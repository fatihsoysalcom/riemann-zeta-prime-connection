import math

def is_prime(n):
    """Checks if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def get_primes_up_to(limit):
    """Generates primes up to a given limit using a sieve."""
    primes = []
    sieve = [True] * (limit + 1)
    for p in range(2, limit + 1):
        if sieve[p]:
            primes.append(p)
            for multiple in range(p * p, limit + 1, p):
                sieve[multiple] = False
    return primes

def riemann_zeta_sum_approximation(s, num_terms=10000):
    """
    Approximates the Riemann Zeta function for real s > 1
    using the infinite sum definition: zeta(s) = sum(1/n^s).
    """
    if s <= 1:
        raise ValueError("s must be greater than 1 for this sum approximation to converge.")
    
    zeta_sum = 0.0
    for n in range(1, num_terms + 1):
        zeta_sum += 1 / (n ** s)
    return zeta_sum

def riemann_zeta_euler_product_approximation(s, num_primes_to_use=500):
    """
    Approximates the Riemann Zeta function for real s > 1
    using the Euler product formula: zeta(s) = product(1 / (1 - p^-s))
    where p are prime numbers.
    """
    if s <= 1:
        raise ValueError("s must be greater than 1 for this product to converge.")

    # Generate enough primes for the approximation
    # A rough upper bound for the Nth prime is N * ln(N)
    # For 500 primes, max prime is around 500 * ln(500) ~ 500 * 6.21 = 3105
    # We use a slightly larger limit to be safe.
    prime_limit = int(num_primes_to_use * math.log(num_primes_to_use) * 1.5) if num_primes_to_use > 1 else 10
    primes = get_primes_up_to(prime_limit)[:num_primes_to_use]

    zeta_product = 1.0
    for p in primes:
        zeta_product *= (1 / (1 - (p ** -s)))
    return zeta_product

# --- Main demonstration ---
if __name__ == "__main__":
    # The article discusses the Riemann Hypothesis, which concerns the zeros
    # of the Riemann Zeta function. A fundamental aspect of the Zeta function
    # is its connection to prime numbers, illustrated by the Euler product formula.
    # This example demonstrates that connection for a real 's > 1'.

    s_value = 2.0  # Choose a real value for 's' where s > 1
    print(f"Demonstrating Riemann Zeta function approximations for s = {s_value}\n")

    # 1. Approximate using the infinite sum definition
    num_sum_terms = 10000
    zeta_from_sum = riemann_zeta_sum_approximation(s_value, num_sum_terms)
    print(f"Approximation using sum (first {num_sum_terms} terms):\n  zeta({s_value}) ≈ {zeta_from_sum:.6f}")
    # For s=2, zeta(2) = pi^2 / 6 ≈ 1.644934
    print(f"  (Known value for zeta(2) is pi^2/6 ≈ {math.pi**2 / 6:.6f})\n")

    # 2. Approximate using the Euler product formula (product over primes)
    num_primes_for_product = 500 # Using more primes for better accuracy
    zeta_from_product = riemann_zeta_euler_product_approximation(s_value, num_primes_for_product)
    print(f"Approximation using Euler product (first {num_primes_for_product} primes):\n  zeta({s_value}) ≈ {zeta_from_product:.6f}")

    # The Riemann Hypothesis relates to the non-trivial zeros of this function
    # in the complex plane, which are deeply connected to the distribution of prime numbers.
    # The Euler product formula explicitly shows this fundamental connection.
    print("\n--- Connection to Riemann Hypothesis ---")
    print("The close agreement between these two approximations (sum and product over primes)")
    print("demonstrates the fundamental identity linking the Riemann Zeta function to prime numbers.")
    print("The Riemann Hypothesis itself makes a claim about the distribution of the 'non-trivial zeros'")
    print("of this function in the complex plane, which in turn governs the distribution of prime numbers.")
    print("While this example doesn't delve into complex numbers or finding zeros,")
    print("it illustrates the core mathematical object and its prime number connection discussed in the article.")
