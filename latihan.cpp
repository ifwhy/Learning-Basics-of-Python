#include <iostream>
using namespace std;

int gcd(int a);
int bil1, bil2, fpb = 0;
int main()
{
    // Greatest common factor (fpb)
    cout << "Masukkan bilangan pertama : ";
    cin >> bil1;
    cout << "Masukkan bilangan kedua : ";
    cin >> bil2;

    if(bil2 > bil1){
        gcd(bil2);
    } else {
        gcd(bil1);
    }
    printf("FPB-nya adalah %d", fpb);
    return 0;
}

int gcd(int a){
    for(int i = 1; i <= a; i++){
            if(bil1%i == 0 && bil2%i == 0){
                if(i >= fpb){
                    fpb = i;
                }
            }
        }
    return fpb;
}
