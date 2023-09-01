#include <stdio.h>

void impressao(int N){

    if(N == 1){
        printf("1");
    }

    else{

        impressao(N-1);
        printf("%d\n",N);
        
    }
    
}

int main()
{
    
    int a;

    scanf("%d",&a);

    impressao(a);

    return 0;
}