tp = int(input ("How many TRUE POSITIVE predictions have been made? "))
fp = int(input ("How many FALSE POSITIVE predictions have been made? "))
fn = int(input ("How many FALSE NEGATIVE predictions have been made? "))
tn = int(input ("How many TRUE NEGATIVE predictions have been made? "))
accuracy = ((tp+tn)/(tp+tn+fp+fn))*100
print (f"The model's accuracy is {'%.1f' % accuracy}%")