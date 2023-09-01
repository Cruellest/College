#include <stdio.h>

struct Data
{
    short dia;
    short mes;
    short ano;
};



int main(){

Data first,second;
int a,b;


scanf("%hd/%hd/%hd",&first.dia,&first.mes,&first.ano);
scanf(" %hd/%hd/%hd",&second.dia,&second.mes,&second.ano);

if ((first.dia>31 || second.dia >31 || first.dia <0 || second.dia<0) || (first.mes>12||second.mes>12 || first.mes<0 ||second.mes<0))
{
    printf("Data invalida\n");
    return 1;
}

else{

    a = (first.dia)+(first.mes *30)+(first.ano*365);
    b = (second.dia)+(second.mes *30)+(second.ano*365);

    if (a>b)
    {
        printf("%d\n",a-b);
    }
    
    else{
        printf("%d\n",b-a);
    }
        return 0;
}


}