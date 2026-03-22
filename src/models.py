from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional

db = SQLAlchemy()


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    firstname: Mapped[str] = mapped_column(String(50), nullable=False)
    lastname: Mapped[str] = mapped_column(String(100), nullable=True)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    favoritos_personajes: Mapped[List['FavoritosPersonajes']] = relationship(
        back_populates='user')
    favoritos_vehiculos: Mapped[List['FavoritosVehiculos']] = relationship(
        back_populates='user')
    favoritos_lugares: Mapped[List['FavoritosLugares']
                              ] = relationship(back_populates='user')
    favoritos_criaturas: Mapped[List['FavoritosCriaturas']] = relationship(
        back_populates='user')
    favoritos_droides: Mapped[List['FavoritosDroides']
                              ] = relationship(back_populates='user')
    favoritos_organizaciones: Mapped[List['FavoritosOrganizaciones']] = relationship(
        back_populates='user')
    favoritos_especies: Mapped[List['FavoritosEspecies']] = relationship(
        back_populates='user')

    def serialize(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "favoritos": {
                'personajes': [favorito.serialize() for favorito in self.favoritos_personajes],
                'vehiculos': [favorito.serialize() for favorito in self.favoritos_vehiculos],
                'lugares': [favorito.serialize() for favorito in self.favoritos_lugares],
                'criaturas': [favorito.serialize() for favorito in self.favoritos_criaturas],
                'droides': [favorito.serialize() for favorito in self.favoritos_droides],
                'organizaciones': [favorito.serialize() for favorito in self.favoritos_organizaciones],
                'especies': [favorito.serialize() for favorito in self.favoritos_especies]
            }
        }


class Personaje(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    image: Mapped[str] = mapped_column(String(255))

    favoritos: Mapped[List['FavoritosPersonajes']] = relationship(
        back_populates='personaje')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'image': self.image,
        }


class FavoritosPersonajes(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    personaje_id: Mapped[int] = mapped_column(
        ForeignKey('personaje.id'), nullable=False)

    user: Mapped['User'] = relationship(back_populates='favoritos_personajes')
    personaje: Mapped['Personaje'] = relationship(back_populates='favoritos')

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'personaje_id': self.personaje_id
        }


class Vehiculo(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    image: Mapped[str] = mapped_column(String(255))

    favoritos: Mapped[List['FavoritosVehiculos']] = relationship(
        back_populates='vehiculo')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'image': self.image,
        }


class FavoritosVehiculos(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    vehiculo_id: Mapped[int] = mapped_column(
        ForeignKey('vehiculo.id'), nullable=False)

    user: Mapped['User'] = relationship(back_populates='favoritos_vehiculos')
    vehiculo: Mapped['Vehiculo'] = relationship(back_populates='favoritos')

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'vehiculo_id': self.vehiculo_id
        }


class Lugar(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    image: Mapped[str] = mapped_column(String(255))

    favoritos: Mapped[List['FavoritosLugares']] = relationship(
        back_populates='lugar')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'image': self.image,
        }


class FavoritosLugares(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    lugar_id: Mapped[int] = mapped_column(
        ForeignKey('lugar.id'), nullable=False)

    user: Mapped['User'] = relationship(back_populates='favoritos_lugares')
    lugar: Mapped['Lugar'] = relationship(back_populates='favoritos')

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'lugar_id': self.lugar_id
        }


class Criatura(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    image: Mapped[str] = mapped_column(String(255))

    favoritos: Mapped[List['FavoritosCriaturas']] = relationship(
        back_populates='criatura')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'image': self.image,
        }


class FavoritosCriaturas(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    criatura_id: Mapped[int] = mapped_column(
        ForeignKey('criatura.id'), nullable=False)

    user: Mapped['User'] = relationship(back_populates='favoritos_criaturas')
    criatura: Mapped['Criatura'] = relationship(back_populates='favoritos')

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'criatura_id': self.criatura_id
        }


class Droide(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    image: Mapped[str] = mapped_column(String(255))

    favoritos: Mapped[List['FavoritosDroides']
                      ] = relationship(back_populates='droide')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'image': self.image,
        }


class FavoritosDroides(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    droide_id: Mapped[int] = mapped_column(
        ForeignKey('droide.id'), nullable=False)

    user: Mapped['User'] = relationship(back_populates='favoritos_droides')
    droide: Mapped['Droide'] = relationship(back_populates='favoritos')

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'droide_id': self.droide_id
        }


class Organizacion(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    image: Mapped[str] = mapped_column(String(255))

    favoritos: Mapped[List['FavoritosOrganizaciones']] = relationship(
        back_populates='organizacion')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'image': self.image,
        }


class FavoritosOrganizaciones(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    organizacion_id: Mapped[int] = mapped_column(
        ForeignKey('organizacion.id'), nullable=False)

    user: Mapped['User'] = relationship(
        back_populates='favoritos_organizaciones')
    organizacion: Mapped['Organizacion'] = relationship(
        back_populates='favoritos')

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'organizacion_id': self.organizacion_id
        }


class Especie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    image: Mapped[str] = mapped_column(String(255))

    favoritos: Mapped[List['FavoritosEspecies']] = relationship(
        back_populates='especie')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'image': self.image,
        }


class FavoritosEspecies(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    especie_id: Mapped[int] = mapped_column(
        ForeignKey('especie.id'), nullable=False)

    user: Mapped['User'] = relationship(back_populates='favoritos_especies')
    especie: Mapped['Especie'] = relationship(back_populates='favoritos')

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'especie_id': self.especie_id
        }
