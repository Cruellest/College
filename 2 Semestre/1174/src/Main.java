import java.util.Scanner;

public class Main {


    public static void main(String[] args) throws Exception {


        Scanner scan = new Scanner(System.in);

        int tremruim,co;

        do{
            tremruim = scan.nextInt()/2;
            int array[] = new int[tremruim];

            co=0;
            for(int i = 0;i<tremruim;i++){
                if(i>0){
                    System.out.printf("\n");
                    co++;
                }

                for(int j =0; j<tremruim;j++){

                if(j>=co){
                    array[j]++;

                }
                System.out.printf("%d ",array[j]);
                }
                for(int k = tremruim-1;k>=0;k--){
                    System.out.printf("%d ",array[k]);
            }
            
        }

        System.out.printf("\n");

        for(int i = 0;i<tremruim;i++){
                if(i>0){
                    System.out.printf("\n");
                    co--;
                }

                for(int j =0; j<tremruim;j++){

                if(j>=co+1){
                    array[j]--;

                }
                System.out.printf("%d ",array[j]);
                }
                for(int k = tremruim-1;k>=0;k--){
                    System.out.printf("%d ",array[k]);
            }
            
        }

        

        System.out.printf("\n\n");
        }
        while(tremruim!=0);
    }
}