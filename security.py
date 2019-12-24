from werkzeug.security import safe_str_cmp
from models.user import UserModel

# users = [
# 	User(1,'kans','kans')
# ]

# username_mapping = { u.username : u for u in users}

# userid_mapping = { u.id : u for u in users}

# userid_mapping = { 1: {
# 		'id':1,
# 		'username':'kans',
# 		'password':'kans'
# 	}
# }

def authentication(username,password):   #to retrieve user bu username
	user = UserModel.find_by_username(username)
	if user and safe_str_cmp(user.password,password):
		return user

#to retrieve user bu user id
def identity(payload):
	user_id = payload['identity']
	return UserModel.find_by_id(user_id)