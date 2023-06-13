import bcrypt

def generate_pwd_hash(password:str):
    bytes = password.encode('utf-8')

    salt = bcrypt.gensalt()

    hash = bcrypt.hashpw(bytes,salt)

    return str(hash)


def check_password(password:str,hashed_pwd):
    bytes = password.encode('utf-8')

    result = bcrypt.checkpw(bytes,hashed_pwd)

    return result