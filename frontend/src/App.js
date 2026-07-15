import { useEffect, useState } from "react";
import "./App.css";

import api from "./api";
import EmployeeForm from "./components/EmployeeForm";
import EmployeeTable from "./components/EmployeeTable";

function App() {

  const [employees, setEmployees] = useState([]);

  // Load Employees
  const loadEmployees = async () => {
    try {
      const response = await api.get("/employees");
      setEmployees(response.data);
    } catch (error) {
      console.log(error);
      alert("Unable to fetch employees.");
    }
  };

  useEffect(() => {
    loadEmployees();
  }, []);

  // Add Employee
  const addEmployee = async (employee) => {
    try {
      await api.post("/employees", employee);
      loadEmployees();
    } catch (error) {
      console.log(error);
      alert("Unable to add employee.");
    }
  };

  return (
    <div className="App">

      <header className="header">
        <h1>Employee Management System</h1>
        <p>Production Environment Demo</p>
      </header>

      <div className="container">

        <EmployeeForm addEmployee={addEmployee} />

        <EmployeeTable employees={employees} />

      </div>

    </div>
  );
}

export default App;
