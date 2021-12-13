from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Sighting:
    db_name = 'sightings'

    def __init__(self,db_data):
        self.id = db_data['id']
        self.location = db_data['location']
        self.description = db_data['description']
        self.date_reported = db_data['date_reported']
        self.date_sighted = db_data['date_sighted']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.user_id = db_data['user_id']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO sightings (location, description, date_sighted,user_id) VALUES (%(location)s,%(description)s,%(date_sighted)s,%(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM sightings;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        return results
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM sightings WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls( results[0] )

    @classmethod
    def update(cls, data):
        query = "UPDATE sightings SET location=%(location)s, description=%(description)s, date_sighted=%(date_sighted)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM sightings WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @staticmethod
    def validate_sighting(sighting):
        is_valid = True
        if len(sighting['location']) < 3:
            is_valid = False
            flash("location must be at least 3 characters","sighting")
        if len(sighting['description']) < 3:
            is_valid = False
            flash("Description must be at least 3 characters","sighting")
        if sighting['date_sighted'] == "":
            is_valid = False
            flash("Please enter a date","sighting")
        return is_valid
