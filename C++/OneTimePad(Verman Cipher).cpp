#include <string>
#include <iostream>
using namespace std;
string encryptANDdecrypt(string msg, string key){
    int msg_size=msg.size();
    int key_size=key.size();
    string res="";
    for(int i=0;i<msg_size;i++){
    	char num1 = (int)msg[i]-65;
    	char num2 = (int)key[i]-65;
        res+=char((num1^num2)+65);
    }
	
    return res;
}

int main() {
    string msg,key;
    cout<<"Enter Message: ";
    getline(cin,msg);
    cout<<"Enter Key: ";
    getline(cin,key);
    string enc=encryptANDdecrypt(msg,key);
    cout <<"\nEncrypted Message: "<<enc;
    string dec=encryptANDdecrypt(enc,key);
    cout <<"\nDecrypted Message: "<<dec;
    return 0;
}
