import { useEffect, useState } from "react";
import "./App.css";

import api from "./api";

import EmployeeForm from "./components/EmployeeForm";
import EmployeeTable from "./components/EmployeeTable";

import FileUpload from "./components/FileUpload";
import FileList from "./components/FileList";

function App() {

  const [employees, setEmployees] = useState([]);
  const [files, setFiles] = useState([]);

  // ===========================
  // Employee Functions
  // ===========================

  const loadEmployees = async () => {
    try {
      const response = await api.get("/employees/");
      setEmployees(response.data);
    } catch (error) {
      console.error(error);
      alert("Unable to fetch employees.");
    }
  };

  const addEmployee = async (employee) => {
    try {
      await api.post("/employees/", employee);
      loadEmployees();
    } catch (error) {
      console.error(error);
      alert("Unable to add employee.");
    }
  };

  // ===========================
  // S3 File Functions
  // ===========================

  const loadFiles = async () => {
    try {
      const response = await api.get("/s3/files");
      setFiles(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  useEffect(() => {
    loadEmployees();
    loadFiles();
  }, []);

  return (
    <div className="App">

      <header className="header">
        <h1>Employee Management System</h1>
        <p>Production Environment with AWS S3 Integration</p>
      </header>

      <div className="container">

        {/* Employee Section */}

        <EmployeeForm addEmployee={addEmployee} />

        <EmployeeTable employees={employees} />

        {/* S3 Upload Section */}

        <FileUpload refreshFiles={loadFiles} />

        <FileList
          files={files}
          refreshFiles={loadFiles}
        />

      </div>

    </div>
  );
}

export default App;
