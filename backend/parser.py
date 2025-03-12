import json
from datetime import datetime
from app.models.user_model import User, UserPreferences
from app.utils.database import get_db
from app import create_app

def load_json_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def parse_user_data(user_data):
    roles = []
    if user_data.get('is_user_admin', False):
        roles.append('admin')
    if user_data.get('is_user_manager', False):
        roles.append('manager')    
    if user_data.get('is_user_tester', False):
        roles.append('tester')

    preferences = UserPreferences(timezone=user_data['user_timezone'])
    created_ts = datetime.strptime(user_data['created_at'], "%Y-%m-%dT%H:%M:%SZ").timestamp()

    return User(
        username=user_data['user'],
        password=user_data['password'],
        roles=roles,
        preferences=preferences,
        created_ts=created_ts,
        active=user_data['is_user_active'],
    )

def insert_users_into_mongodb(users, db):
    user_collection = db['users']
    user_collection.insert_many([user.dict() for user in users])

def main():
    app = create_app()
    with app.app_context():
        data = load_json_data('udata.json')
        users = [parse_user_data(user) for user in data['users']]
        db = get_db()
        insert_users_into_mongodb(users, db)
        print("Data inserted successfully!")

if __name__ == "__main__":
    main()
