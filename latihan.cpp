#include <iostream>
using namespace std;

int fibonacci(int n){
    if(n == 1 or n == 0){
        return 1;
    } else {
        return fibonacci(n-1) + fibonacci(n-2);
    }
}

int main()
{
    // Program membuat suku ke-n bilangan dalam barisan fibonacci
    int n;
    cout << "PROGRAM BARISAN FIBONACCI" << endl;
    cout << "Suku ke berapa yang ingin Anda cari? : ";
    cin >> n;
    cout << "Suku ke-" << n << " dalam barisan fibonacci adalah " << fibonacci(n);
    return 0;
}
