from empolyeedetails import details
import json
from datetime import datetime
def save(Empname,Empage,Empposition,Empcode,Empexperince,Empqulation):
    data={
        "Employee name":Empname,
        "Employee age": Empage,
        "Empolyee Code":Empcode,
        "Empolyee  Qualification":Empqulation,
        "Empolyee Positon": Empposition,
        "Empolyee Exp.":Empexperince
    }
    emp_data=open("emp.json","w")
    mydata=json.dumps(data,emp_data,indent=5)