#include<stdio.h>
#include<ctype.h>
int main(){
	char n,n1,n2;
	scanf("%c%c%c",&n,&n1,&n2);
	if islower(n)
	{
		n = toupper(n);
		n1 = toupper(n1);
		n2 = toupper(n2);
		printf("%c%c%c",n,n1,n2);
	}
	
	return 0;
}
//check ว่าตัวอักษรแรกเป็นตัวใหญ่ไหม ถ้าเป็นให้ตัวอักษรที่รับเข้าอีกตัวเป็นตัวพิมพ์ใหญ่
