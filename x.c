#include<stdio.h>
int main(){
	float number;
	float row,colum;
	scanf("%f",&number);
	for (row = 1; row <= number;row++)
	{
		for(colum = 1;colum<=number;colum++)
		{
			if (row == colum || colum ==(number-row+1))
				printf("-");
			else
				printf("#");
		}
		printf("\n");
		
	}
	
	return 0;
}
//สร้างรูปตัว X
Footer
© 2023 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
