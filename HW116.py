def get_credentials_users(path):
    credentials_list = []
    with open(path, "rb") as file:
        for line in file:
            line = line.decode("utf-8").strip()
            credentials_list.append(line)
        return credentials_list 