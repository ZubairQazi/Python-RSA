import math

def find_pq(n: int):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            p = i
            q = n / i
            return p, q
    return 1, n
    
def mod_inverse(e: int, phi: int):
    e = e % phi;
    for i in range(1, int(phi)):
        # make sure that e does not share any divisors with phi
        if e * i % phi == 1:
            return i
    return 1
    
def decrypt(input: int, d: int, n: int):
    return (input ** d) % n
            
def main():
    encoding_pattern = {2: 'A', 3: 'B', 4: 'C', 5: 'D', 6: 'E', 7: 'F', 8: 'G', 9: 'H', 10: 'I', 11: 'J', 12: 'K', 13: 'L', 14: 'M', 15: 'N', 16: 'O', 17: 'P', 18: 'Q', 19: 'R', 20: 'S', 21: 'T', 22: 'U', 23: 'V', 24: 'W', 25: 'X', 26: 'Y', 27: 'Z', 28: ' ' }
    e = int(input("Enter e: "))
    n = int(input("Enter n: "))
    
    input_nums = input("Enter the input numbers: ")
    
    p, q = find_pq(n)
    phi = (p - 1) * (q - 1)
    
    d = mod_inverse(e, phi)
    output = ""
    
    for str_num in input_nums.split():
        decrypted_num = decrypt(int(str_num), d, n)
        output += encoding_pattern.get(decrypted_num)
    
    print(output)
    
main()
    
    
    
    
