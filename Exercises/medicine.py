def try_parse_num (text):
    try:
        return float(text)
    except:
        return -1

age = try_parse_num(input("How old is the person, full years? "))
weight = try_parse_num(input("What is the person's weight (kg)? "))

age_adolesc = 12
weight_adolesc = 40
age_children_mid = 7
weight_children_mid = 26
min_age_child = 3
min_weight_child = 15

dose_0 = "no pills for this age or weight."
dose_1 = "0.5 pill."
dose_2 = "0.5 - 1 pill."
dose_3 = "1 pill."
dose_4 = "1-2 pills."

msg = "The recommended number of pills is: "


if (age > 125 or age < 0) or (weight > 250 or weight < 5):
    print ("Wrong input. Pls try again later")
elif age > age_adolesc and weight > weight_adolesc:
    print (msg, dose_4)
elif age > age_adolesc and weight <= weight_adolesc:
    print (msg, dose_3)
elif age >= age_children_mid and weight >= weight_children_mid:
    print (msg, dose_2)
elif age >= min_age_child and weight >= min_weight_child:
    print (msg, dose_1)
else:
    print (msg, dose_0)