
#include<bits/stdc++.h>
using namespace std;

string encrypt(string message,string key,int pattern []){
	int row=ceil((float)message.size()/(float)key.size());
	
	char arr[row][key.size()];
	int k=0;
	for(int i=0;i<row;i++){
		for(int j=0;j<key.size();j++){
			if(k>=message.size()){
				arr[i][pattern[j]]='x';
			}
			else{
			arr[i][pattern[j]]=(char)message[k];
		    }
			k++;
		}
	}
	
		string res="";
		for(int i=0;i<key.size();i++){
		for(int j=0;j<row;j++){
			res+=arr[j][i];
		}
	}
	return res;
}
string decrypt(string message, string key, int pattern[]){
	int row=ceil((float)message.size()/(float)key.size());
	char arr[row][key.size()];
	int k=0;
	for(int i=0;i<key.size();i++){
		for(int j=0;j<row;j++){
			arr[j][i]=message[k];
			k++;
		}
	}
	string res="";
	for(int i=0;i<row;i++){
		for(int j=0;j<key.size();j++){
			res+=arr[i][pattern[j]];
		}
	}
	return res;
}
