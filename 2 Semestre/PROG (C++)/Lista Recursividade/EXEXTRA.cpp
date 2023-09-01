#include <stdio.h>

int cu(int n){

    if(n == 1){
        return 1;

    }

    else{
        return cu(n-1)+n;

    }
}

int main()
{
    
    int a,b;

    scanf("%d",&a);

    b = cu(a);

    printf("%d\n",b);



    return 0;
}