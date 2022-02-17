def res_history(**kwargs):
    marks = []
    pass_lst = []
    fail_lst = []
    for kwarg in kwargs:
        if kwargs[kwarg] < 100:
            marks.append(kwargs)
            if kwargs[kwarg] < 40:
                fail_lst.append(kwargs.items())
            else:
                pass_lst.append(kwargs.items())
    print(fail_lst)
    print(pass_lst)
    print(marks)


res_history(a=172, b=21, c=56)
res_history(d=102, e=52, f=68)