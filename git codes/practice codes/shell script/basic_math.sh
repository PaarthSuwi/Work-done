echo "enter value a:"
read a
echo "enter value b:"
read b

val=`expr $a + $b`
echo " add of both is $val"

val=`expr $a - $b`
echo " diff of both value $val"

val=`expr $a \* $b`
echo " mul of both value $val"

val=`expr $a / $b`
echo " div of both value $val"

val=`expr $a % $b`
echo "Remainder of both $val"

