import hashlib
import os
import bcrypt


def process_password(password, method):

    if method == "plain":
        return {
            "stored": password
        }

    elif method == "sha256":
        hashed = hashlib.sha256(password.encode()).hexdigest()
        return {
            "hash": hashed
        }

    elif method == "salted":
        salt = os.urandom(16)
        hashed = hashlib.sha256(salt + password.encode()).hexdigest()
        return {
            "salt": salt.hex(),
            "hash": hashed
        }

    elif method == "bcrypt":
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        return {
            "hash": hashed.decode()
        }
        

def get_attack_info(method):
    
    info = {
        "plain": {"time": "0.0001 san", "status": "LEAKED", "desc": "Müdafiəsizdir."},
        "sha256": {"time": "5 dəq", "status": "LEAKED", "desc": "Rainbow Table ilə tapıldı."},
        "salted": {"time": "3 ay", "status": "SECURED", "desc": "Brute-force tələb olunur."},
        "bcrypt": {"time": "100+ il", "status": "SECURED", "desc": "Sındırılması qeyri-mümkündür."}
    }
    return info.get(method)

def process_password(password, method):
    if method == "plain":
        res = {"stored": password}
        
    elif method == "sha256":
        hashed = hashlib.sha256(password.encode()).hexdigest()
        res = {"hash": hashed}
        
    elif method == "salted":
        salt = os.urandom(16)
        hashed = hashlib.sha256(salt + password.encode()).hexdigest()
        res = {"salt": salt.hex(), "hash": hashed}
        
    elif method == "bcrypt":
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        res = {"hash": hashed.decode()}
    
    return res