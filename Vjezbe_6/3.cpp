#include <iostream>
#include <algorithm>

using namespace std;

void brojevi(float polje[], int N)
{
  for( int i = 0; i < N; i++)
  {
    std::cout << polje[i] << " ";
  }
  std::cout << std::endl;
}

void a_b(float polje[], int N, int a, int b)
{
    for( int i = 0; i < N; i++)
    {
        if(polje[i]>=a && polje[i]<=b) 
        { std::cout << polje[i] << " ";
        std::cout << std::endl;
        }
    }
}
void zamjena(float polje[], int x, int y)
{
    float n;
    n=polje[x];
    polje[x]=polje[y];
    polje[y]=n;
    
}




int main()
{
    float polje[10]={1,3,53,-5,4,-22,7,-8,-2,54};
    brojevi(polje, 10);
    a_b(polje, 10, -2, 10);
    zamjena(polje, 2, 6);
    brojevi(polje, 10);
    std::reverse(std::begin(polje), std::end(polje));
    brojevi(polje, 10);
    std::sort(std::begin(polje), std::end(polje));
    brojevi(polje, 10);
    return 0;
}