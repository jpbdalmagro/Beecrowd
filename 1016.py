seg = int(input())

mins = seg // 60
seg = seg % 60
hours = mins // 60
mins = mins % 60

print("{}:{}:{}".format(hours, mins, seg))
