#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> array) {
    vector<int> answer;
    int a = 0;
    int b = 0;
    for (int i = 0; i < array.size(); i++)
    {
        if(a < array[i])
        {
            a = array[i];
            b = i;
        }
    }
    answer.push_back(a);
    answer.push_back(b);
    return answer;
}