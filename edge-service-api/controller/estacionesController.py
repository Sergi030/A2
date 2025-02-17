from models.estacion import Estacion, EstacionSchema
from models.cargador import Cargador, CargadorSchema
from utils.db import db


def get_all_estaciones():
    i = Estacion.query.all()
    return EstacionSchema(many=True).dump(i)


def get_estacion_by_id(id):
    i = Estacion.query.filter(Estacion.id_estacion == id).one_or_none()
    if i:
        estacion_dict = EstacionSchema().dump(i)

        estacion_dict["cargadores"] = []
        for cargador in i.Cargadors:
            estacion_dict["cargadores"].append(CargadorSchema().dump(cargador))

        return estacion_dict

    return None


def delete_cargador(id, id_Cargador):
    i = Cargador.query.filter(Cargador.id_cargador == id_Cargador).one_or_none()
    if i:
        db.session.delete(i)
        db.session.commit()
        return True
    return False
