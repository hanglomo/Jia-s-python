
    #人的年龄
    age=int(input("人的年龄是多少"))
    if age>120 or age<0:
            print("年龄不符合标准")
    else:
            print("合法年龄")


    #考试成绩
    a=int(input("数学考试成绩"))
    b=int(input("语文考试成绩"))
    if a>=60 or b>=60:
        print("考试及格")
    else:
        print("考试不及格")
        
    #奖励分类
    a=int(input("你考了多少分"))
    if a>=100:
        print("奖励书一个")
    elif 80<a<100:
        print("奖励本一个")
    elif 60<a<80:
        print("奖励笔一根")
    else:
        print("无奖励")
