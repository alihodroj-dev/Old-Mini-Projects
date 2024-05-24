#include <iostream>
#include <string>
#include <cstdlib>
#include <fstream>
using namespace std;

void Question(){
    cout << "What would you like to do?" << endl;
    cout << endl << "1)" << "See Addition Information" << endl;
};

int main(){
    //Login Variables
    int answer;
    int num1 = 0;
    int num2 = 1;
    int num3 = 0;
    int num4 = 3;
    string login_email;
    string login_password;
    string client_email;
    string client_password;
    char client_name[50];

    //Info Variables
    string username;
    string value;
    string date_created;
    int num5 = 0;
    int num6 = 4;
    char filename[50];

    //OPENING FILES
    ifstream Client_Accounts;
    ifstream info;

    Client_Accounts.open("Clients_Accounts.txt");
    cout << "********************************************************************************";
    cout << "                           Welcome to Hodroj Bank                               ";
    cout << "********************************************************************************" << endl;
    cout << "Please Login to Your Account:" << endl;

    //LOGIN PROCESS
    while(num1 < num2){
        cout << "Email:";
        cin >> login_email;
        cout << "Password:";
        cin >> login_password;
        while(num3 < num4){
            Client_Accounts >> client_name;
            Client_Accounts >> client_email;
            Client_Accounts >> client_password;
            Client_Accounts >> filename;
            if(client_email == login_email && client_password == login_password){
                cout << "Welcome " << client_name << endl;
                num3 = 4;
                num1 = 2;
            };
        };
    };
    //DOING PROCESS
    info.open(filename);
    Question();
    cin >> answer;
    if(answer == 1){
        info >> username >> username;
        info >> date_created >> date_created;
        info >> value >> value;
        cout << username << endl;
        cout << date_created << endl;
        cout << value << endl;
    };
    return 0;
};