#include <stdio.h>
#include <stdint.h>

uint64_tencrypt(int64_t data, uint64_t key)
{
    data ^= key;
    data = (data << 1) | (data >> 63);
    return data;
}

uint64_t decrypt(uint64_t data, uint64_t key)
{
    data = (data >> 1) | (data << 63);
    data ^= key;
    return data;
}

int main()
{
    uint64_t plaintext, key, ciphertext, decrypted;

    printf("Enter 64-bit plaintext (hex): ");
    scanf("%llx", &plaintext);

    printf("Enter 56-bit key (hex): ");
    scanf("%llx", &key);

    ciphertext = encrypt(plaintext, key);
    decrypted = decrypt(ciphertext, key);

    printf("\nPlaintext  : %016llX", plaintext);
    printf("\nCiphertext : %016llX", ciphertext);
    printf("\nDecrypted  : %016llX\n", decrypted);

    return 0;
}
