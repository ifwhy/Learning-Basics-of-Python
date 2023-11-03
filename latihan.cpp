#include <iostream>
using namespace std;

void decToBinOkt(int n, int p){
    int i = 0, data[n]; 
    while(n > 0){
        data[i] = n % p;
        n /= p;
        i++;
    }
    for(int j = i-1; j >= 0; j--){
        cout << data[j] << " ";
    }
}

int main()
{
    int n;
    cout << "Bilangan Desimal : ";
    cin >> n;

    cout << "Bilangan biner : ";
    decToBinOkt(n, 2);
    cout << endl << "Bilangan oktal : ";
    decToBinOkt(n, 8);
    return 0;
}
