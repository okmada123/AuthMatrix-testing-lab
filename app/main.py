from fastapi import FastAPI, HTTPException, Request
from typing import List

app = FastAPI()

# Define user roles
ROLES = {
    "admin": ["admin", "manager", "employee", "guest"],
    "manager": ["manager", "employee", "guest"],
    "employee": ["employee", "guest"],
    "guest": ["guest"],
}

USERS_ROLES = {
    "user1": "admin",
    "user2": "manager",
    "user3": "employee",
    "user4": "guest",
}

def authenticate_user(request: Request):
    x_role = request.headers.get("X-Role")
    # You would replace this with actual authentication logic
    if not x_role:
        raise HTTPException(status_code=401, detail="Unauthorized")
    if x_role not in USERS_ROLES:
        raise HTTPException(status_code=401, detail="Invalid role")
    return USERS_ROLES[x_role]


def authorize_user(request: Request, required_role: str):
    current_role = authenticate_user(request)
    #print(f"Required role: {required_role};\tCurrent user role: {current_role} (has all these roles: {ROLES[current_role]})")
    if required_role:
        if required_role not in ROLES[current_role]:
            raise HTTPException(status_code=403, detail="Forbidden")
    return current_role

@app.get("/admin_data")
def get_admin_data(request: Request):
    authorize_user(request, "admin")
    return {"message": "Admin data accessed successfully"}

@app.get("/manager_data")
def get_manager_data(request: Request):
    authorize_user(request, "manager")
    return {"message": "Manager data accessed successfully"}

@app.get("/employee_data")
def get_employee_data(request: Request):
    authorize_user(request, "employee")
    return {"message": "Employee data accessed successfully"}

@app.get("/guest_data")
def get_guest_data(request: Request):
    authorize_user(request, "guest")
    return {"message": "Guest data accessed successfully"}
    
@app.get("/public_data")
def get_public_data(request: Request):
    #authorize_user(request, "manager")
    return {"message": "Public data accessed successfully"}

@app.get("/s3cr3t_4_u4")
def get_public_data(request: Request):
    if request.headers.get("X-Role") != "user4":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"message": "Secret data accessed successfully"}