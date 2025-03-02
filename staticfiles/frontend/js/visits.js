function loadVisits() {
    fetch('/api/visits/')
        .then(response => response.json())
        .then(visits => {
            const visitsList = document.getElementById('visits-list');
            visitsList.innerHTML = '';

            visits.forEach(visit => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${visit.id}</td>
                    <td>${visit.client.first_name} ${visit.client.last_name}</td>
                    <td>${visit.employee.first_name} ${visit.employee.last_name}</td>
                    <td>${visit.planned_start_time}</td>
                    <td>${visit.planned_end_time}</td>
                     <td>
                        <a href="add_visit.html?id=${visit.id}" class="btn btn-warning btn-sm">Edit</a>
                        <button class="btn btn-danger btn-sm" onclick="deleteVisit(${visit.id})">Delete</button>
                    </td>

                `;
                visitsList.appendChild(row);
            });
        });
}
function deleteVisit(visitId) {
    if (confirm('Are you sure?')) {
        fetch(`/api/visits/${visitId}/`, { method: 'DELETE' })
            .then(response => {
                if (response.ok) {
                    loadVisits(); // Reload the list
                } else {
                    alert('Error deleting visit.');
                }
            });
    }
}


loadVisits();