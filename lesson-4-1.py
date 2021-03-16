from sys import argv

script_name, output_hours, rate_per_hour, bonus = argv

salary = float(output_hours) * float(rate_per_hour) + float(bonus)
# print(argv)

print("Output, hours: " + output_hours)
print("Rate, $ per hour: " + rate_per_hour)
print("Bonus, $: " + bonus)
print("SALARY, $: " + str(salary))
