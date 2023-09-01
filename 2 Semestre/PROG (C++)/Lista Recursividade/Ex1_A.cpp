#include <stdio.h>

int pot(int x, int n){

    int cu = x;

    for (int i = 0; i < n-1; i++)
    {
        x = x*cu;
    }
    
    return x;

}

int main(){

    int a,b,c;

    scanf("%d",&a);
    scanf(" %d",&b);

    c = pot(a,b);

    printf("%d\n",c);

    return 0;

}