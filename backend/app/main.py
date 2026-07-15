from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app.schemas import EmployeeCreate, EmployeeResponse
from app import crud

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Employee Management API",
    version="1.0"
)

@app.get("/")
def home():
    return {"message":"Employee Management API"}

@app.get("/health")
def health():
    return {"status":"healthy"}

@app.get("/employees", response_model=list[EmployeeResponse])
def list_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)

@app.get("/employees/{employee_id}", response_model=EmployeeResponse)
def get_employee(employee_id:int, db: Session = Depends(get_db)):
    employee = crud.get_employee(db, employee_id)

    if employee is None:
        raise HTTPException(status_code=404, detail="Employee Not Found")

    return employee

@app.post("/employees", response_model=EmployeeResponse)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, employee)

@app.put("/employees/{employee_id}", response_model=EmployeeResponse)
def update_employee(employee_id:int, employee:EmployeeCreate, db:Session=Depends(get_db)):

    updated = crud.update_employee(db, employee_id, employee)

    if updated is None:
        raise HTTPException(status_code=404, detail="Employee Not Found")

    return updated

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id:int, db:Session=Depends(get_db)):

    deleted = crud.delete_employee(db, employee_id)

    if deleted is None:
        raise HTTPException(status_code=404, detail="Employee Not Found")

    return {"message":"Employee Deleted Successfully"}
