from pydantic import BaseModel, EmailStr
from typing import Optional


class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    department: Optional[str] = None
    designation: Optional[str] = None
    salary: Optional[int] = None


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeResponse(EmployeeBase):
    id: int

    class Config:
        from_attributes = True
