#include <iostream>
using namespace std;

int main()
{
    // Program membuat n suku pertama dalam barisan fibonacci
    int n, fn, fn1 = 1, fn2 = 0;
    cout << "PROGRAM MEMBUAT N SUKU PERTAMA DALAM BARISAN FIBONACI" << endl;
    cout << "Masukkan sebuah bilangan asli : ";
    cin >> n;

    cout << n << " suku pertama dalam barisan fibonacci adalah : ";    for(int i = 1; i <= n; i++){
        fn = fn1 + fn2;
        cout << fn << " ";
        fn2 = fn1;
        fn1 = fn;
    }
    return 0;
}
