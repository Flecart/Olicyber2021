#include <stdio.h>

#include <sys/stat.h>
#include <fcntl.h>
int main()
{

    char bufferone[30];

    int qualcosa = open("./flag.txt", 0x1e);  
    read(qualcosa, bufferone, 30);

    puts(bufferone); 
//     int local_100;
//     int j;
//     int k;
//     int i;
//     char local_38 [16] = {0};
//     srand(0);
//     j = 0;
//   while (j < 4) {
//     local_100 = rand();
//     k = 0;
//     while (k < 4) {
//       local_38[k + j * 4] = (char)local_100;
      
//       printf("%d ->", local_38[k + j*4]);
//       printf("%u ", local_100);
//       local_100 = local_100 >> 8;
//       k = k + 1;
      
//     }
//     j = j + 1;
//   }
//   printf("\n", local_38[k + j*4]);

    return 0;
}
  