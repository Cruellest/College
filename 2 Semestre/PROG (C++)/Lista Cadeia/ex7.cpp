#include <stdio.h>
#define MAX 20


    struct aluno
    {
        char nome[MAX+1];
        float nota = 0;
    };
    
    struct salaDeAula
    {
        aluno alunos[5];
        int codigo;
    };
    


int main(){

    salaDeAula sala;
    float media = 0;

    scanf("%d",&sala.codigo);
    
    for (int i = 0; i < 5; i++)
    {
        scanf(" %[^\n]",sala.alunos[i].nome);
        scanf(" %f",&sala.alunos[i].nota);
    }
    
    printf("Sala: %d\n",sala.codigo);

    for (int i = 0; i < 5; i++)
    {
        printf("%s %.2f\n",sala.alunos[i].nome,sala.alunos[i].nota);
        media = media + sala.alunos[i].nota;
    }
    
    printf("Media: %.2f\n",media/5);


    return 0;
}