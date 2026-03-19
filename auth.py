from passlib.context import CryptContext 
from jose import jwt
from datetime import datetime, timedelta


# token ante if login done then the person gets a token so ah token means this person has authentication ani malli login ayte new token ostadi
# hash pass one side ee pass to hash can kani return cant so just checking to see pass crct aa kada ani chudadaniki
# bcrypt for hashing and hs256 for tokens

SECRET_KEY = "supersecretkey" # token ni sign cheyyadaniki vadtam so ah token real ah fake ani telsukovadaniki
ALGORITHM = "HS256" # algorithm used to sign token
ACCESS_TOKEN_EXPIRE_MINUTES = 60 # expire kakapote infinite time ki valid untadi

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# nrml pass ni hash laga convert chestadi bcrypt algorithm tho

# method to hash password
def hash_password(password: str):
    return pwd_context.hash(password)

#hash unnu nrml pss compare chesi same ah kada cheptadi ante pass ni hash chesi same ahh kaada check chestadi
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# token ni chese method
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES) # current time+ expire ayye time
    to_encode.update({"exp": expire}) # ee tym ayyaka token expire aytadi so malli login ayyi malli new token techukovali
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    # Takes your data, Locks it using SECRET_KEY, Returns a secure string