from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Вставь сюда свой токен Posiflora
POSIFLORA_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3NTExMDgxNzEsImV4cCI6MTc1MTExMTc3MSwiY3VzdG9tZXIiOiIxMTYxMSIsImlkIjoiMzkzM2UxYTktZmY4ZC00ZjA0LThiOWYtMmZkNTMyM2VkMTE5IiwibG9naW4iOiJLdWxhZ2luYSJ9.d_69XGTdwwuuSS_cXHwAwYhwlCIqWZRxJIXeli0PD6k8SBT8CmUkEp1ylhLYDhCBKFvLyQzXem3wPcZ0nAvrEVrRmOCNtPD_phtDgjkgpJctAhfb1pvw3laxtupgfj8fJC47syqqgLP8jsuGAAlYIZx0zScr_ryMa1LgsFodi75D_mLlbUVWKGLKHt7QEy8LBqUQ32MUECi2Zw1n9XPVA_DVkzRZMmhLJ1BxSNVw2_o4cOfEKALpbhP_F3uSwOnzKU_d6pgnKbqoZSHAeeaAkEh8abw0FFe8my94CsJrB3PEOsiz-LLHku23Srq5nFr_zZpTqLnz3G32r1aMA9ir8Q"

@app.route('/bouquet/<item_id>', methods=['GET'])
def get_bouquet(item_id):
    url = f"https://lagracia.posiflora.com/api/v1/inventory-items/{item_id}"
    headers = {"Authorization": f"Bearer {POSIFLORA_TOKEN}"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return jsonify({"error": "Posiflora API error", "status": response.status_code}), 500

    data = response.json().get("data", {})
    attributes = data.get("attributes", {})
    title = attributes.get("title", "Неизвестно")
    price = attributes.get("price", "Не указано")

    return f"Букет: {title}\nЦена: {price} ₽"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
