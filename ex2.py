tip_percent = 0.21
bill = 55
tip = round(tip_percent*bill,2)
print("A good tip on a ${} meal would be about {}%, so the tip would be ${} and the total would be ${}".format(bill,int(tip_percent*100),tip,round(tip+bill,3)))
