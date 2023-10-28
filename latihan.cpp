#include <iostream>
using namespace std;

int main()
{
    int n, k;
    int max, min;

    cin >> n;
    for(int i = 1; i <= n; i++){
        cin >> k;
        if(i == 1){
            min = k;
            max = min;
        }
        if(k < min){
            min = k;
        } else if (k > max) {
            max = k;
        }
        cout << max << " " << min << endl;
    }
    return 0;
}
