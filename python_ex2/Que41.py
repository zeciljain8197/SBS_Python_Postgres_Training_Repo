class Student:
    Name = False
    Reg_No = False
    Roll_No = False
    Standard = False
    Admission_Year = False
    Marks = []
    Result = False

    def __init__(self, name, reg_no, roll_no, std, admin_yr):
        if name.isalpha():
            self.Name = name
        if reg_no.isalnum():
            self.Reg_No = reg_no
        if roll_no.isdigit() and std.isdigit() and admin_yr.isdigit():
            self.Roll_No = roll_no
            self.Standard = std
            self.Admission_Year = admin_yr

    def res_history(self, **kwargs):
        pass_lst = []
        fail_lst = []
        for kwarg in kwargs:
            if kwargs[kwarg] < 100:
                self.Marks.append(kwargs)
                if kwargs[kwarg] < 40:
                    fail_lst.append(kwargs.items())
                else:
                    pass_lst.append(kwargs.items())

    def print_result(self):
        res = """
        *******************************************************************
        Name : {Name}
        Roll No : {Roll_No}                             Standard: {Standard}
        *******************************************************************
        Subject    Total Marks    Passing Marks    Obtained Marks    Result
        {Sub_1}        100             40           {sub_1_marks}    {res_1}
        {Sub_2}        100             40           {sub_2_marks}    {res_2}
        {Sub_3}        100             40           {sub_3_marks}    {res_3}
        *******************************************************************
        TOTAL          300            160              {total}
        Result: {res}                     Percentage: {percentage}
        """
        res.format()
