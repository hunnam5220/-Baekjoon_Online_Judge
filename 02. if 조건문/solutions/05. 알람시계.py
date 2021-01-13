import sys, datetime
ipt = sys.stdin.readline
h, m = ipt().split()

time = datetime.datetime.strptime("{}-{}".format(h, m), "%H-%M")
time = time-datetime.timedelta(minutes=45)
h = int(datetime.datetime.strftime(time, "%#H"))
m = int(datetime.datetime.strftime(time, "%M"))

print(h, m)