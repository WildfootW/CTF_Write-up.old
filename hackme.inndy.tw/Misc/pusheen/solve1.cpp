#include <iostream>

using namespace std;

int main()
{
    int i = 1;
    string s;
    while(getline(cin, s))
    {
        if(i % 16 == 8)
            cout << s << endl;
        i++;
    }
    return 0;
}
