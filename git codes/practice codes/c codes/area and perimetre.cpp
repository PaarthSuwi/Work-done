#include <stdio.h>
#include <math.h>

int main()
{
    float radius, length, width, a, b, c, height, area;
    int n;
    float perimeter;
 
    //Perimeter and Area of rectangle
    
    printf("\n 1. Perimeter of rectangle \n");
    printf("\n Enter width and length of the rectangle : \n");
    scanf("%f%f", &width,& length);
    perimeter = 2 * (width + length);
    printf("\nPerimeter of rectangle is: %.3f\n", perimeter);
    area = width*length;
    printf(" Area of rectangle is : %.3f\n", area);
 
 
    //Perimeter and Area of circle
    printf("\n 2.Perimeter of circle \n");
    printf("\n Enter the radius of the circle : ");
    scanf("%f", &radius);
    perimeter = 2 * (22 / 7) * radius;
    printf("\nPerimeter of circle is: %.3f\n", perimeter);
    area = 3.14 * radius * radius;  
    printf("\nArea of circle : %0.4f\n", area);  
 
    //Perimeter and Area of right angled triangle
    printf(" \n 3.Perimeter of right angled triangle \n");
    printf("\n Enter the width and height of the right angled triangle : ");
    scanf("%f%f", &width, &height);
    perimeter = width + height + sqrt(width * width + height * height);
    printf("\nPerimeter of right angled triangle is: %.3f\n", perimeter);
    area = 0.5*width*height;
    printf("\nArea of right angled triangle is: %.3f\n", area);

    return 0;
} 
