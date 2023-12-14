def save_credentials_users(path, users_info):

    with open(path, "wb") as fh:
        for username, password in users_info.items():
            user_info = f"{username}:{password}\n".encode("utf-8")
            fh.write(user_info)
    
   