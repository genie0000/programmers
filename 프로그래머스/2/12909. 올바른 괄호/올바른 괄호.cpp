#include<string>
#include <iostream>
#include <algorithm>
using namespace std;

bool solution(string s)
{
    bool answer = true;
    char a = '(';
    int b = 0;
    for (int i = 0; i < s.size(); i++)
    {
        if (a == s[i] && b >= 0 )
        {
            b += 1;
        }
        else
        {
            b -= 1;
        }
    }
    if (b != 0)
    {
        answer = false;
    }
    else
    {
        answer = true;
    }
    cout << "Hello Cpp" << endl;
    return answer;
}