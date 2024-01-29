function addTask() {
    var taskInput = document.getElementById('taskInput');
    var task = taskInput.value.trim();

    if (task !== '') {
        fetch('/add_task', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `task=${task}`,
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            taskInput.value = '';
            location.reload();
        })
        .catch(error => console.error('Error:', error));
    }
}

function markCompleted(taskIndex) {
    fetch(`/mark_completed/${taskIndex}`)
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            location.reload();
        })
        .catch(error => console.error('Error:', error));
}

function removeTask(taskIndex) {
    fetch(`/remove_task/${taskIndex}`)
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            location.reload();
        })
        .catch(error => console.error('Error:', error));
}
