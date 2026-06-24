from flask import request

def login():

    username = request.args.get("user")

    query = f"""
    SELECT * FROM users
    WHERE username = '{username}'
    """

    return query