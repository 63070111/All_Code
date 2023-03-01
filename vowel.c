#include<stdio.h>
int main(){
	char name;
	scanf("%c",&
		name);
	switch(name)
	{
		case 'a': printf("eve");break;
		case 'A': printf("eve");break;
		case 'e': printf("eve");break;
		case 'E': printf("eve");break;
		case 'i': printf("milk");break;
		case 'I': printf("tafei");break;
		case 'o': printf("milk");break;
		case 'O': printf("tafei");break;
		case 'u': printf("milk");break;
		case 'U': printf("tafei");break;
		default:printf("No");
	}
	return 0;
}
//ถ้าพิมพ์สระ 1 ตัว ให้พิมพ์ออกตามในแต่ละกรณี ถ้าไม่ใช้สระให้พิมพ์ออก No
