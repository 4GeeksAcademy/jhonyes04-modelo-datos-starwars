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

    favoritos: Mapped[List['Favoritos']] = relationship(back_populates='user')

    def serialize(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Character(db.Model):
    _id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    image: Mapped[str] = mapped_column(String(255))

    favoritos: Mapped[List['Favoritos']] = relationship(
        back_populates='character')

    def serialize(self):
        return {
            '_id': self._id,
            'name': self.name,
            'description': self.description,
            'image': self.image,
        }


class Vehicle(db.Model):
    _id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    image: Mapped[str] = mapped_column(String(255))

    favoritos: Mapped[List['Favoritos']] = relationship(
        back_populates='vehicle')

    def serialize(self):
        return {
            '_id': self._id,
            'name': self.name,
            'description': self.description,
            'image': self.image,
        }


class Location(db.Model):
    _id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    image: Mapped[str] = mapped_column(String(255))

    favoritos: Mapped[List['Favoritos']] = relationship(
        back_populates='location')

    def serialize(self):
        return {
            '_id': self._id,
            'name': self.name,
            'description': self.description,
            'image': self.image,
        }


class Creature(db.Model):
    _id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    image: Mapped[str] = mapped_column(String(255))

    favoritos: Mapped[List['Favoritos']] = relationship(
        back_populates='creature')

    def serialize(self):
        return {
            '_id': self._id,
            'name': self.name,
            'description': self.description,
            'image': self.image,
        }


class Droid(db.Model):
    _id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    image: Mapped[str] = mapped_column(String(255))

    favoritos: Mapped[List['Favoritos']] = relationship(back_populates='droid')

    def serialize(self):
        return {
            '_id': self._id,
            'name': self.name,
            'description': self.description,
            'image': self.image,
        }


class Organization(db.Model):
    _id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    image: Mapped[str] = mapped_column(String(255))

    favoritos: Mapped[List['Favoritos']] = relationship(
        back_populates='organization')

    def serialize(self):
        return {
            '_id': self._id,
            'name': self.name,
            'description': self.description,
            'image': self.image,
        }


class Specie(db.Model):
    _id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    image: Mapped[str] = mapped_column(String(255))

    favoritos: Mapped[List['Favoritos']] = relationship(
        back_populates='specie')

    def serialize(self):
        return {
            '_id': self._id,
            'name': self.name,
            'description': self.description,
            'image': self.image,
        }


class Favoritos(db.Model):
    _id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"), nullable=False)
    character_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey('character._id'))
    vehicle_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey('vehicle._id'))
    location_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey('location._id'))
    creature_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey('creature._id'))
    droid_id: Mapped[Optional[int]] = mapped_column(ForeignKey('droid._id'))
    organization_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey('organization._id'))
    specie_id: Mapped[Optional[int]] = mapped_column(ForeignKey('specie._id'))

    user: Mapped['User'] = relationship(back_populates='favoritos')
    character: Mapped[Optional['Character']] = relationship(
        back_populates='favoritos')
    vehicle: Mapped[Optional['Vehicle']] = relationship(
        back_populates='favoritos')
    location: Mapped[Optional['Location']] = relationship(
        back_populates='favoritos')
    creature: Mapped[Optional['Creature']] = relationship(
        back_populates='favoritos')
    droid: Mapped[Optional['Droid']] = relationship(back_populates='favoritos')
    organization: Mapped[Optional['Organization']
                         ] = relationship(back_populates='favoritos')
    specie: Mapped[Optional['Specie']] = relationship(
        back_populates='favoritos')

    def serialize(self):
        return {
            '_id': self._id,
            'user_id': self.user_id,
            'character_id': self.character_id,
            'vehicle_id': self.vehicle_id,
            'location_id': self.location_id,
            'creature_id': self.creature_id,
            'droid_id': self.droid_id,
            'organization_id': self.organization_id,
            'specie_id': self.specie_id,
        }
