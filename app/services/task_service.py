
from app.database import get_connection


# Create a new task
def create_task(task_data):
    connection = get_connection()

    cursor = connection.execute(
        """
        INSERT INTO tasks (title, description, priority, status)
        VALUES (?, ?, ?, ?)
        """,
        (
            task_data.title,
            task_data.description,
            task_data.priority,
            task_data.status
        )
    )

    connection.commit()

    task_id = cursor.lastrowid

    connection.close()

    return get_task_by_id(task_id)


# Get all tasks
def get_all_tasks(status=None, priority=None):
    connection = get_connection()

    query = "SELECT * FROM tasks WHERE 1=1"
    values = []

    if status:
        query += " AND status = ?"
        values.append(status)

    if priority:
        query += " AND priority = ?"
        values.append(priority)

    cursor = connection.execute(query, values)

    tasks = [dict(row) for row in cursor.fetchall()]

    connection.close()

    return tasks


# Get one task by ID
def get_task_by_id(task_id):
    connection = get_connection()

    cursor = connection.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    )

    task = cursor.fetchone()

    connection.close()

    return dict(task) if task else None


# Update a task
def update_task(task_id, task_data):
    connection = get_connection()

    connection.execute(
        """
        UPDATE tasks
        SET title = ?, description = ?, priority = ?, status = ?
        WHERE id = ?
        """,
        (
            task_data.title,
            task_data.description,
            task_data.priority,
            task_data.status,
            task_id
        )
    )

    connection.commit()
    connection.close()

    return get_task_by_id(task_id)


# Update only task status
def update_task_status(task_id, status):
    connection = get_connection()

    connection.execute(
        "UPDATE tasks SET status = ? WHERE id = ?",
        (status, task_id)
    )

    connection.commit()
    connection.close()

    return get_task_by_id(task_id)


# Delete a task
def delete_task(task_id):
    connection = get_connection()

    cursor = connection.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    connection.commit()

    deleted = cursor.rowcount > 0

    connection.close()

    return deleted
