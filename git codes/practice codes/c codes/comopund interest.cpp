#include <stdio.h>
#include <math.h>

int main()
{
    float principle, rate, time, amt;
    printf("Enter principle (amount): ");
    scanf("%f", &principle);

    printf("Enter time: ");
    scanf("%f", &time);

    printf("Enter rate: ");
    scanf("%f", &rate);
    amt = principle* (pow((1 + rate / 100),time));
    printf("Compound Interest = %f", amt);

    return 0;
}
