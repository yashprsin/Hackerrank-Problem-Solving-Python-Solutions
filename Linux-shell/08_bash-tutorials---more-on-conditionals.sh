read -p "Enter the length of side X: " X
read -p "Enter the length of side Y: " Y
read -p "Enter the length of side Z: " Z

if [ "$X" -eq "$Y" ] && [ "$X" -eq "$Z" ]; then
    echo "EQUILATERAL"
elif [ "$X" -eq "$Y" ] || [ "$X" -eq "$Z" ] || [ "$Y" -eq "$Z" ]; then
    echo "ISOSCELES"
else
    echo "SCALENE"
fi