def is_leap(yr):
     if (yr%4==0):
         return "True"
     else:
         return "False"

year = int(input())
print(is_leap(year))