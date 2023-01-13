""" The MyModel model.
"""

import dataclasses

from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from .meta import Base


@dataclasses.dataclass
class MyModel(Base):
    """ The SQLAlchemy declarative model class for a MyModel object.
    """
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)




Index('my_index', MyModel.name, unique=True, mysql_length=255)
