const form = document.getElementById('client-form');
const clientId = new URLSearchParams(window.location.search).get('id');

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
const csrftoken = getCookie('csrftoken');

function loadClientData(id) {
    fetch(`/api/clients/${id}/`)
        .then(response => response.json())
        .then(client => {
            document.getElementById('client-id').value = client.id;
            document.getElementById('first_name').value = client.first_name;
            document.getElementById('last_name').value = client.last_name;
            document.getElementById('address').value = client.address;
            document.getElementById('phone').value = client.phone;
            document.getElementById('contact_person_first_name').value = client.contact_person_first_name;
            document.getElementById('contact_person_last_name').value = client.contact_person_last_name;
            document.getElementById('contact_person_phone').value = client.contact_person_phone;
            document.getElementById('contact_person_email').value = client.contact_person_email;
            document.getElementById('notes').value = client.notes;

        });
}

if (clientId) {
    loadClientData(clientId);  // Load client data if editing
}

form.addEventListener('submit', function(event) {
    event.preventDefault();

    const clientData = {
        id: document.getElementById('client-id').value,
        first_name: document.getElementById('first_name').value,
        last_name: document.getElementById('last_name').value,
        address: document.getElementById('address').value,
        phone: document.getElementById('phone').value,
        contact_person_first_name: document.getElementById('contact_person_first_name').value,
        contact_person_last_name: document.getElementById('contact_person_last_name').value,
        contact_person_phone: document.getElementById('contact_person_phone').value,
        contact_person_email: document.getElementById('contact_person_email').value,
        notes: document.getElementById('notes').value,
        service_type: "Basic Visit"
    };

    const method = clientId ? 'PUT' : 'POST';  // Use PUT for update, POST for create
    const url = clientId ? `/api/clients/${clientId}/` : '/api/clients/';

    fetch(url, {
        method: method,
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken  // Add CSRF token
        },
        body: JSON.stringify(clientData),
    })
    .then(response => {
        if (response.ok) {
            window.location.href = '/clients/'; // Redirect to clients list
        } else {
           return response.json().then(data => {  // Parse the response body
                throw new Error(JSON.stringify(data));  // Throw an error with the response data
           });
        }
    })
    .catch((error) => {
        console.error('Error:', error);
        document.getElementById('error-message').textContent = 'Error: viz konzole ' + error;
    });
});