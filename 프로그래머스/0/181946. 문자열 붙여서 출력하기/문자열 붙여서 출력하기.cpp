#include <iostream>
#include <string>

using namespace std;

int main(void) {
    string s = "";
    string answer = "";
    string str1, str2;
    cin >> str1 >> str2;
    s = str1 + str2;
    for (int i = 0; i < s.length(); i++)
       if (s[i] == ' ')
           continue;
       else
           answer += s[i];
    cout << answer;

           
    return 0;
}