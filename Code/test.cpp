#include <stdio.h>
#include<math.h>
#include<time.h>
#include<stdlib.h>
#include<conio.h>
#define N 1000
int main()
{
	double a = 0, l = 0;	//��ĳ��ȵ�ƽ����֮��ļ��
	double x = 0, y = 0;	//xΪ����е����ƽ���ߵľ��룬yΪ����ƽ���߼нǵ�����ֵ
	double PI;
	long n = 0, m = 0;//nΪ�ܹ�ʵ�������mΪ��ƽ�����ཻ��ʵ�����
	
	{
		scanf("������ƽ���߼��a=%lf", &a);//����ƽ���߼��
		scanf("��������ĳ���l=%lf,l<a", &l);//������ĳ���
	}
	for (n = 0; n < N; n++)
	{
		srand(time(NULL));
		x = 0.5*a*((rand() % 100000) / 100000.0);
		y = (rand() % 100000) / 100000.0;
		if (x < 0.5 * l * y)		//����ƽ�����ཻ
			m++;
	}
	PI = 2 * n * l / (a * m);
	printf("�еĽ���ֵΪ%lf", PI);
	getch();
	return 0;
}

