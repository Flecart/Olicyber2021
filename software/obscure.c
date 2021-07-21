#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define ulong unsigned long
#define true 1
#define byte char

int value_84BA7800 = 0x84BA7800;
char fuck[] = {0xbe, 0xc0, 0xc9, 0x76, 0xf5, 0xab, 0xf6, 0x09, 0x56, 0x19, 0x85, 0xfd, 0xe1, 0x4d, 0x0e, 0x83, 0xe3, 0x46, 0xa8, 0xa6, 0x5b, 0xcb, 0x7c, 0x8b, 0xbe, 0x33, 0x1c, 0x24, 0x74, 0x51, 0xb3, 0x1b, 0xcb, 0xca, 0x8f, 0xec, 0x98, 0xbf, 0x78, 0x5b};

char * len(char *param_1){
  char *what;
  
  what = param_1;
  do {
    what = what + 1;
  } while (*what != '\0');
  return what + -(long)param_1;
}

// cambia a coppier di due vicine tipo ABCD diventa BADC per tutte
void swap_each_2(byte *param_1)

{
  ulong uVar1;
  int maybeCounter;
  
  maybeCounter = 0;
  while( true ) {
    uVar1 = len(param_1);
    if (uVar1 <= (ulong)(long)maybeCounter) break;
    param_1[maybeCounter] = param_1[maybeCounter] + param_1[(long)maybeCounter + 1];
    param_1[(long)maybeCounter + 1] = param_1[(long)maybeCounter + 1] + param_1[maybeCounter];
    param_1[maybeCounter] = param_1[(long)maybeCounter + 1] - param_1[maybeCounter];
    param_1[(long)maybeCounter + 1] =
         (param_1[(long)maybeCounter + 1] - param_1[maybeCounter]) - param_1[maybeCounter];
    maybeCounter = maybeCounter + 2;
  }
  return;
}


// funzione supporto a firstScramble
void final_change_param(int *param_1,int *param_2)
{
  char cVar1;
  ulong uVar2;
  int i;
  int *pointer;
  int *myInput;
  
  uVar2 = len(param_2);
  pointer = param_2;
  myInput = param_1;
  if ((ulong)(long)4 < uVar2) {
    uVar2 = uVar2 / (ulong)(long)4;
    i = 0;
    while ((ulong)(long)i < uVar2) {
      param_1[i] = param_2[i];
      i = i + 1;
    }
    final_change_param(param_1 + uVar2,param_2 + uVar2);
  }
  else {
    do {
      *(char *)myInput = *(char *)pointer;
      cVar1 = *(char *)pointer;
      pointer = (int *)((long)pointer + 1);
      myInput = (int *)((long)myInput + 1);
    } while (cVar1 != '\0');
  }
  return;
}

// sposta il risultato di 16 % len mia flag dall inizio a fondo, esempio
// AAAABBBBC sposta 7 char in fondo diventando BCAAAABBB
// ma sarebbe da provare con lunghezze maggiori perch'e non ho capito perche queste non vadano
void firstScramble(byte *param_1,int param_2)

{
  long stringLen1;
  char *__ptr;
  ulong stringLen2;
  int k;
  int i;
  int j;
  
  stringLen1 = len(param_1);
  __ptr = (char *)calloc(1,stringLen1 + 1);
  k = 0;
  stringLen2 = len(param_1);
  i = (int)((ulong)(long)param_2 % stringLen2);
  while( true ) {
    stringLen2 = len(param_1);
    if (stringLen2 <= (ulong)(long)i) break;
    __ptr[k] = param_1[i];
    k = k + 1;
    i = i + 1;
  }
  j = 0;
  while (j < param_2) {
    __ptr[k] = param_1[j];
    k = k + 1;
    j = j + 1;
  }
  stringLen1 = len(param_1);
  __ptr[stringLen1] = '\0';
  final_change_param((int *)param_1,(int *)__ptr);
  free(__ptr);
  return;
}

void print_wrong_input(void){
  puts("Wrong input");
  exit(0);
}

// sposta il risultato di 16 % len mia flag dall fondo allinizio, esempio
// AAAABBBBC sposta 7 char in fondo diventando AABBBBCAA il contrario del primo scramble
void scrable_2(char *param_1,int param_2)

{
  long lVar1;
  char *__ptr;
  ulong uVar2;
  int k;
  int i;
  int j;
  
  lVar1 = len(param_1);
  __ptr = (char *)calloc(1,lVar1 + 1);
  uVar2 = len(param_1);
  k = (int)((ulong)(long)param_2 % uVar2);
  i = 0;
  while( true ) {
    uVar2 = len(param_1);
    if ((ulong)(long)param_2 % uVar2 <= (ulong)(long)i) break;
    __ptr[k] = param_1[i];
    k = k + 1;
    i = i + 1;
  }
  uVar2 = len(param_1);
  j = (int)((ulong)(long)param_2 % uVar2);
  while( true ) {
    uVar2 = len(param_1);
    if (uVar2 <= (ulong)(long)j) break;
    uVar2 = len(param_1);
    __ptr[(ulong)(long)k % uVar2] = param_1[j];
    k = k + 1;
    j = j + 1;
  }
  lVar1 = len(param_1);
  __ptr[lVar1] = '\0';
  final_change_param((int *)param_1,(int *)__ptr);
  free(__ptr);
  return;
}


#pragma region Region_1 per mandare tutto in maiuscolo */
// ma nel programma `e chiamato con offset di 10
// e diventa il contrario
// es: aaaabbbbccccaaaabbbbcccc -> aaaabbbbccCCAAAABBBBCCCC
void to_upper_case(char* param_1,ushort param_2)

{
  long counter;
  
  counter = 0;
  while (counter < (long)(ulong)param_2) {
    if (counter < 1) {
      if (('`' < *(char *)(param_1 + counter + (ulong)param_2 + -1)) &&
         (*(char *)(param_1 + counter + (ulong)param_2 + -1) < '{')) {
        *(char *)(param_1 + counter + (ulong)param_2 + -1) =
             *(char *)(param_1 + counter + (ulong)param_2 + -1) + -0x20;
      }
      counter = counter + -1;
    }
    else {
      if (('`' < *(char *)(param_1 + counter)) && (*(char *)(param_1 + counter) < '{')) {
        *(char *)(param_1 + counter) = *(char *)(param_1 + counter) + -0x20;
      }
    }
    counter = -counter;
  }
  return;
}

// primi param_2 char in maiuscolo
// es: aaaabbbbccccaaaabbbbcccc -> AAAABBBBCCccaaaabbbbcccc
void to_upper_case_first(long param_1,ushort param_2)

{
  long local_18;
  long local_10;
  
  local_18 = 0;
  local_10 = (long)(int)(param_2 - 1);
  while (local_10 != -1) {
    if (('`' < *(char *)(param_1 + local_18)) && (*(char *)(param_1 + local_18) < '{')) {
      *(char *)(param_1 + local_18) = *(char *)(param_1 + local_18) + -0x20;
    }
    local_18 = local_18 + local_10;
    if (local_10 < 1) {
      local_10 = local_10 + 1;
    }
    else {
      local_10 = local_10 + -1;
    }
    local_10 = -local_10;
  }
  return;
}
#pragma endregion Region_1

// praticamente toglie index di posizione lol
void encrypt_WITHPOSIZION(byte *param_1,int param_2)

{
  long length;
  long lVar1;
  int local_1c;
  
  local_1c = 0x1438;
  while( true ) {
    lVar1 = (long)0x1438;
    length = len(param_1);
    if ((ulong)(length + lVar1) <= (ulong)(long)local_1c) break;
    param_1[local_1c - 0x1438] = param_1[local_1c - 0x1438] - (char)local_1c;
    param_1[local_1c - 0x1438] = param_1[local_1c - 0x1438] + (char)param_2;
    param_1[local_1c - 0x1438] = param_1[local_1c - 0x1438] + (char)0x1438;
    local_1c = local_1c + 1;
  }
  return;
}

// xor molto normale
void maybe_xor(byte *param_1,byte *param_2)

{
  ulong uVar1;
  int local_14;
  
  local_14 = 0;
  while( true ) {
    uVar1 = len(param_1);
    if (uVar1 <= (ulong)(long)local_14) break;
    param_1[local_14] =
         param_1[local_14] & ~param_2[local_14] | ~param_1[local_14] & param_2[local_14];
    local_14 = local_14 + 1;
  }
  return;
}

// funzione inutile che non cambia mai, boh. str_cmp lha detto tiziano
void str_cmp(char *param_1,int *param_2)

{
  char *cycle_through_input;
  char exit_condition;
  
  cycle_through_input = param_1;
  do {
    if (((*cycle_through_input + value_84BA7800) - *param_2 & 0xffU) == 0) {
      *cycle_through_input = ((char)param_2[1] - (char)*param_2) + *cycle_through_input;
    }
    exit_condition = *cycle_through_input;
    cycle_through_input = cycle_through_input + 1;
  } while (exit_condition != '\0');
  return;
}

int final_compare(char *param_1,char *param_2)

{
  char *pcVar1;
  char *pcVar2;
  char cVar3;
  char cVar4;
  int uVar5;
  char *myInput;
  char *longlong_global;
  
  myInput = param_1;
  longlong_global = param_2;
  do {
    if ((*myInput == '\0') || (*longlong_global == '\0')) break;
    pcVar1 = myInput + 1;
    cVar3 = *myInput;
    pcVar2 = longlong_global + 1;
    cVar4 = *longlong_global;
    myInput = pcVar1;
    longlong_global = pcVar2;
  } while (cVar3 == cVar4);
  if ((*myInput == *longlong_global) && (*myInput == '\0')) {
    uVar5 = 1;
  }
  else {
    uVar5 = 0;
  }
  return uVar5;
}
int main(int argc, char *argv[])
{
    
  ulong uVar2;
  uVar2 = len(argv[1] + 0xa);

  
  swap_each_2(fuck);
    int local_30 [2];
  int local_28 [2];
  int local_20 [2];

    local_30[0] = 0x5f;
  local_30[1] = 0x2d;
  local_28[0] = 0x21;
  local_28[1] = 0x69;
  local_20[0] = 0x37;
  local_20[1] = 0x74;


  str_cmp(argv[1],local_30);
  str_cmp(argv[1],local_28);
  str_cmp(argv[1],local_20);

  if (argc < 2) {
    print_wrong_input();
  }
  firstScramble(argv[1], 0x10);
  scrable_2(argv[1], 0x10);
    // maybe_xor(argv[1], 0x84ba7800);
    // maybe_xor(argv[1],fuck);
    // swap_each_2(argv[1]);
    // firstScramble(argv[1], 0x10);
  // encrypt_WITHPOSIZION(argv[1], value_84BA7800);
// to_upper_case(argv[1]+0xa,len(argv[1]+0xa));
  // to_upper_case_first(argv[1], 0xa);
  printf("%s\n", argv[1]);
  // char ciao[] = "aaaabbbbccccaaaabbbbcccc";
  // int out = final_compare(argv[1], ciao);
  // printf("%d\n", out);
  int string_len = strlen(argv[1]);
  // printf("%d\n", string_len);
  for(int i = 0; i < string_len; i++) {
        printf("0x%x ", argv[1][i]);
    }
    printf("\n");
//   print_wrong_input();
  return 0;

}
// e78e9a5cbae0b54e735dcadfdd753db6fe079f926ff46bb0890f280d65649833e3f984c3b38f5046