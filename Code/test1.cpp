#include <stdio.h>
#include<math.h>
#include<time.h>
#include<stdlib.h>
#include <conio.h>
#define N 1000000
int main()
{
	double a = 0, l = 0;	//��ĳ��ȵ�ƽ����֮��ļ��
	double x = 0, y = 0;	//xΪ����е����ƽ���ߵľ��룬yΪ����ƽ���߼нǵ�����ֵ
	double PI;
	long n = 0, m = 0;//nΪ�ܹ�ʵ�������mΪ��ƽ�����ཻ��ʵ�����
	{
		puts("������ƽ���߼��a");
		scanf("%lf",&a);//����ƽ���߼��
		puts("��������ĳ���l,l<a");
		scanf("%lf", &l);//������ĳ���
	}
	srand(time(NULL));
	for (n = 0; n < N; n++)
	{
		x = 0.5*a*((double)rand() / RAND_MAX);
		//rand(time(NULL) + n);
		y = sin(acos(0) * (double)rand() / RAND_MAX);
		//y = (double)rand() / RAND_MAX;

		if (x < 0.5 * l * y)		//����ƽ�����ཻ
			m++;
		//printf("x=%lf y=%lf m=%ld, n=%ld\n",x,y, m, n);
	}
	PI = 2 * n * l / (a * m);
	printf("�еĽ���ֵΪ%lf", PI);
	getch();
	return 0;
}

