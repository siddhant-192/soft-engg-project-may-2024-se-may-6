from main import cache
from .models import *


@cache.memoize(60*60*24)
def isAuth(ui, apit):
    try:
        currentUser=Users.query.get(ui)
        if currentUser.API_token == apit:
            return True
        return False
    except:
        return False