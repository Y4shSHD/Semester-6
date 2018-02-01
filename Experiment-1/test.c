#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
 
int mutex=1,x=0;       //semaphore references and item number
int empty=3,full=0;    //buffer references 
int produConsu(int min, int max)
{
   int r;
   r = (rand() % (max + 1 - min)) + min;
   return r;
}
int wait(int s)//Acquires CS for itself
{
    return (--s);
}
 
int signal(int s)//Releases CS from itself
{
    return(++s);
}
 
void producer()//thread Producer
{
    mutex=wait(mutex);
    full=signal(full);
    empty=wait(empty);
    x++;
    printf("\nProducer produces the item %d",x);
    mutex=signal(mutex);
}
 
void consumer()//thread Consumer
{
    mutex=wait(mutex);
    full=wait(full);
    empty=signal(empty);
    printf("\nConsumer consumes item %d",x);
    x--;
    mutex=signal(mutex);
}
int main()
{
    int n,buffer=0,b=0;
    int time=0;
    int t=0;    
    int wait(int);
    int signal(int);
    printf("\nEnter buffer size: ");
    scanf("%d",&empty);
    printf("\nEnter system timeout: ");
    scanf("%d",&time);
    buffer=empty;   
    while(t<=time) 
    {	
        n= produConsu(1,2);
        //printf("\nRandom Generated: %d",n);
        switch(n)
        {
            case 1:    if((mutex==1)&&(empty!=0))
                        producer();
                    else
                        { printf("\nBuffer's full!! Calling Consumer...");
			  consumer();
			}
                    break;
            case 2:    if((mutex==1)&&(full!=0))
                        consumer();
                    else
                        { printf("\nBuffer's empty!! Calling Producer...");
			  producer();
			}
                    break;
            default:    printf("\nError at switcher!!!");
        } t++; 
    }
    printf("\nThanks for using!!!");
    printf("\nE");
    
    printf("x");
    
    printf("i");
    
    printf("t");
  
    printf("t");
    
    printf("i");
      
    printf("n");
    
    printf("g");
    
    int i;
    for(i=0;i<3;i++)   
    {
	printf(". ");
	
    }
    printf("\n");
    exit(0);
    return 0;
}
 

