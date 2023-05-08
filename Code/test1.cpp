#include <stdio.h>
#include<math.h>
#include<time.h>
#include<stdlib.h>
#include <conio.h>
#define N 1000000
int main()
{
	double a = 0, l = 0;	//针的长度的平行线之间的间距
	double x = 0, y = 0;	//x为针的中点距离平行线的距离，y为针与平行线夹角的正弦值
	double PI;
	long n = 0, m = 0;//n为总共实验次数，m为与平行线相交的实验次数
	{
		puts("请输入平行线间距a");
		scanf("%lf",&a);//输入平行线间距
		puts("请输入针的长度l,l<a");
		scanf("%lf", &l);//输入针的长度
	}
	srand(time(NULL));
	for (n = 0; n < N; n++)
	{
		x = 0.5*a*((double)rand() / RAND_MAX);
		//rand(time(NULL) + n);
		y = sin(acos(0) * (double)rand() / RAND_MAX);
		//y = (double)rand() / RAND_MAX;

		if (x < 0.5 * l * y)		//针与平行线相交
			m++;
		//printf("x=%lf y=%lf m=%ld, n=%ld\n",x,y, m, n);
	}
	PI = 2 * n * l / (a * m);
	printf("π的近似值为%lf", PI);
	getch();
	return 0;
}

