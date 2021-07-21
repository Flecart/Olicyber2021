#include <stdlib.h>
#include <stdio.h>
#include <openssl/evp.h>

int main()
{
    ulong t = time(NULL);
    EVP_PKEY_CTX *ctx = (EVP_PKEY_CTX *)(t & 0xffffffff);
    srand((uint)ctx);
    printf("%d", rand());

    return 0;
}