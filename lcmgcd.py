def compute_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm_and_gcd(a, b):
    gcd = compute_gcd(a, b)
    lcm = (a * b) // gcd
    return [lcm, gcd]

# Example usage
if __name__ == "__main__":
    a = int(input())
    b = int(input())
    result = lcm_and_gcd(a, b)
    print(result)
            
