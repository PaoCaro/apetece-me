#include <stdio.h>
#include <string.h>

int main() 
{
  char frase[30];

  printf("vá escreve ai uma merda qualquer:\n");
  fgets(frase, sizeof(frase), stdin);

  printf("%s", frase);
  return 0;
}
