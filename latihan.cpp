#include <iostream>
using namespace std;

int doubleFaktorial(int n){
    if(n == 1){
        return 1;
    } else if(n%2 == 0){
        return (n/2)*doubleFaktorial(n-1);
    } else {
        return n*doubleFaktorial(n-1);
    }
}

int main()
{
    int n;
    cin >> n;
    cout << doubleFaktorial(n);
    return 0;
}
