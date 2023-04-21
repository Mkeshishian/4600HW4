#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef unsigned char byte;
typedef unsigned long long word;

/* Helper functions */

/* Convert a string of hexadecimal digits to a byte array */
void hex_to_bytes(char* hex_string, byte* byte_array, size_t len) {
    for (size_t i = 0; i < len; i++) {
        byte_array[i] = strtol(hex_string + 2*i, NULL, 16);
    }
}

/* Convert a byte array to a string of hexadecimal digits */
void bytes_to_hex(byte* byte_array, char* hex_string, size_t len) {
    for (size_t i = 0; i < len; i++) {
        sprintf(hex_string + 2*i, "%02X", byte_array[i]);
    }
}

/* Compute the greatest common divisor of two numbers */
word gcd(word a, word b) {
    word temp;
    while (b != 0) {
        temp = a % b;
        a = b;
        b = temp;
    }
    return a;
}

/* Compute the modular inverse of a number */
word mod_inverse(word a, word m) {
    word m0 = m;
    word y = 0, x = 1;
    if (m == 1) {
        return 0;
    }
    while (a > 1) {
        word q = a / m;
        word t = m;
        m = a % m;
        a = t;
        t = y;
        y = x - q * y;
        x = t;
    }
    if (x < 0) {
        x += m0;
    }
    return x;
}

/* Main function */

int main() {
    /* I used 128 bit values for simplicity but you should use 512 bit + values for security */
    char p_hex[] = "F7E75FDC469067FFDC4E847C51F452DF";
    char q_hex[] = "E85CED54AF57E53E092113E62F436F4F";
    char e_hex[] = "0D88C3";
    byte p_bytes[16];
    byte q_bytes[16];
    byte e_bytes[3];
    byte n_bytes[16];
    word p, q, e, n, phi, d;
    char d_hex[17];

    /* Convert hexadecimal strings to byte arrays */
    hex_to_bytes(p_hex, p_bytes, 16);
    hex_to_bytes(q_hex, q_bytes, 16);
    hex_to_bytes(e_hex, e_bytes, 3);

    /* Convert byte arrays to numbers */
    p = *(word*)p_bytes;
    q = *(word*)q_bytes;
    e = *(word*)e_bytes;

    /* Compute n and phi */
    n = p * q;
    phi = (p - 1) * (q - 1);

    /* Compute d */
    d = mod_inverse(e, phi);

    /* Convert d to hexadecimal string */
    sprintf(d_hex, "%016llX", d);

    /* Print the results */
    printf("p: %s\n", p_hex);
    printf("q: %s\n", q_hex);
    printf("e: %s\n", e_hex);
    printf("d: %s\n", d_hex);

    return 0;
}

