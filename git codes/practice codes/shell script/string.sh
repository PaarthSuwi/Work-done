echo "enter string 1"
read str1
echo "enter string 2"
read str2

if [ "$str1" == "$str2" ]
then 
	echo "string1 equals to string2"
else
	echo "string1 not equal to string2"
fi

concat="$str1$str2"
echo "concatinated string is $concat"

length=`expr length "$concat"`
echo "length of string is $length"

for((i=0;i<length;i+=2))
do
	echo "${concat:i:1}"
done

reverse=""
for((i>length-1;i>=0;i--))
do
	reverse="$reverse${concat:i:1}"
done
echo "reverse is $reverse"

if [ "$reverse" == "$concat" ]
then
	echo "palindrome"
else
	echo "not palindrome"
fi


echo "enter string"
read st
echo "enter charcater"
read ch
count=`expr "$st"| grep -o "$ch"| wc -l`
echo "in "$st" this "$ch" repeats $count times"
