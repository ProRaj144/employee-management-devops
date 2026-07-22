from sqlalchemy.orm import Session
from app.models import Employee
from app.schemas import EmployeeCreate


def get_employees(db: Session):
    return db.query(Employee).all()


def get_employee(db: Session, employee_id: int):
    return db.query(Employee).filter(Employee.id == employee_id).first()


def create_employee(db: Session, employee: EmployeeCreate):
    db_employee = Employee(**employee.model_dump())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def update_employee(db: Session, employee_id: int, employee: EmployeeCreate):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()

    if not db_employee:
        return None

    db_employee.first_name = employee.first_name
    db_employee.last_name = employee.last_name
    db_employee.email = employee.email
    db_employee.department = employee.department
    db_employee.designation = employee.designation
    db_employee.salary = employee.salary

    db.commit()
    db.refresh(db_employee)

    return db_employee


def delete_employee(db: Session, employee_id: int):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()

    if employee:
        db.delete(employee)
        db.commit()

    return employee
