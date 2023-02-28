#include<stdio.h>
#include<math.h>
double perimeter(double x, double y);
double area(double x, double y);

double main(){
	double x,y,total,real;
	scanf("%lf %lf",&x,&y);
	total = perimeter(x,y);
	real = area(x,y);
	printf("Perimeter: %.2lf\n",total);
	printf("Area: %.2lf\n",real);
	return 0;
}
double perimeter(double x, double y)
{
	double z,full;
	z = sqrt((x*x)+(y*y));
	full = x+y+z;
	return full;
}
double area(double x, double y)
{
	return 0.5*(x*y);
}
/* จงเขียนโปรแกรมที่ประกอบไปด้วยฟังก์ชันเพื่อคำนวณหาเส้นรอบรูป  และพื้นที่ของรูปสามเหลี่ยมมุมฉาก เมื่อให้ความยาวของด้านสองด้าน (a และ b)
   กำหนดให้ main() มีเฉพาะการเรียกฟังก์ชันย่อยเท่านั้น โดยให้สร้างฟังก์ชันย่อย 2 ฟังก์ชัน คือ 
   perimeter() - หาเส้นรอบรูป
   area()      - หาพื้นที้
   * ถ้าใช้ library math.h เวลา compile ให้เพิ่ม -lm ด้วย เช่น gcc source.c -lm -o output.out */
