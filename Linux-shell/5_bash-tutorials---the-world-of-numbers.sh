read X
read Y
a=$(expr $X + $Y)
echo "$a"
c=$(expr $X - $Y)
echo "$c"
d=$(expr $X \* $Y)
echo "$d"
e=$(expr $X / $Y)
echo "$e"