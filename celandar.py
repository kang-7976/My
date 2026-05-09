from datetime import datetime as dt

print('一 二 三 四 五 六 日')

# 获取当前时间
d = dt.now()

# 显示日期
print(f'今天是 {d.year}年 {d.month}月 {d.day}日')
print("今天是星期" + ["一", "二", "三", "四", "五", "六", "日"][d.weekday()])
print(f'现在是 {d.hour}:{d.minute}')

# 特定节日的打印
if d.month == 1 and d.day == 1:
    print('元旦快乐')
elif d.month == 4 and d.day == 4:
    print('清明节快乐放3天')
elif d.month == 5 and d.day == 1:
    print('劳动节！')
elif d.month == 6 and 10 <= d.day <= 20:
    print("这几天是端午节前后~")
elif d.month == 10 and d.day == 1:
    print('现在是国庆节.')
elif d.month == 4 and d.day == 23:
    print('今天是我生日')

# 定义hour
hour = d.hour

# 把一天分成早上 中午 下午 晚上
if 5 <= hour <= 7:
    print('早上好，新的一天又开始')
elif 7 <= hour <= 12:
    print('中午好，每天都要快快乐乐吃饭哦')
elif 12 <= hour <= 18:
    print('现在是下午时间')
elif 18 <= hour <= 22:
    print('现在是晚上时间，现在睡觉正合适哦')
elif hour >= 22:
    print('现在已经即将踏入凌晨')
elif hour < 5:
    print('都凌晨了还不睡？')

