function EmployeeTable({ employees }) {
  return (
    <div className="card">

      <h3>Employee Directory</h3>

      <table>

        <thead>
          <tr>
            <th>ID</th>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Email</th>
            <th>Department</th>
            <th>Designation</th>
            <th>Salary (₹)</th>
          </tr>
        </thead>

        <tbody>

          {employees.length === 0 ? (

            <tr>
              <td colSpan="7" style={{ textAlign: "center" }}>
                No Employees Found
              </td>
            </tr>

          ) : (

            employees.map((emp) => (

              <tr key={emp.id}>
                <td>{emp.id}</td>
                <td>{emp.first_name}</td>
                <td>{emp.last_name}</td>
                <td>{emp.email}</td>
                <td>{emp.department}</td>
                <td>{emp.designation}</td>
                <td>₹ {emp.salary}</td>
              </tr>

            ))

          )}

        </tbody>

      </table>

    </div>
  );
}

export default EmployeeTable;
