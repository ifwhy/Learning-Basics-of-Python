#include <stdio.h>

int main(){
    int nilai;
    float ipk;
    char grade[] = "AA-B+BC+CDE";
    int lanjut = 5, i = 1 ;

    while (i <= lanjut) {
        printf("\nMasukkan Nilai Anda = ");
        scanf("%d", &nilai);

        if (nilai >= 85 && nilai <= 100) {
            printf("IPK = %.2f\n", ipk = 4.00);
            printf("Grade = %c", grade[0]);
        } else if (nilai >= 80 && nilai < 85) {
            printf("IPK = %.2f\n", ipk = 3.70);
            printf("Grade = %c%c", grade[1], grade[2]);
        }   else if (nilai >= 75 && nilai < 80){
            printf("IPK = %.2f\n", ipk = 3.30);
            printf("Grade = %c%c", grade[3], grade[4]);
        } else if (nilai >= 70 && nilai <75) {
            printf("IPK = %.2f\n", ipk = 3.00);
            printf("Grade = %c", grade[5]);
        } else if (nilai >= 65 && nilai < 70) {
            printf("IPK = %.2f\n", ipk = 2.70);
            printf("Grade = %c%c", grade[6], grade[7]);
        } else if (nilai >= 60 && nilai < 65) {
            printf("IPK = %.2f\n", ipk = 2.00);
            printf("Grade = %c ", grade[8]);
        } else if (nilai >= 55 && nilai < 60) {
            printf("IPK = %.2f\n", ipk = 1.00);
            printf("Grade = %c", grade[9]);
        } else if (nilai <= 55 && nilai >  0) {
            printf("IPK = %.2f\n", ipk = 0.00);
            printf("Grade = %c", grade[9]);
        } else {
            printf("Masukan Anda salah");
        }
        i++;
    }
}