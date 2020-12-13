#include<iostream>
using namespace std;
//dia 2

int Search(int array[],int index  );


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
	Search(Numbers,index); //para buscar cual conjunto de tres numeros suma 2020
	

	
	
	return 0;
}

int Search(int Numbers[],int index )
{
	for(int i=0;i<index;i++)
	{
		for(int j=0;j<index;j++)
		{
			for(int o=0;o<index;o++)
			{
				if(Numbers[i]  + Numbers[j]  +  Numbers[o] == 2020) //si encontramos los mltiplicamos
				{				
					int multiplicacion = Numbers[i] *  Numbers[j] *  Numbers[o];
					cout<<Numbers[i]<<"  *  "<<Numbers[j]<<" *  "<<Numbers[o]<<" = "<<multiplicacion; //mostramos la multiplicaion
					return multiplicacion;
					
				}
			}
		}
		
	}
}










