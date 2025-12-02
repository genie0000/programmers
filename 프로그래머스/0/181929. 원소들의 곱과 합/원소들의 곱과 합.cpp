#include <string>
#include <vector>

using namespace std;

int solution(vector<int> num_list) {
    int answer = 0;
    int value = 0;
    int valuee = 1;
    for (int i = 0; i < num_list.size(); i++){
        value += num_list[i];
        valuee *= num_list[i];
    }
                           
    
    if (value * value < valuee){
        answer = 0;
    }
    else{
        answer = 1;
    }
        
    return answer;
}