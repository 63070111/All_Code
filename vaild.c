#include<stdio.h>
int main(){
	int one,two,three;
	scanf("%d %d %d",&one,&two,&three);
	if ((one+two>three) && (one+three>two) && (two+three>one))
	{
		printf("Triangle is valid.");
	}
	else
		printf("Triangle is not valid.");

}
//หาว่าเป็นรูปสามเหลี่ยมด้านเท่าไหม
