from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      title TEXT NOT NULL,
                      description TEXT,
                      status TEXT NOT NULL)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        status = request.form['status']
        conn = sqlite3.connect('tasks.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (title, description, status) VALUES (?, ?, ?)",
                       (title, description, status))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_task.html')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/update/<int:task_id>', methods=['GET', 'POST'])
def update_task(task_id):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        status = request.form['status']
        cursor.execute("UPDATE tasks SET title=?, description=?, status=? WHERE id=?",
                       (title, description, status, task_id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    cursor.execute("SELECT * FROM tasks WHERE id=?", (task_id,))
    task = cursor.fetchone()
    conn.close()
    return render_template('add_task.html', task=task)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
