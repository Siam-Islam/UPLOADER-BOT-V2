import os

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1763065907:AAEtGmMbHR8lZTY5xn0XYtm9JWAp_Zga0OY")
    
    API_ID = int(os.environ.get("API_ID", 2766365))
    
    API_HASH = os.environ.get("API_HASH", "b867ccbeb57dd4f0c8e1d82e8bc363ef")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 50000000

    TG_MAX_FILE_SIZE = 2097152000

    FREE_USER_MAX_FILE_SIZE = 50000000
    
    CHUNK_SIZE = int(128)

    HTTP_PROXY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 3600
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "1369867278"))

    SESSION_NAME = "UploadLinkToFileBot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Testbot:1234509876@cluster0.aelsk.mongodb.net/cluster0?retryWrites=true&w=majority")

    MAX_RESULTS = "50"
