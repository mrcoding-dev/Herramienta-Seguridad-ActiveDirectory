from dotenv import load_dotenv
import os

def update_token(new_token:str):
    with open("token.txt", "w") as f:
        f.write(new_token)
