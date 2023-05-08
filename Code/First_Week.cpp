//First_Week.cpp
#include<iostream>
#include<cmath>
using namespace std;
int main()
{
    float a=1,b=1;
    int t_plus_L=0;
    while(a!=0)
    {
        b=a;
        a/=2;
        t_plus_L++;
    }
    float c=3,d=1,t=1;
    while(c-1==2*d)
    {
        d=2*d+1;
        c=2*c+1;
        t++;
    }
    float u=2*d;
    while(u/2==d)
    {
        u*=2;d*=2;
    }
    cout<<t_plus_L<<endl;
    cout<<"上溢值为："<<d<<endl<<"下溢值为："<<pow(2,t-t_plus_L)<<endl
    <<"机器精度为："<<pow(2,-t)<<endl;
    return 0;
}