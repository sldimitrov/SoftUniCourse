# Read User input
number_of_bitcoins = int(input())
num_of_chinese_value = float(input())
compromission = float(input())
# Logic
leva = number_of_bitcoins * 1168
dollars = num_of_chinese_value * 0.15
dollars_in_lv = dollars * 1.76
leva += dollars_in_lv
euro = (leva / 1.95)
discount = euro * compromission / 100
total_output = euro - discount

print(round(total_output,2))
# Print User output