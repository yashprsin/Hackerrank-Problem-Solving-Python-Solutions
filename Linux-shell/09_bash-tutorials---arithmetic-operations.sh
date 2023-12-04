read -p "Enter the expression: " exp
printf "%.3f" $(echo $exp | bc -l)