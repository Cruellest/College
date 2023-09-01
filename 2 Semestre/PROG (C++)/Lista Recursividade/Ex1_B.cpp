#include <stdio.h>

int potR(int x,int n){

    if(n == 0){

        return 1;

    }
 
    else if (n == 1){

        return x;
    }
    else{

    return x*potR(x,n-1);

    }
}

int main(){

    int a,b,c;

    scanf("%d",&a);
    scanf(" %d",&b);

    c = potR(a,b);

    printf("%d\n",c);

    return 0;

}