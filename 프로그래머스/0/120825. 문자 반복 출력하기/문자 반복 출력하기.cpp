#include <string>
#include <vector>
#include<algorithm>

using namespace std;

string solution(string my_string, int n) {
    string answer = "";
    for(int i =0; i < my_string.size(); i++)
    {
        {
            int j = 0;
            while(j < n)
            {
                answer += my_string[i];
                j++;
            }
        }
    }


    return answer;
}