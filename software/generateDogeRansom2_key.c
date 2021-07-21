#include <stdlib.h>
#include <stdio.h>

#define ulong unsigned long

// globalz
char cose1[32];
char globale[32];



ulong return_time(void)

{
  ulong uVar1;
  
  uVar1 = time(NULL);
  return uVar1;
}

long long alfabeto(char* globa,long hex_1e)

{
  int iVar1;
  uint uVar2;


//   char inizioAlfabeto[] = {0x68, 0x67,0x66,0x65,0x64,0x63,0x62,0x61, 0x70, 0x6f,0x6e,0x6d,0x6c,0x6b,0x6a,0x69, 0x78, 0x77,0x76,0x75,0x74,0x73,0x72,0x71, 0x46, 0x45,0x44,0x43,0x42,0x41,0x7a,0x79, 0x4e, 0x4d,0x4c,0x4b,0x4a,0x49,0x48,0x47, 0x56, 0x55,0x54,0x53,0x52,0x51,0x50,0x4f, 0x33, 0x32,0x31,0x30,0x59,0x5a,0x58,0x57, 0x5f, 0x2d,0x39,0x38,0x37,0x36,0x35,0x34};
    char inizioAlfabeto[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_";
 
  long local_18;
  int local_14;
  ulong counter;
  
  local_18 = 0;
  if (hex_1e != 0) {
    counter = 0;
    while (counter < hex_1e - 1) {
      iVar1 = rand();


      // il codice sotto e copiato pari pari da GHIDRA, ma non funziona
      uVar2 = (uint)(iVar1 >> 0x1f) >> 0x1a;
      local_14 = (iVar1 + uVar2 & 0x3f) - uVar2;
      *(long *)(globa + counter) = *(long *)((long)&inizioAlfabeto + (long)local_14);
      counter = counter + 1;
    }
    *(long *)((hex_1e - 1U) + globa) = 0;
  }
  return globa;
}
void init_globals()

{
  uint uVar1;
  int iVar2;
  int iVar3;
  int long_global_to_zero;
  
  long_global_to_zero = 0;
  while (long_global_to_zero < 4) {
    *(long *)(&globale + (long)long_global_to_zero * 8) = 0;
    long_global_to_zero = long_global_to_zero + 1;
  }
  uVar1 = return_time();
  srand(uVar1);
  iVar2 = return_time();
  iVar3 = rand();
  srand(iVar3 % 10000 + iVar2);
  uVar1 = rand();
  srand(uVar1);
  uVar1 = rand();
  srand(uVar1);
  uVar1 = rand();
  
  srand(uVar1);
  alfabeto(&cose1,0x1e);
  return;
}

int main() {
    init_globals();
    printf("%s", cose1);

    return 0;
}
// #include <openssl/evp.h>

// int main()
// {
//     ulong t = time(NULL);
//     EVP_PKEY_CTX *ctx = (EVP_PKEY_CTX *)(t & 0xffffffff);
//     srand((uint)ctx);
//     printf("%d", rand());

//     return 0;
// }