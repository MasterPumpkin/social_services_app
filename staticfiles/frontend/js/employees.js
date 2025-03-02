function loadEmployees() {
    fetch('/api/employees/')
        .then(response => response.json())
        .then(employees => {
            const employeesList = document.getElementById('employees-list');
            employeesList.innerHTML = ''; // Clear

            employees.forEach(employee => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${employee.id}</td>
                    <td>${employee.first_name}</td>
                    <td>${employee.last_name}</td>
                    <td>${employee.phone}</td>
                    <td>
                        <a href="add_employee.html?id=${employee.id}" class="btn btn-warning btn-sm">Edit</a>
                        <button class="btn btn-danger btn-sm" onclick="deleteEmployee(${employee.id})">Delete</button>
                    </td>
                `;
                employeesList.appendChild(row);
            });
        });
}

function deleteEmployee(employeeId) {
    if (confirm('Are you sure?')) {
        fetch(`/api/employees/${employeeId}/`, { method: 'DELETE' })
            .then(response => {
                if (response.ok) {
                    loadEmployees();
                } else {
                    alert('Error deleting employee.');
                }
            });
    }
}


loadEmployees();