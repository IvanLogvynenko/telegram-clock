class Configuration:
    SESSION_NAME = ""
    API_ID = ""
    API_HASH = ""

    def __init__(self, config_path="app.conf"):
        file = open(config_path, "r")
        for line in file:
            key, value = line.split("=")
            if key == "SESSION_NAME":
                self.SESSION_NAME = str(value).replace("\n", "")
            elif key == "CREDENTIALS_PATH":
                creds = open(value, "r")
                api_id, api_hash = creds
                self.API_ID = str(api_id.split("=")[1])
                self.API_HASH = str(api_hash.split("=")[1])
            else:
                raise ValueError(f"Parsing failed on {line}")
