from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

todo_list = []

@app.route('/')
def index():
    return render_template('index.html', tasks=todo_list)

@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form['task']
    todo_list.append({'task': task, 'completed': False})
    return jsonify({'message': f'Task "{task}" added to the to-do list.'})

@app.route('/mark_completed/<int:task_index>')
def mark_completed(task_index):
    if 0 <= task_index < len(todo_list):
        todo_list[task_index]['completed'] = True
        return jsonify({'message': f'Task "{todo_list[task_index]["task"]}" marked as completed.'})
    else:
        return jsonify({'error': 'Invalid task index.'}), 400

@app.route('/remove_task/<int:task_index>')
def remove_task(task_index):
    if 0 <= task_index < len(todo_list):
        removed_task = todo_list.pop(task_index)
        return jsonify({'message': f'Task "{removed_task["task"]}" removed from the to-do list.'})
    else:
        return jsonify({'error': 'Invalid task index.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
