from dotenv import load_dotenv
import os
import qrcode
import json

load_dotenv()

def get_json_data():
    file_path = "data.json"
    with open(file_path, "r") as file:
        data = json.load(file)
    return data

def create_url(id: str):
    data = get_json_data()
    return f"{os.getenv('TELEGRAM_BOT_URL')}?start=qr_{data[id]}"

def generate_qr(url: str, id: str):
    current_directory = os.getcwd()
    filename = f"{id}.png"
    file_path = os.path.join(current_directory, "qr", filename)
    img = qrcode.make(url)
    img.save(file_path)

def generate_qr_codes():
    host = os.getenv("HOST")
    for id in get_json_data():
        url = f"{host}/qr/{id}"
        print(f"Generating QR for {url}...")
        generate_qr(url, id)
        print(f"QR generated for {url}!")
        print("========================")

generate_qr_codes()

