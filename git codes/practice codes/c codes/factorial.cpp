#include <stdio.h>

void multiply(int result[], int num, int *size)
{
    int carry = 0, prod;
    for(int i=0; i<*size; i++)
    {
        prod = result[i] * num + carry;
        result[i] = prod % 10;
        carry = prod / 10;
    }
    while(carry)
    {
        result[*size] = carry % 10;
        carry /= 10;
        (*size)++;
    }
}

void factorial(int n)
{
    int result[1000] = {0};
    result[0] = 1;
    int size = 1;

    for(int i=2; i<=n; i++)
    {
        multiply(result, i, &size);
    }

    printf("%d! = ", n);
    for(int i=size-1; i>=0; i--)
    {
        printf("%d", result[i]);
    }
    printf("\n");
}

int main()
{
    int start, end;
    printf("Enter the start and end numbers of the range: ");
    scanf("%d%d", &start, &end);

    for(int i=start; i<=end; i++)
    {
        factorial(i);
    }

    return 0;
}

