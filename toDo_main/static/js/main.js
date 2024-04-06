function validateForm() {
    var taskInput = document.getElementById('taskInput').value;
    if (taskInput.trim() === '') {
        alert('Please enter a task.');
        return false;
    }
    return true;
}