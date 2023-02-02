from flask import Blueprint
from flask import jsonify,request
import uuid
# Entities
from models.entities.Evento import Evento

#Models
from models.EventoModel import EventoModel



main=Blueprint('evento_blueprint',__name__)

@main.route('/')
def get_eventos():
    try:
        eventos = EventoModel.get_eventos()
        return jsonify(eventos)
    except Exception as ex:
        return jsonify({'message': str(ex) }), 500

@main.route('/<idUsuario>')
def get_evento(idUsuario):
    try:
        evento = EventoModel.get_evento(idUsuario)
        if evento != None: 
            return jsonify(evento)
        else:
            return jsonify({}),404
    except Exception as ex:
        return jsonify({'message': str(ex) }), 500

@main.route('/add',methods=['POST'])
def add_evento():
    try:
        nombreEvento=request.json['nombreEvento']
        fechaInicio=request.json['fechaInicio']
        fechaFin=request.json['fechaFin']
        idUsuario=request.json['idUsuario']
        id = uuid.uuid4().int
        print(id)
        evento= Evento(str(id),nombreEvento,fechaInicio,fechaFin,idUsuario)
        
        affected_rows=EventoModel.add_evento(evento)

        if affected_rows == 1: 
            return jsonify(evento.idEvento)
        else:
            return jsonify({'message': "Error insertando el evento" }), 500
    except Exception as ex:
        return jsonify({'message': str(ex) }), 500

@main.route('/update/<idEvento>',methods=['PUT'])
def update_evento(idEvento):
    try:
        nombreEvento=request.json['nombreEvento']
        fechaInicio=request.json['fechaInicio']
        fechaFin=request.json['fechaFin']
        idUsuario=request.json['idUsuario']
        idEvento=request.json['idEvento']
        evento= Evento(idEvento,nombreEvento,fechaInicio,fechaFin,idUsuario)
        
        affected_rows=EventoModel.update_evento(evento)

        if affected_rows == 1: 
            return jsonify(evento.idEvento)
        else:
            return jsonify({'message': "Error al actualizar el evento" }), 500
    except Exception as ex:
        return jsonify({'message': str(ex) }), 500


@main.route('/delete/<idEvento>',methods=['DELETE'])
def delete_evento(idEvento):
    try:
        evento=Evento(idEvento)
        affected_rows = EventoModel.delete_evento(evento)
        if affected_rows == 1: 
            return jsonify(evento.idEvento)
        else:
            return jsonify({'message': "No se elimino ningun evento" }), 500
    except Exception as ex:
        return jsonify({'message': str(ex) }), 500