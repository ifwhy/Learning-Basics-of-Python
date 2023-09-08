#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cout << "Masukkan sebuah bilangan : ";
    cin >> n;

    for(int i = 1; i <= n; i++){
        if(i == 1 or i == n){
            for(int j = 1; j <= n; j++){
                cout << "*";
            }
            cout << endl;
        } else {
                cout << "*";
                for(int l = 1; l <= n-2; l++){
                    cout << " ";
                } 
                cout << "*";
                cout << endl;
        }
    }
    return 0;
}
