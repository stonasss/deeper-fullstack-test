from bson import ObjectId
from app.models.user_model import User, UserPreferences
from datetime import datetime

class UserService:
    @staticmethod
    def get_all_users(db):
        users = db.users.find()
        return [UserService._map_user(user) for user in users]

    @staticmethod
    def get_user_by_id(db, user_id):
        user = db.users.find_one({'_id': ObjectId(user_id)})
        return UserService._map_user(user) if user else None

    @staticmethod
    def create_user(db, data):
        user = User(
            username=data['username'],
            password=data['password'],
            roles=data.get('roles', []),
            preferences=UserPreferences(timezone=data['preferences']['timezone']),
            created_ts=datetime.now().timestamp(),
            active=data.get('active', True)
        )
        user_dict = user.dict()
        result = db.users.insert_one(user_dict)
        user_dict['_id'] = str(result.inserted_id)
        return user_dict

    @staticmethod
    def update_user(db, user_id, data):
        updated_data = {
            'username': data.get('username'),
            'password': data.get('password'),
            'roles': data.get('roles'),
            'preferences': data.get('preferences'),
            'active': data.get('active')
        }
        db.users.update_one({'_id': ObjectId(user_id)}, {'$set': updated_data})
        return UserService.get_user_by_id(db, user_id)

    @staticmethod
    def delete_user(db, user_id):
        db.users.delete_one({'_id': ObjectId(user_id)})

    @staticmethod
    def _map_user(user_data):
        if not user_data:
            return None
        user_id = user_data.pop('_id', None)

        preferences = user_data.get('preferences', {})
        if isinstance(preferences, str):
            preferences = { "timezone": preferences }
        elif isinstance(preferences, list):
            preferences = preferences[0] if len(preferences) > 0 else {}
        if not isinstance(preferences, dict):
            preferences = {}
        if "timezone" not in preferences:
            preferences["timezone"] = "UTC"

        user_data['preferences'] = UserPreferences(**preferences)
        user = User(**user_data)

        user_dict = user.dict()
        user_dict['_id'] = str(user_id)

        return user_dict