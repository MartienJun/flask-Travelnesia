from flask import Blueprint, render_template, request, redirect, url_for, session
from app.Controllers.role_controller import RoleController
from app.Models.role import Role


# Insialisasi Blueprint dengan url_prefix role
blueprint = Blueprint("role", __name__, url_prefix="/admin/role")


# Routing untuk ke halaman view
@blueprint.route('/')
@blueprint.route('/view')
def view():
    # Jika session admin tidak ada, redirect kembali ke home
    if session.get('admin') is None:
        return redirect(url_for('home'))
    # Jika session admin ada, tampilkan halaman view
    return render_template("Views/role/view.html", list_role=RoleController.get_all())


# Routing untuk halaman insert
@blueprint.route('/insert', methods=['GET', 'POST'])
def insert():
    # Jika session admin tidak ada, redirect kembali ke home
    if session.get('admin') is None:
        return redirect(url_for('home'))
    # Jika metodenya adalah get, tampilkan halaman insert
    if request.method == 'GET':
        return render_template("Views/role/insert.html")

    # Jika metodenya adalah post, dapatkan data dari post
    role_id = request.form['role_id']
    role_name = request.form['role_name']

    # Cek apakah role_id sudah ada dalam database
    if RoleController.get_by_id(role_id) is not None:
        # jika iya, tampilkan error message
        return render_template('Views/role/insert.html', message="role_id sudah pernah terdaftar!")

    # Jika data sudah sesuai, masukan data tersebut ke dalam database melalui model
    role = Role(role_id, role_name)
    RoleController.insert(role)

    # Redirect ke halaman view
    return redirect(url_for('role.view'))


# Routing untuk halaman update
@blueprint.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    # Jika session admin tidak ada, redirect kembali ke home
    if session.get('admin') is None:
        return redirect(url_for('home'))
    # Jika metodenya adalah get, tampilkan halaman update
    if request.method == 'GET':
        return render_template("Views/role/update.html", role=RoleController.get_by_id(id))

    # Jika metodenya adalah post, dapatkan data dari post
    role_id = request.form['role_id']
    role_name = request.form['role_name']

    # Update data tersebut ke dalam database melalui model
    role = Role(role_id, role_name)
    RoleController.update(role)

    # Redirect kembali ke view
    return redirect(url_for('role.view'))


# Routing untuk halaman delete
@blueprint.route('/delete/<id>', methods=['POST'])
def delete(id):
    # Jika session admin tidak ada, redirect kembali ke home
    if session.get('admin') is None:
        return redirect(url_for('home'))

    # Hapus data tersebut dari database
    RoleController.delete(id)

    # Redirect kembali ke View
    return redirect(url_for('role.view'))
