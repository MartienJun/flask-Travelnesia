from flask import Blueprint, render_template, request, redirect, url_for
from flask.helpers import flash
from flask_login import current_user, login_required
from app.Models.transportation import Transportation
from app.Controllers.transportation_controller import TransportationController


# Insialisasi Blueprint dengan url_prefix transportation
blueprint = Blueprint("transportation", __name__, url_prefix="/admin/transportation")


# Routing untuk ke halaman view
@blueprint.route('/')
@blueprint.route('/view')
@login_required
def view():
    # Jika session rolenya bukan admin, redirect kembali ke sign in
    if current_user.role != 'adm':
        flash("You must sign in as admin to use this feature")
        return redirect(url_for('auth.signin'))
    # Jika session admin ada, tampilkan halaman view
    return render_template("admin/transportation/view.html", list_transportation=TransportationController.get_all())


# Routing untuk halaman insert
@blueprint.route('/insert', methods=['GET', 'POST'])
@login_required
def insert():
    # Jika session rolenya bukan admin, redirect kembali ke sign in
    if current_user.role != 'adm':
        flash("You must sign in as admin to use this feature")
        return redirect(url_for('auth.signin'))
    # Jika metodenya adalah get, tampilkan halaman insert
    if request.method == 'GET':
        return render_template("admin/transportation/insert.html")

    # Jika metodenya adalah post, dapatkan data dari post
    transport_id = request.form['transport_id']
    transport = request.form['transport']
    type = request.form['type']

    # Cek apakah transport_id sudah ada dalam database
    if TransportationController.get_by_id(transport_id) is not None:
        # jika iya, tampilkan error message
        return render_template('admin/transportation/insert.html', message="transport_id sudah pernah terdaftar!")

    # Jika data sudah sesuai, masukan data tersebut ke dalam database melalui model
    transportation = Transportation(transport_id, transport, type)
    TransportationController.insert(transportation)

    # Redirect ke halaman view
    return redirect(url_for('transportation.view'))


# Routing untuk halaman update
@blueprint.route('/update/<id>', methods=['GET', 'POST'])
@login_required
def update(id):
    # Jika session rolenya bukan admin, redirect kembali ke sign in
    if current_user.role != 'adm':
        flash("You must sign in as admin to use this feature")
        return redirect(url_for('auth.signin'))
    # Jika metodenya adalah get, tampilkan halaman update
    if request.method == 'GET':
        return render_template("admin/transportation/update.html", transportation=TransportationController.get_by_id(id))

    # Jika metodenya adalah post, dapatkan data dari post
    transport_id = request.form['transport_id']
    transport = request.form['transport']
    type = request.form['type']

    # Update data tersebut ke dalam database melalui model
    transportation = Transportation(transport_id, transport, type)
    TransportationController.update(transportation)

    # Redirect kembali ke view
    return redirect(url_for('transportation.view'))


# Routing untuk halaman delete
@blueprint.route('/delete/<id>', methods=['GET', 'POST'])
@login_required
def delete(id):
   # Jika session rolenya bukan admin, redirect kembali ke sign in
    if current_user.role != 'adm':
        flash("You must sign in as admin to use this feature")
        return redirect(url_for('auth.signin'))
    # Hapus data tersebut dari database
    TransportationController.delete(id)

    # Redirect kembali ke View
    return redirect(url_for('transportation.view'))
