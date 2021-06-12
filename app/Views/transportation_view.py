from flask import Blueprint, render_template, request, redirect, url_for, session
from app.Controllers.transportation_controller import TransportationController
from app.Models.transportation import Transportation


# Insialisasi Blueprint dengan url_prefix transportation
blueprint = Blueprint("transportation", __name__, url_prefix="/admin/transportation")


# Routing untuk ke halaman view
@blueprint.route('/')
@blueprint.route('/view')
def view():
    # Jika session admin tidak ada, redirect kembali ke home
    if session.get('admin') is None:
        return redirect(url_for('home'))
    # Jika session admin ada, tampilkan halaman view
    return render_template("admin/transportation/view.html", list_transportation=TransportationController.get_all())


# Routing untuk halaman insert
@blueprint.route('/insert', methods=['GET', 'POST'])
def insert():
    # Jika session admin tidak ada, redirect kembali ke home
    if session.get('admin') is None:
        return redirect(url_for('home'))
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
def update(id):
    # Jika session admin tidak ada, redirect kembali ke home
    if session.get('admin') is None:
        return redirect(url_for('home'))
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
def delete(id):
    # Jika session admin tidak ada, redirect kembali ke home
    if session.get('admin') is None:
        return redirect(url_for('home'))

    # Hapus data tersebut dari database
    TransportationController.delete(id)

    # Redirect kembali ke View
    return redirect(url_for('transportation.view'))
