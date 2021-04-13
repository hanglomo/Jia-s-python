    #网吧智能判断系统
    age=int(input("年龄"))
    if age>=18:
    print("可以进网吧")
    else:
    print("不可以进")
    #成绩判断
    a=int(input("成绩"))
    b=int(input("成绩"))
    if a==100 and b==100:
    print("去迪士尼")   
    else: 
    print("在家里写作业")

    #成绩判断
    a=int(input("成绩"))
    b=int(input("成绩"))
    if a==100 or b==100:
    print("去迪士尼")   
    else: 
    print("在家里写作业")
    #是否为合法年龄
    a=int(input("年龄"))
    if a>=0 and a<=120:
    print("合法")
    else: 
    print("不合法") 
    #成绩是否合格
    a=int(input("成绩"))
    b=int(input("成绩"))
    if a>60 or b>60:
    print("考试合格")  
    else:
    print("考试不合格")
    #使用布尔类型判断是否为我们班的人
    student=True
    if not student:
    print("不是我们班级的")   
    else:
    print("是我们班级的")
