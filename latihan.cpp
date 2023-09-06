#include<bits/stdc++.h>
using namespace std;

int main()
{
    float n;
    cin >> n;

    if(n == trunc(n)){
        cout << n << " " << n;
    } else if (n > 0){
        cout << trunc(n)<< endl;
        cout << trunc(n+1) ;
    } else {
        cout << trunc(n)-1 << endl;
        cout << trunc(n)  ;
    }
   
    return 0;
}
