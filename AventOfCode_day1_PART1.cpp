#include<iostream>
using namespace std;

int main()
{
	int Numbers[700];
	int index = 0;
	while(1)
	{
		int number;
		cin>>number;
		if(number == 0) //si es 0 salimos
			break;
		Numbers[index] = number; //guardamos el numero
		index++;
	}
	
	bool encontrado = false;
	long multiplicacion = 0;
	
	for(int i=0;i<index;i++)
	{
		for(int j=0;j<index;j++)
		{
			if(Numbers[i] + Numbers[j] == 2020)
			{
				multiplicacion =  Numbers[i] * Numbers[j];
				cout<<Numbers[i]<<" * "<<Numbers[j]<<" = "<<multiplicacion<<endl;
				encontrado = true;
				break;
			}
		}
		if(encontrado)
		{
			break;
		}
	}
	
}
