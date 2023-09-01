#include <stdio.h>

int contadig(int n){

    if(n<9){
        return 1;

    }

    else{
        return contadig(n/10)+1;

    }


}

int main()
{
    
    int a,b;

    scanf("%d",&a);

    b = contadig(a);

    printf("%d\n",b);



    return 0;
}
