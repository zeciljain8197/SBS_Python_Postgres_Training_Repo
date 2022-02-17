class Student:
    Name = False
    Reg_no = False
    Roll_no = False
    Standard = False
    Admission_Yr = False
    Marks = []
    Result = False

    def __init__(self, name, reg_no, roll_no, std, admin_yr):
        try:
            if name.isalpha():
                self.Name = name
            if reg_no.alnum():
                self.Reg_no = reg_no
            if roll_no.isdigit() and std.isdigit() and admin_yr.isdigit():
                self.Roll_no = roll_no
                self.Standard = std
                self.Admission_Yr = admin_yr