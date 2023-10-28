#include <stdio.h>
#include <math.h>

#define PI 3.1415926 // Konstanta pi
#define E 2.71828182845 // Bilangan Euler
#define logE 0.434294 // Logaritma dari bilangan euler

float degreeToRad(float n);
float radToDegree(float n);
float standarDevPop(float data[], int n);
float standarDevSam(float data[], int n);

int main()
{
    char pilih, pilih1, pilih2, pilih3, pilih4, pilih4_6;
    int banyakData;
    float bil1, bil2, hasil, dataStat, sum = 0, dataStat1;

    // Menu
    printf("_____________________________________________________\n");
    printf("\t\tKALKULATOR MILIK IVAN\n");
    printf("_____________________________________________________\n");

    printf("PILIHAN MODE \t\t: \n");
    printf("1. Operasi Matematika Dasar\n");
    printf("2. Trigonometri\n");
    printf("3. Logaritma\n");
    printf("4. Statistika\n");
    printf("5. Barisan dan Deret\n");
    printf("_____________________________________________________\n");


    printf("PILIH MODE \t\t: ");
    scanf("%s", &pilih);

    // Operasi Matematika Dasar
    if(pilih == '1'){
        printf("OPERASI MATDAS \t: \n");
        printf("1. Perkalian\n");
        printf("2. Pembagian\n");
        printf("3. Penjumlahan\n");
        printf("4. Pengurangan\n");
        printf("5. Akar Kuadrat\n");
        printf("6. Akar Pangkat Tiga\n");
        printf("7. e^x\n");
        printf("8. Eksponensial\n");
        printf("_____________________________________________________\n");
        printf("PILIH \t\t\t: ");
        scanf("%s", &pilih1);

        if(pilih1 == '1'){
            printf("\n\n\t\tOPERASI PERKALIAN\n");
            printf  ("_____________________________________________________\n");
            printf("Bilangan Pertama \t: ");
            scanf("%f", &bil1);
            printf("Bilangan Kedua \t\t: ");
            scanf("%f", &bil2);
            printf("_____________________________________________________\n");
            hasil = bil1*bil2;
            printf("Operasi \t\t: %.2f x %.2f = %.3f", bil1, bil2, hasil);
        } else if(pilih1 == '2'){
            printf("\n\t\tOPERASI PEMBAGIAN\n");
            printf  ("_____________________________________________________\n");
            printf("Bilangan Pertama \t: ");
            scanf("%f", &bil1);
            printf("Bilangan Kedua \t\t: ");
            scanf("%f", &bil2);
            printf("_____________________________________________________\n");
            hasil = bil1/bil2;
            printf("Operasi \t\t: %.2f / %.2f = %.3f", bil1, bil2, hasil);
        } else if(pilih1 == '3'){
            printf("\n\t\tOPERASI PENJUMLAHAN\n");
            printf  ("_____________________________________________________\n");
            printf("Bilangan Pertama \t: ");
            scanf("%f", &bil1);
            printf("Bilangan Kedua \t\t: ");
            scanf("%f", &bil2);
            printf("_____________________________________________________\n");
            hasil = bil1+bil2;
            printf("Operasi \t\t: %.2f + %.2f = %.3f", bil1, bil2, hasil);
        } else if(pilih1 == '4'){
            printf("\n\t\tOPERASI PENGURANGAN\n");
            printf  ("_____________________________________________________\n");
            printf("Bilangan Pertama \t: ");
            scanf("%f", &bil1);
            printf("Bilangan Kedua \t\t: ");
            scanf("%f", &bil2);
            printf("_____________________________________________________\n");
            hasil = bil1-bil2;
            printf("Operasi \t\t: %.2f - %.2f = %.3f", bil1, bil2, hasil);
        } else if(pilih1 == '5'){
            printf("\n\t\tAKAR KUADRAT\n");
            printf("_____________________________________________________\n");
            printf("Bilangan \t\t: ");
            scanf("%f", &bil1);
            hasil = sqrt(bil1);
            printf("Operasi \t\t: sqrt(%.2f) = %.3f", bil1, hasil);
        } else if(pilih1 == '6'){
            printf("\n\t\tAKAR PANGKAT TIGA\n");
            printf("_____________________________________________________\n");
            printf("Bilangan \t\t: ");
            scanf("%f", &bil1);
            hasil = cbrt(bil1);
            printf("Operasi \t\t: cbrt(%.2f) = %.3f", bil1, hasil);
        } else if(pilih1 == '7'){
            printf("\n\t\tEXP OF X\n");
            printf("_____________________________________________________\n");
            printf("Bilangan \t\t: ");
            scanf("%f", &bil1);
            hasil = exp(bil1);
            printf("Operasi \t\t: e^%.2f = %.3f", bil1, hasil);
        } else if(pilih1 == '8'){
            printf("\n\t\tOPERASI EKSPONENSIAL\n");
            printf("_____________________________________________________\n");  
            printf("Bilangan Pokok \t\t: ");
            scanf("%f", &bil1);
            printf("Pangkat \t\t: ");
            scanf("%f", &bil2);
            printf("_____________________________________________________\n");
            hasil = pow(bil1, bil2);
            printf("Operasi \t\t: %.2f ^ %.2f = %.3f", bil1, bil2, hasil);
        } else {
            printf("MASUKAN ANDA SALAH!\n");
        }
    } else if(pilih == '2'){
        printf("TRIGONOMETRI \t\t: \n");
        printf("1. sin()\n");
        printf("2. cos()\n");
        printf("3. tan()\n");
        printf("4. csc()\n");
        printf("5. sec()\n");
        printf("6. cot()\n");
        printf("7. asin()\n");
        printf("8. acos()\n");
        printf("9. atan()\n");
        printf("_____________________________________________________\n");
        printf("PILIH \t\t\t: ");
        scanf("%s", &pilih2);
        printf("_____________________________________________________\n");

        if(pilih2 == '1'){
            printf("\n\t\t\tSIN(X)\n");
            printf("_____________________________________________________\n");
            printf("Sudut(degree) \t\t: ");
            scanf("%f", &bil1);
            hasil = sin(degreeToRad(bil1));
            printf("Operasi \t\t: sin(%.2f) = %.3f", bil1, hasil);
        } else if(pilih2 == '2'){
            printf("\n\t\t\tCOS(X)\n");
            printf("_____________________________________________________\n");
            printf("Sudut(degree) \t\t: ");
            scanf("%f", &bil1);
            hasil = cos(degreeToRad(bil1));
            printf("Operasi \t\t: cos(%.2f) = %.3f", bil1, hasil);
        } else if(pilih2 == '3'){
            printf("\n\t\t\tTAN(X)\n");
            printf("_____________________________________________________\n");
            printf("Sudut(degree) \t\t: ");
            scanf("%f", &bil1);
            hasil = tan(degreeToRad(bil1));
            printf("Operasi \t\t: tan(%.2f) = %.3f", bil1, hasil);
        } else if(pilih2 == '4'){
            printf("\n\t\t\tCOSECAN(X)\n");
            printf("_____________________________________________________\n");
            printf("Sudut(degree) \t\t: ");
            scanf("%f", &bil1);
            hasil = 1/sin(degreeToRad(bil1));
            printf("Operasi \t\t: csc(%.2f) = %.3f", bil1, hasil);
        } else if(pilih2 == '5'){
            printf("\n\t\t\tSECAN(X)\n");
            printf("_____________________________________________________\n");
            printf("Sudut(degree) \t\t: ");
            scanf("%f", &bil1);
            hasil = 1/cos(degreeToRad(bil1));
            printf("Operasi \t\t: sec(%.2f) = %.3f", bil1, hasil);
        } else if(pilih2 == '6'){
            printf("\n\t\t\tCOTANGEN(X)\n");
            printf("_____________________________________________________\n");
            printf("Sudut(degree) \t\t: ");
            scanf("%f", &bil1);
            hasil = 1/tan(degreeToRad(bil1));
            printf("Operasi \t\t: cot(%.2f) = %.3f", bil1, hasil);
        } else if(pilih2 == '7'){
            printf("\n\t\tINVERS SIN(X)\n");
            printf("_____________________________________________________\n");
            printf("Sin \t\t\t: ");
            scanf("%f", &bil1);
            hasil = asin(bil1);
            hasil = radToDegree(hasil);
            printf("Operasi \t\t: asin(%.2f) = %.3f derajat", bil1, hasil);
        } else if(pilih2 == '8'){
            printf("\n\t\t INVERS COS(X)\n");
            printf("_____________________________________________________\n");
            printf("Cos \t\t\t: ");
            scanf("%f", &bil1);
            hasil = acos(bil1);
            hasil = radToDegree(hasil);
            printf("Operasi \t\t: acos(%.2f) = %.3f derajat", bil1, hasil);
        } else if(pilih2 == '9'){
            printf("\n\t\tINVERS TAN(X)\n");
            printf("_____________________________________________________\n");
            printf("Sudut(degree) \t\t: ");
            scanf("%f", &bil1);
            hasil = atan(bil1);
            hasil = radToDegree(hasil);
            printf("Operasi \t\t: atan(%.2f) = %.3f derajat", bil1, hasil);
        } else {
            printf("MASUKAN ANDA SALAH\n");
        }
    } else if(pilih == '3'){
        printf("LOGARITMA \t\t: \n");
        printf("1. log()\n");
        printf("2. ln()\n");
        printf("3. Logaritma dengan Basis Lain\n");
        printf("_____________________________________________________\n");
        printf("PILIH \t\t\t: ");
        scanf("%s", &pilih3);
        
        if(pilih3 == '1'){
            printf("\n\t\t\tLOG(X)\n");
            printf("_____________________________________________________\n");
            printf("Numerus \t\t: ");
            scanf("%f", &bil1);
            hasil = log(bil1)*logE;
            printf("Operasi \t\t: log(%.2f) = %.3f", bil1, hasil);
        } else if(pilih3 == '2'){
            printf("\n\t\t\tLOGARITMA NATURAL\n");
            printf("_____________________________________________________\n");
            printf("Numerus \t\t: ");
            scanf("%f", &bil1);
            hasil = log(bil1);
            printf("Operasi \t\t: ln(%.2f) = %.3f", bil1, hasil);
        } else if(pilih3 == '3'){
            printf("\n\t\t\tLOGARITMA\n");
            printf("_____________________________________________________\n");
            printf("Basis \t\t: ");
            scanf("%f", &bil1);
            printf("Numerus \t\t: ");
            scanf("%f", &bil2);
            hasil = log(bil2)/log(bil1);
            printf("Operasi \t\t: ^(%.2f) log(%.2f) = %.3f", bil1, bil2, hasil);
        } else {
            printf("MASUKAN ANDA SALAH\n");
        }
    } else if(pilih == '4'){
        printf("_____________________________________________________\n");
        printf("STATISTIKA \t\t: \n");
        printf("1. Rata-Rata\n");
        printf("2. Median\n");
        printf("3. Modus\n");
        printf("4. Standar Deviasi Populasi dan Variansinya\n");
        printf("5. Standar Deviasi Sampel dan Variansinya\n");
        printf("6. Menghitung SUM (Keperluan Regresi atau Korelasi)\n");
        printf("_____________________________________________________\n");
        printf("PILIH \t\t\t: ");
        scanf("%s", &pilih4);

        if(pilih4 == '1'){
            printf("\n\t\t\tAVERAGE\n");
            printf("_____________________________________________________\n");
            printf("Banyak Data \t\t: ");
            scanf("%d", &banyakData);

            for(int i = 1; i <= banyakData; i++){
                printf("Data ke-%d : ", i);
                scanf("%f", &dataStat);
                sum += dataStat;
            }
            printf("Rata-Rata \t\t: %.3f", sum/banyakData);
        } else if(pilih4 == '2'){
            printf("PROGRAM BELUM DIBUAT HEHE\n");
        } else if (pilih4 == '3'){
            printf("PROGRAM BELUM DIBUAT HEHE\n");
        } else if(pilih4 == '4'){
            printf("\n\t\tSTANDAR DEVIASI POPULASI\n");
            printf("_____________________________________________________\n");
            printf("Banyak Data \t\t: ");
            scanf("%d", &banyakData);
            float data[banyakData];
            for(int i = 0; i < banyakData; i++){
                printf("Data ke-%d : ", i+1);
                scanf("%f", &data[i]);
            }
            printf("\nStandar Deviasi \t: %.3f\n", standarDevPop(data, banyakData));
            printf("Variansi/Ragam \t\t: %.3f", pow(standarDevPop(data, banyakData), 2));
        } else if(pilih4 == '5'){
            printf("\n\t\tSTANDAR DEVIASI SAMPEL\n");
            printf("_____________________________________________________\n");
            printf("Banyak Data \t\t: ");
            scanf("%d", &banyakData);
            float data[banyakData];
            for(int i = 0; i < banyakData; i++){
                printf("Data ke-%d : ", i+1);
                scanf("%f", &data[i]);
            }
            printf("\nStandar Deviasi \t: %.3f\n", standarDevSam(data, banyakData));
            printf("Variansi/Ragam \t\t: %.3f", pow(standarDevSam(data, banyakData), 2));
        } else if(pilih4 == '6'){
            printf("\n\t\t\tJUMLAHAN\n");
            printf("_____________________________________________________\n");
            printf("1. SUM X\n");
            printf("2. Sum X^2\n");
            printf("3. Sum XY\n");
            printf("PILIH \t\t\t: ");
            scanf("%s", &pilih4_6);
            printf("_____________________________________________________\n");

            if(pilih4_6 == '1'){
                printf("Banyak Data \t\t: ");
                scanf("%d", &banyakData);
                for(int i = 1; i <= banyakData; i++){
                    printf("Data ke-%d : ", i);
                    scanf("%f", &dataStat);
                    sum += dataStat;
                }
                printf("\nJumlah Semua Data \t: %.3f", sum);
            } else if(pilih4_6 == '2'){
                printf("Banyak Data \t\t: ");
                scanf("%d", &banyakData);
                for(int i = 1; i <= banyakData; i++){
                    printf("Data ke-%d : ", i);
                    scanf("%f", &dataStat);
                    sum += pow(dataStat, 2);
                }
                printf("\nJumlah Semua Data \t: %.3f", sum);
            } else if(pilih4_6 == '3'){
                printf("Banyak Data \t\t: ");
                scanf("%d", &banyakData);
                for(int i = 1; i <= banyakData; i++){
                    printf("Data X ke-%d : ", i);
                    scanf("%f", &dataStat);
                    printf("Data Y ke-%d : ", i);
                    scanf("%f", &dataStat1);
                    sum += dataStat*dataStat1;
                }
                printf("\nJumlah Semua Data \t: %.3f", sum);
            } else {
                printf("MASUKAN ANDA SALAH\n");
            }
        }
    }
    printf("\n_____________________________________________________\n");
    printf("\tMAKASI DAH GUNAIN KALKULATOR IVAN");
    
    return 0;
}

float degreeToRad(float n){
    return n*PI/180;
}
float radToDegree(float n){
    return n*180/PI;
}

float standarDevPop(float data[], int n){
    float sum = 0, average, sumSquare = 0, stDev;
    for(int i = 0; i <= n; i++){
        sum += data[i];
    }
    average = sum/n;
    for(int i = 0; i < n; i++){
        sumSquare += pow((data[i] - average), 2);
    }
    stDev = sqrt(sumSquare/n);
    return stDev;
}

float standarDevSam(float data[], int n){
    float sum = 0, average, sumSquare = 0, stDev;
    for(int i = 0; i < n; i++){
        sum += data[i];
    }
    average = sum/n;
    for(int i = 0; i < n; i++){
        sumSquare += pow((data[i] - average), 2);
    }
    stDev = sqrt(sumSquare/(n-1));
    return stDev;
}