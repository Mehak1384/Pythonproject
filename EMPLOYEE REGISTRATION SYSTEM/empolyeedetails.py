def details():
    Empcode=int(input("Enter your Employee code"))
    Empname=input("Enter the Employee name :")
    Empage=input("Enter your age in form Date.Month.Year")
    Empqulation=input("Enter your Education Level")
    Empexperince=float(input("Enter your Exp. in terms of years"))
    Empposition=input("Enter you position in Company")
    return Empname,Empage,Empposition,Empcode,Empexperince,Empqulation
details()