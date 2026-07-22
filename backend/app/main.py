from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routes import employee
from app.routes import upload

app = FastAPI(
    title="Employee Management API",
    version="1.0.0"
)


# Create database tables when the application starts
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace * with frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Root Endpoint
@app.get("/")
def root():
    return {
        "message": "Employee Management API"
    }


# Health Check Endpoint
@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


# Employee CRUD Routes
app.include_router(
    employee.router,
    prefix="/employees",
    tags=["Employees"]
)


# AWS S3 Upload Routes
app.include_router(
    upload.router,
    prefix="/s3",
    tags=["S3 Upload"]
)
