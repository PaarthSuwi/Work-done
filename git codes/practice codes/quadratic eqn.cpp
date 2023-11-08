# include<stdio.h>
# include<conio.h>
# include<math.h>

int main ()
{
    
   float a,b,c;
   printf ("Enter the values of coefficient: a, b, and c \n");
   scanf (" %f %f %f", &a, &b, &c);
    
   float discriminant;
   discriminant= sqrt(b*b-4*a*c);
    
   float r1, r2;
    
   if (discriminant>0)
   {
      r1 = -b+sqrt (discriminant)/(2*a);
      r2 = -b-sqrt (discriminant)/(2*a);
      printf ("The roots of the equation are = %f %f", r1, r2);
   }
   else if (discriminant==0)
   {
      r1 = -b/(2*a);
      r2 = -b/(2*a);
      printf ("The roots of the equation are equal having the value =%f %f", r1, r2);
   }
   else
      printf("The roots of the equation are imaginary and hence we can not compute them");
}

