import controller.trabajadorController as control
from flask import Blueprint, jsonify, request

trabajador = Blueprint('trabajadores', __name__)


@trabajador.route('/trabajador', methods=['GET'])
def get_trabajadores():
    respuesta = control.get_all_trabajadores()
    return jsonify(respuesta)
# habra que hacer el error 401


@trabajador.route('/trabajador/<dni>', methods=['GET'])
def get_trabajadores_dni(dni):
    respuesta = control.get_trabajador_dni(dni)
    if respuesta:
        return jsonify(respuesta), 200
    else:
        return jsonify({"error": "Trabajador not found."}), 404
# habra que meter el error 401


@trabajador.route('/trabajador', methods=['POST'])
def post_trabajador():
    dni = request.form.to_dict()["dni"]
    name = request.form.to_dict()["name"]
    lastname = request.form.to_dict()["lastname"]
    telf = request.form.to_dict()["telf"]
    email = request.form.to_dict()["email"]
    rol = request.form.to_dict()["rol"]
    last_access = -1
    picture = "https://editor.swagger.io/"

    t = control.post_trabajador(dni, name, lastname, telf, email, rol, last_access, picture)
    return jsonify(t)


@trabajador.route('/trabajador/<dni>', methods=["PUT"])
def modify_trabajador(dni):
    name = None
    lastname = None
    telf = None
    email = None
    rol = None
    last_access = None
    picture = None

    if "name" in request.form.to_dict():
        name = request.form.to_dict()["name"]
    if "lastname" in request.form.to_dict():
        lastname = request.form.to_dict()["lastname"]
    if "telf" in request.form.to_dict():
        telf = request.form.to_dict()["telf"]
    if "email" in request.form.to_dict():
        email = request.form.to_dict()["email"]
    if "rol" in request.form.to_dict():
        rol = request.form.to_dict()["rol"]
    if "last_access" in request.form.to_dict():
        last_access = -1
    if "picture" in request.form.to_dict():
        picture = "https://editor.swagger.io/"
        print("INNNNNNN")
    if "dni" in request.form.to_dict():
        dni_change = request.form.to_dict()["dni"]

    respuesta = control.modify_trabajador(dni, dni_change, name, lastname, telf, email, rol, last_access, picture)

    if respuesta:
        return jsonify(respuesta), 200
    else:
        return jsonify({"error": "Trabajador not found."}), 404
# habra que hacer error 400


@trabajador.route('/trabajador/<dni>', methods=["DELETE"])
def deleted_trabajador(dni):
    deleted = control.delete_trabajador(dni)
    if deleted:
        return jsonify({"msg": "Trabajador deleted succesfully"}), 200
    else:
        return jsonify({"error": "Trabajador not found."}), 404
# habra que hacer error 401
