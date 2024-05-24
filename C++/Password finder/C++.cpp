#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
using namespace std;

int main(){
    int num = 0;
    int loop_num = 1;
    string checker;
    ifstream file;
    file.open("Ali Account.txt");
    if(!file.is_open()){
        cout << "Error 99 occured";
        return 0;
    };
    while(num < loop_num){
        file >> checker;
        if(checker == "Password"){
            file >> checker >> checker;
            cout << "Your password is:" << checker;
            num = 2;
        }
    };
    return 0;
};