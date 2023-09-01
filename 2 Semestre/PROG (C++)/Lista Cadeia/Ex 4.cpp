#include <stdio.h>
#include <string.h>
#define MAX 20


struct grao
{
	
	char tipo;
	char nome[MAX+1];
	float peso;
	float precoKG;

};

int main(){

	grao graos[3];
	int iguais = 1,pos[3]={0,0,0};
	char melhor='C';
	

	for (int i = 0; i < 3; i++)
	{
		scanf(" %[^\n]",graos[i].nome);
		scanf(" %c",&graos[i].tipo);
		scanf(" %f",&graos[i].peso);
		scanf(" %f",&graos[i].precoKG);

		if (melhor>graos[i].tipo){

			melhor = graos[i].tipo;
			iguais = 1;
			pos[0] = 0; pos[1] = 0; pos[2] = 0;
			pos[i]++;

		}

		else if(melhor == graos[i].tipo){
			
			iguais++;
			pos[i]++;


		}

	}	
	

	if(iguais<2){
		
		for (int i = 0; i < 3; i++)
		{
			if(pos[i] == 1){

				printf("O grão ideal é o/a %s\n",graos[i].nome);
			}
		}
	}

	else{

		char horadoduelo[iguais][MAX+1];
		int j = 0;
		float a,b;

		for (int i = 0; i < 3 ; i++)
		{
			if (pos[i]==1)
			{
				strcpy(horadoduelo[j],graos[i].nome);
                j++;
			}
			

		}
		
		scanf( "%f",&a);
		scanf( "%f",&b);

		if (a<b)
		{
			printf("O grão ideal é o/a %s\n",horadoduelo[1]);
		}
			
		else{

			printf("O grão ideal é o/a %s\n",horadoduelo[0]);

		}

		

	

	}
	
	


return 0;

}
