from flask import Blueprint, request, jsonify, abort
from app import db
from app.models import Task

bp = Blueprint('api', __name__)

@bp.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@bp.errorhandler(400)
def bad_request(error):
    message = error.description if hasattr(error, 'description') else 'Bad request'
    return jsonify({'error': message}), 400

@bp.route('/tasks', methods=['GET'])
def get_tasks():
    """Return a list of all tasks."""
    tasks = Task.query.order_by(Task.timestamp.desc()).all()
    return jsonify([task.to_dict() for task in tasks])

@bp.route('/tasks', methods=['POST'])
def create_task():
    """Create a new task."""
    data = request.get_json() or {}
    if 'title' not in data or not data['title'].strip():
        abort(400, description='Title is required')
    task = Task(title=data['title'].strip())
    db.session.add(task)
    db.session.commit()
    return jsonify(task.to_dict()), 201

@bp.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    """Update an existing task."""
    task = Task.query.get_or_404(id)
    data = request.get_json() or {}
    if 'title' in data and not data['title'].strip():
        abort(400, description='Title cannot be empty')
    task.from_dict(data)
    db.session.commit()
    return jsonify(task.to_dict())

@bp.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    """Delete a task."""
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted'})
