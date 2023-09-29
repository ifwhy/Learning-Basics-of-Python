#include <iostream>
using namespace std;

int main()
{
    int n, k = 0;
    cin >> n;

    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= i; j++){
            if(k == 10){
                k = 0;
            }
            cout << k;
            k++;
        }
        cout << endl;
    }
    return 0;
}
