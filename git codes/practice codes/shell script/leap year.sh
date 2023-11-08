echo "enter year"
read a
if [ `expr $a % 4` == 0 ] && [ `expr $a % 100` -ne 0 ] || [ `expr $a % 400` == 0 ]
then
echo "leap"
else 
echo "no leap"
fi
