function loadClients() {
    fetch('/api/clients/')
        .then(response => response.json())
        .then(clients => {
            const clientsList = document.getElementById('clients-list');
            clientsList.innerHTML = ''; // Clear the list

            clients.forEach(client => {
                const row = document.createElement('tr');
                // Dynamically create the edit URL:
                const editUrl = `/add_client/?id=${client.id}`; // Construct the URL in JavaScript

                row.innerHTML = `
                    <td>${client.id}</td>
                    <td>${client.first_name}</td>
                    <td>${client.last_name}</td>
                    <td>${client.address}</td>
                    <td>${client.phone}</td>
                    <td>
                        <a href="${editUrl}" class="btn btn-warning btn-sm">Edit</a>
                        <button class="btn btn-danger btn-sm" onclick="deleteClient(${client.id})">Delete</button>
                    </td>
                `;
                clientsList.appendChild(row);
            });
        });
}

// ... (zbytek souboru) ...

function deleteClient(clientId) {
    if (confirm('Are you sure?')) {
        fetch(`/api/clients/${clientId}/`, { method: 'DELETE' })
            .then(response => {
                if (response.ok) {
                    loadClients(); // Reload the list
                } else {
                    alert('Error deleting client.');
                }
            });
    }
}


loadClients(); // Load clients when the page loads