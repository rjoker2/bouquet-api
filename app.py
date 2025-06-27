from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Вставь сюда свой токен Posiflora
POSIFLORA_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3NTEwMjg0MjMsImV4cCI6MTc1MTAzMjAyMywiY3VzdG9tZXIiOiIxMTYxMSIsImlkIjoiMzkzM2UxYTktZmY4ZC00ZjA0LThiOWYtMmZkNTMyM2VkMTE5IiwibG9naW4iOiJLdWxhZ2luYSJ9.UE2e47hkU_r2dp8DBmb_uIyUQb6oW7nX5Y9iYNNoMFUuYA6-QXAdcflGeVZ4L3YURiiw6e_pBFJ8z-4zux6FjS5L6B9bFtMgw-ge6Q6su_2XXMgv-StvvDdxM5viPOl_7N4KVJx-n5nRV-C-iIpPC5y8pHUPrpusrM-zs_RS97amxpS-kW6aMS_ZsMGFIDjSvOxvRoyxEWkG5tLP8NhDccdhzzYpD5TQpLLJuyXfqDhE7qOLu2boTsnP3xcj-HQDSZxgvDEkIE0Ry0bjBzfQMc9NOcNAIXxbnCZ9EBsk7zNvnRYYOKMezZ-BSUWCd1FSvK3lzkvAnYpOeZkM400a-g"

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
