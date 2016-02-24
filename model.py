from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

############################################################################
#Model Definitions

class Character(db.Model):
    """Character information"""

    __tablename__ = "characters"

    character_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    character_name = db.Column(db.String(75), nullable=False)
    civilian_name  = db.Column(db.String(75), nullable=True)
    abilities = db.Column(db.String(400), nullable=False)
    description = db.Column(db.String(2000), nullable=False)
    image1 = db.Column(db.String(100))
    image2 = db.Column(db.String(100))

    groups = db.relationship("Group",
                            secondary = "charactergroups",
                            backref = "characters")


    def __repr__(self):
        """Representation of info when printed."""

        return "<%s | %s | id=%s>" % (
            self.character_name, self.civilian_name, self.character_id)

class Movie(db.Model):
    """Movie Information"""

    __tablename__ = "movies"

    movie_id = db.Column(db.Integer, primary_key=True)
    movie_name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    release_date = db.Column(db.String(10))
    image = db.Column(db.String(100))

    characters = db.relationship("Character",
                                    secondary="moviecharacters",
                                    backref="movies")

    def __repr__(self):
        """Representation of info when printed."""

        return "<%s:%s>" % (self.movie_name, self.movie_id)

class MovieCharacter(db.Model):
    """Association table."""

    __tablename__ = "moviecharacters"

    moviecharacter_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    character_id = db.Column(db.Integer, 
                    db.ForeignKey('characters.character_id'), 
                    nullable=False)
    movie_id = db.Column(db.Integer, 
                    db.ForeignKey('movies.movie_id'), 
                    nullable=False)

    def __repr__(self):
        """Representation of info when printed"""

        return "<moviecharacter_id=%s | movie_id=%s | character_id=%s>" %(
            self.moviecharacter_id, self.movie_id, self.character_id)

class Group(db.Model):
    """Table explaining the types of relationships between characters."""

    __tablename__ = "groups"

    group_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    group_name = db.Column(db.String(100), nullable=False)
    group_type = db.Column(db.String(20), nullable= False)

    def __repr__(self):
        """Representation of info when printed."""

        return"<group_name=%s | type=%s | id=%s>" %(
            self.group_name, self.group_type, self.group_id)

class CharacterGroup(db.Model):
    """Middle table between Characters and Relationships."""

    __tablename__="charactergroups"

    chargroup_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    character_id = db.Column(db.Integer, 
                    db.ForeignKey('characters.character_id'), 
                    nullable=False)
    group_id = db.Column(db.Integer, 
                        db.ForeignKey('groups.group_id'), 
                        nullable=False)
    joined_at = db.Column(db.String(50) )
    left_at = db.Column(db.String(50))

    characters = db.relationship("Character", 
                                backref= "chargroups")
    groups = db.relationship("Group",
                            backref="chargroups")

    def __repr__(self):
        """Representation of info when printed."""

        return "group_id=%s | character_id=%s | joined_at=%s  | left_at=%s" %(
            self.group_id, self.character_id, self.joined_at, self.left_at)




##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///mcu'
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."