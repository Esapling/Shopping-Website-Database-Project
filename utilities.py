from passlib.context import CryptContext


def hashPassword(password):
    """
        Hashes given password and returns it
     """
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    hashed_pass = pwd_context.hash(password)
    return hashed_pass


def verifyPassword(password, hashed_pass):
    """
        Verifies if the given password is correct by given hashed_password  
    """
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    is_password_correct = pwd_context.verify(password, hashed_pass)
    return is_password_correct
