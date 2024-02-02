# Read User input
rec_in_sec = float(input())
len_in_m = float(input())
sec_per_m = float(input())
# Logic
time_in_s = len_in_m * sec_per_m
delay = (len_in_m // 50) * 30
total_time = time_in_s + delay
total_time = round(total_time,2)

if total_time < rec_in_sec:
    print("Yes! The new record is %.2f seconds." % total_time)
else:
    diff = abs(rec_in_sec - total_time)
    print("No! He was %.2f seconds slower." % diff)
# Print User output