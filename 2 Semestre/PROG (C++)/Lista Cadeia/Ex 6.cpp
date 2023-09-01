#include <stdio.h>
#define MAX 15

struct eletrodomesticos
{
    char nome[MAX+1];
    float potencia,tempo,potenciad;
};



int main(){

    eletrodomesticos eletros[5];
    int tempo; 
    float pt=0;

    for (int i = 0; i < 5; i++)
    {
        scanf( " %[^\n]",eletros[i].nome);
        scanf( " %f",&eletros[i].potencia);
        scanf( " %f",&eletros[i].tempo);
        eletros[i].potenciad = eletros[i].potencia*eletros[i].tempo;
    }
    
    scanf (" %d",&tempo);

    for (int i = 0; i < 5; i++)
    {
        pt =pt + (eletros[i].potenciad*tempo);
    }

    printf("%.2f\n",pt);   

    for (int i = 0; i < 5; i++)
    {
        printf("%.2f\n",((eletros[i].potenciad*tempo)/pt)*100);
    }
     

    return 0;
}

