
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
int main(){
	string message="TNRGDMEIRXERWIXHAOTXEGNEX";
	string okey="FRONT";
	string key=okey;
	int key_size=key.size();
	int key_arr[key_size];
	int k=0;
	int pattern[key_size];
	for(int i=0;i<key_size;i++){
		for(int j=i+1;j<key_size;j++){
		if((int)key[i]>=(int)key[j]){
			char temp=key[i];
			key[i]=key[j];
			key[j]=temp;
		}
	}
	}	

	int op=0;
	for(int i=0;i<key_size;i++){
		for(int j=0;j<key_size;j++){
		if(okey[i]==key[j]){
			key[j]='*';
			pattern[op]=j;
			op++;
			break;
		}
	}	
}
		
	string enc=encrypt(message,key,pattern);
	cout<<"Encrypted Text : "<<enc<<endl;
	string dec=decrypt(message,key,pattern);
	cout<<"Decrypted Text : "<<dec;
}
