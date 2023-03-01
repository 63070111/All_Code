#include<stdio.h>
#include<ctype.h>
int main(){
	char name;
	scanf("%c",&name);
	if islower(name)
		printf("lowercase");
	else if isupper(name)
		printf("uppercase");
	else if isalnum(name)
		printf("number");
	else
		printf("error");

	return 0;
}
//ใส่ตัวอักษรมา 1 ตัว แล้วแสดงผลตามที่เงื่อนไขกำหนด
