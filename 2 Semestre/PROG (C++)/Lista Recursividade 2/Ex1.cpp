#include <stdio.h>

int multiplica(int n1,int n2){

    if (0 == n1 && 0 == n2){

        return 0;
    }

    else if(1 == n2){

        return n1;
    }

    else{

        return multiplica(n1,n2-1)+n1;

    }

}

int main()
{
    
    int a,b,c;

    scanf("%d",&a);
    scanf(" %d",&b);


    c = multiplica(a,b);

    printf("%d\n",c);



    return 0;
}