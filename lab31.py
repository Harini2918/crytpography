# CMAC Subkey Generation

def left_shift(value, block_size):
    """Left shift by 1 bit within the block size"""
    return (value << 1) & ((1 << block_size) - 1)


def generate_subkey(L, block_size):
    # Constants
    if block_size == 64:
        Rb = 0x1B
    elif block_size == 128:
        Rb = 0x87
    else:
        print("Invalid block size")
        return None

    # Check MSB
    msb = (L >> (block_size - 1)) & 1

    # Left shift
    K = left_shift(L, block_size)

    # XOR with Rb if MSB is 1
    if msb == 1:
        K = K ^ Rb

    return K


# Main program
print("CMAC Subkey Generation")

block_size = int(input("Enter block size (64 or 128): "))
L = int(input("Enter L in hexadecimal: "), 16)

# Generate K1
K1 = generate_subkey(L, block_size)

# Generate K2
K2 = generate_subkey(K1, block_size)

print("\nL  =", format(L, '0{}X'.format(block_size // 4)))
print("K1 =", format(K1, '0{}X'.format(block_size // 4)))
print("K2 =", format(K2, '0{}X'.format(block_size // 4)))

if block_size == 64:
    print("\nRb = 0x1B")
else:
    print("\nRb = 0x87")
