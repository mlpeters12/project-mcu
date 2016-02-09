from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

############################################################################
#Model Definitions

class Character(db.Characters):
    """Character information"""

    __tablename__ = "characters"

    character_id