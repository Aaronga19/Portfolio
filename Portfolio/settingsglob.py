from pydantic import BaseSettings

# Settings
class Settings(BaseSettings):
    secret_key: str  
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    email: str
    pass_email: str
    aws_id: str
    aws_access: str
    aws_name: str
    
    class Config:
        env_file = ".env"

settings = Settings()