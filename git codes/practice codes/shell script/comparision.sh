echo "enter first :"
read a
echo "enter second:"
read b
if [[ $a -gt $b ]]
then
	echo "$a is gretaer than $b"
else
	echo "$a is smaller than $b"
fi
