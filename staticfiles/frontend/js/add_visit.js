const form = document.getElementById('visit-form');
const clientIdSelect = document.getElementById('client');
const employeeIdSelect = document.getElementById('employee');
const visitId = new URLSearchParams(window.location.search).get('id');

// --- Přidej funkci getCookie ---
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
// --- Konec funkce getCookie ---


function loadClients() {
    fetch('/api/clients/')
        .then(response => response.json())
        .then(clients => {
            clients.forEach(client => {
                const option = document.createElement('option');
                option.value = client.id;
                option.textContent = `${client.first_name} ${client.last_name}`;
                clientIdSelect.appendChild(option);
            });
        });
}

function loadEmployees() {
    fetch('/api/employees/')
        .then(response => response.json())
        .then(employees => {
            employees.forEach(employee => {
                const option = document.createElement('option');
                option.value = employee.id;
                option.textContent = `${employee.first_name} ${employee.last_name}`;
                employeeIdSelect.appendChild(option);
            });
        });
}
function loadVisitData(id){
     fetch(`/api/visits/${id}/`)
        .then(response => response.json())
        .then(visit => {
            document.getElementById('visit-id').value = visit.id;
            document.getElementById('planned_start_time').value = visit.planned_start_time.replace("Z", "");
            document.getElementById('planned_end_time').value = visit.planned_end_time.replace("Z", "");
            //set select boxes
            clientIdSelect.value = visit.client.id;
            employeeIdSelect.value = visit.employee.id;
        });
}
if (visitId) {
    loadVisitData(visitId);  // Load visit data if editing
}
loadClients();
loadEmployees();

form.addEventListener('submit', function(event) {
    event.preventDefault();

      // Get CSRF token
    const csrftoken = getCookie('csrftoken'); // Použijeme funkci getCookie

    const visitData = {
        id: document.getElementById('visit-id').value,
        client_id: clientIdSelect.value,
        employee_id: employeeIdSelect.value,
        planned_start_time: document.getElementById('planned_start_time').value,
        planned_end_time: document.getElementById('planned_end_time').value,

    };

    const method = visitId ? 'PUT' : 'POST';
    const url = visitId ? `/api/visits/${visitId}/` : '/api/visits/';

    fetch(url, {
        method: method,
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken  // Add CSRF token
        },
        body: JSON.stringify(visitData),
    })
  .then(response => {
        if (response.ok) {
            window.location.href = '/visits/'; // Redirect to visits list
        } else {
           return response.json().then(data => {
                throw new Error(JSON.stringify(data));
           });
        }
    })
    .catch((error) => {
        console.error('Error:', error);
         document.getElementById('error-message').textContent = 'Error: viz konzole ' + error;
    });
});