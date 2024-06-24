document.addEventListener('DOMContentLoaded', () => {
    const orderForm = document.getElementById('order-form');
    const ordersTableBody = document.getElementById('orders-table').getElementsByTagName('tbody')[0];

    orderForm.addEventListener('submit', (event) => {
        event.preventDefault();
        const formData = new FormData(orderForm);
        const item = formData.get('item');
        const quantity = formData.get('quantity');

        fetch('/add_order', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ item, quantity, price: quantity * 10 }), // Assume each item costs $10 for simplicity
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                fetchOrders();
            }
        })
        .catch(error => console.error('Error:', error));
    });

    function fetchOrders() {
        fetch('/get_orders')
            .then(response => response.json())
            .then(orders => {
                ordersTableBody.innerHTML = '';
                orders.forEach(order => {
                    const row = ordersTableBody.insertRow();
                    row.insertCell(0).textContent = order.item_name;
                    row.insertCell(1).textContent = order.quantity;
                    row.insertCell(2).textContent = order.price;
                    const deleteCell = row.insertCell(3);
                    const deleteButton = document.createElement('button');
                    deleteButton.textContent = 'Delete';
                    deleteButton.onclick = () => deleteOrder(order.item_name);
                    deleteCell.appendChild(deleteButton);
                });
            });
    }

    function deleteOrder(item_name) {
        fetch('/delete_order', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ item_name }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                fetchOrders();
            }
        })
        .catch(error => console.error('Error:', error));
    }

    fetchOrders();
});
