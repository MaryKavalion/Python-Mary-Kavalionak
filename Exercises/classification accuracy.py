total_num = int(input ("How many predictions have been made?"))
correct_predict = int(input ("How many of them have been correct?"))
accuracy = correct_predict/total_num*100
print (f"The model's accuracy is {'%.1f' % accuracy}%")