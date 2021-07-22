import yaml
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base


with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

Base = declarative_base()
engine = sa.create_engine(f"{config['DATABASE_URI']}/{config['SCHEMA_NAME']}")


class Court_Availabilities(Base):

    __tablename__ = "court_availabilities"

    court_availability_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    domain = sa.Column(sa.String(128), nullable=False)
    url = sa.Column(sa.String(256), nullable=False)
    openplay_court_id = sa.Column(sa.Integer, nullable=False)
    openplay_court_name = sa.Column(sa.String(24), nullable=False)
    openplay_court_slot = sa.Column(sa.String(9), nullable=False)
    slot_date = sa.Column(sa.Date, nullable=False)
    slot_hour = sa.Column(sa.Integer, nullable=False)
    slot_available = sa.Column(sa.Boolean, nullable=False)
    datetime_added = sa.Column(sa.DateTime, nullable=False)
