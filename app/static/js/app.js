document.addEventListener('DOMContentLoaded', () => {
    const taskForm = document.getElementById('task-form');
    const taskTitleInput = document.getElementById('task-title');
    const tasksList = document.getElementById('tasks');

    // Fetch and render all tasks
    async function fetchTasks() {
        const response = await fetch('/api/tasks');
        if (!response.ok) {
            console.error('Failed to fetch tasks');
            return;
        }
        const tasks = await response.json();
        tasksList.innerHTML = '';
        tasks.forEach(addTaskToDOM);
    }

    // Render a single task
    function addTaskToDOM(task) {
        const li = document.createElement('li');
        li.className = 'task' + (task.done ? ' done' : '');
        li.dataset.id = task.id;

        const title = document.createElement('span');
        title.className = 'title';
        title.textContent = task.title;

        const actions = document.createElement('div');

        const toggleBtn = document.createElement('button');
        toggleBtn.textContent = task.done ? 'Undo' : 'Done';
        toggleBtn.className = 'toggle';
        toggleBtn.addEventListener('click', () => toggleTask(task.id, !task.done));

        const deleteBtn = document.createElement('button');
        deleteBtn.textContent = 'Delete';
        deleteBtn.className = 'delete';
        deleteBtn.addEventListener('click', () => deleteTask(task.id));

        actions.appendChild(toggleBtn);
        actions.appendChild(deleteBtn);

        li.appendChild(title);
        li.appendChild(actions);
        tasksList.appendChild(li);
    }

    // Add a new task
    taskForm.addEventListener('submit', async e => {
        e.preventDefault();
        const title = taskTitleInput.value.trim();
        if (!title) return;
        const response = await fetch('/api/tasks', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title })
        });
        if (response.ok) {
            taskTitleInput.value = '';
            fetchTasks();
        }
    });

    // Toggle task done/undone
    async function toggleTask(id, done) {
        const response = await fetch(`/api/tasks/${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ done })
        });
        if (response.ok) fetchTasks();
    }

    // Delete a task
    async function deleteTask(id) {
        const response = await fetch(`/api/tasks/${id}`, { method: 'DELETE' });
        if (response.ok) fetchTasks();
    }

    // Initial load
    fetchTasks();
});
