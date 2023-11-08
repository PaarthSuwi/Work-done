echo -n "Enter number : "
read n
x=0
y=0
z=$n 
while [ $n -gt 0 ]
do
    x=$(( $n % 10 ))
    n=$(( $n / 10 )) 
    y=$(( $y + 1)) 
done
echo  "Numnber of digit in a $z is $y"
