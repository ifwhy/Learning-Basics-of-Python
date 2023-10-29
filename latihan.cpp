#include <iostream>
#include <math.h>
using namespace std;

float sum(float data[], int n);
float product(float dataX[], float dataY[], int n);
float kuadrat(float data[], int n);

int main()
{
    int n;
    float rPembilang, rPenyebut, r, slopeReg, constReg;

    cout << "\t\tREGRESI DAN KORELASI" << endl;
    cout << "______________________________________________________\n";
    cout << "Banyak Data \t\t: ";
    cin >> n;
    cout << "______________________________________________________\n";
    cout << endl;

    float dataX[n], dataY[n];
    for(int i = 0; i < n; i++){
        cout << "Data X ke-" << i+1 << " \t\t: ";
        cin >> dataX[i];
    }   
    cout << "______________________________________________________\n";

    cout << endl;
    for(int i = 0; i < n; i++){
        cout << "Data Y ke-" << i+1 << " \t\t: ";
        cin >> dataY[i];
    }
    cout << "______________________________________________________\n";
    cout << endl;
    cout << "Jumlah Data X adalah \t: " << sum(dataX, n) << endl;
    cout << "Jumlah Data Y adalah \t: " << sum(dataY, n) << endl;
    cout << "Jumlah Data X^2 adalah \t: " << kuadrat(dataX, n) << endl;
    cout << "Jumlah Data Y^2 adalah \t: " << kuadrat(dataY, n) << endl;
    cout << "Jumlah Data XY adalah \t: " << product(dataX, dataY, n) << endl << endl;
    cout << "______________________________________________________\n";

    r = (n*product(dataX, dataY, n) - sum(dataX, n)*sum(dataY, n))/(sqrt((n*kuadrat(dataX, n) - sum(dataX, n)*sum(dataX, n))*(n*kuadrat(dataY, n) - sum(dataY, n)*sum(dataY, n))));

    cout << "KK Pearson (R)\t\t: " << r << endl;
    cout << "Hubungan \t\t: ";
    if(r > 0) {
        cout << "Positif - ";
    } else {
        cout << "Negatif - ";
    }

    if(abs(r) > 0.75 && abs(r) <= 1){
        cout << "Kuat" << endl;
    } else if(abs(r) > 0.5 and abs(r) <= 0.75){
        cout << "Sedang" << endl;
    } else if(abs(r >= 0) and abs(r) <= 0.5){
        cout << "Lemah" << endl;
    }
    cout << "Koef. Determinasi (R^2)\t: " << pow(r, 2) << endl;
    cout << "Besar Pengaruh X thd Y \t: " << pow(r, 2)*100 << "\%"; 

    // Regresi
    constReg = (sum(dataY, n)*kuadrat(dataX, n) - sum(dataX, n)*product(dataX, dataY, n))/(n*kuadrat(dataX, n) - sum(dataX, n)*sum(dataX, n));
    slopeReg = (n*product(dataX, dataY, n) - sum(dataX, n)*sum(dataY, n))/(n*kuadrat(dataX, n) - sum(dataX, n)*sum(dataX, n));

    if(constReg > 0){
        cout << "\nPersamamaan Regresi \t: " << slopeReg << "x + " << constReg << endl; 
    } else {
        cout << "\nPersamamaan Regresi \t: " << slopeReg << "x " << constReg << endl; 
    }
    cout << "______________________________________________________" << endl << endl;;




    return 0;
}

float sum(float data[], int n){
    float sum = 0;
    for(int i = 0; i < n; i++){
        sum += data[i];
    }
    return sum;
}

float product(float dataX[], float dataY[], int n){
    float sum = 0;
    for(int i = 0; i < n; i++){
        sum += dataX[i]*dataY[i];
    }
    return sum;
}

float kuadrat(float data[], int n){
    float sum = 0;
    for(int i = 0; i < n; i++){
        sum += pow(data[i], 2);
    }
    return sum;
}