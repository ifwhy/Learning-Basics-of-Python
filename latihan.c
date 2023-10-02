#include <stdio.h>
#include <string.h>

int main()
{
    int nilai;
    float IPK = 4.00;
    char grade[] = "ABCD+-";
    printf("Program mendata nilai mahasiswa \n");
    printf("Berapakah nilai Anda? : ");
    scanf("%d", &nilai);

    print("Nilai Anda adalah %d\n", nilai);
    if(nilai >= 85 && nilai <= 100){
        printf("IPK Anda adalah %.2f\n", IPK);
        printf("Grade Anda adalah %c", grade[0]);
    } else if(nilai >= 80 && nilai < 85){
        printf("IPK Anda adalah %.2f\n", IPK-0.50);
        printf("Grade Anda adalah %c%c", grade[0], grade[5]);
    } else if(nilai >= 75 && nilai < 80){
        printf("IPK Anda adalah %.2f\n", IPK-0.75);
        printf("Grade Anda adalah %c%c", grade[1], grade[4]);   
    } else if(nilai >= 70 && nilai < 75){
        printf("IPK Anda adalah %.2f\n", IPK-1.00);
        printf("Grade Anda adalah %c", grade[1]);
    } 
    return 0;
}
