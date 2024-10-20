###
# Time converter
#
full_format = str(input("Enter an hour (hh:mm format)) : "))
first_part = full_format[0:2]
second_part = full_format[3:5]
first_part = int(first_part)
tw_format = ''
if first_part == 0 :
    tw_format = f"12:{second_part} am. "
if first_part > 0 and first_part < 12 :
    tw_format = f"{first_part}:{second_part} am. "
if first_part == 12 :
    tw_format = f"12:{second_part} pm. "
if first_part > 12 and first_part <= 23 :
    tw_format = f"{first_part - 12}:{second_part} pm. "
print(f"Time in 12 hour format: {tw_format}. ")



