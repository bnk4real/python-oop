# class TbTJuristic():
#     def __init__(self, id, status, currentActivity, cid, createDate, updateData, currentStatus, currentActivityStatusCode):
#         self.id = id
#         self.status = status
#         self.currentActivity = currentActivity
#         self.cid = cid
#         self.createDate = createDate
#         self.updateDate = updateData
#         self.currentStatus = currentStatus
#         self.currentActivityStatusCode = currentActivityStatusCode
#     def __str__(self):
#         return f"{self.id}, {self.status}, {self.currentActivity}, {self.cid}, {self.createDate}, {self.currentStatus}"

# consider query or get data from somewhere else

# Improve Way :
from dataclasses import dataclass
from datetime import datetime


# The @dataclass decorator automatically generates the __init__, __repr__, and other methods, reducing boilerplate code.
@dataclass
class TbTJuristic:
    id: int
    status: str
    current_activity: str
    cid: int
    create_date: datetime
    update_date: datetime
    current_status: str
    current_activity_status_code: str
    
    def __str__(self):
        return f"ID: {self.id}, Status: {self.status}, Current Activity: {self.current_activity}, Cid: {self.cid}, Create Date: {self.create_date}, Current Status: {self.current_status}"

data = TbTJuristic(1, 'OPEN', 'form_submit', '111002', datetime.now(), datetime.now(), 'SC', '0000')

dataList = [data]