
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

WEBHOOK_URL = 'https://hook.us2.make.com/s9t65nbxzp8oakm3jlfivw627vd7t6os'

@app.route('/agregar-pendiente', methods=['POST'])
def agregar_pendiente():
    data = request.json

    required_fields = ['Cliente', 'Descripción', 'Fecha de Pedido', 'Fecha de Entrega', 'Material', 'Encargado', 'Entregado', 'Fecha de Entregado']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Falta el campo: {field}'}), 400

    response = requests.post(WEBHOOK_URL, json=data)

    if response.status_code == 200:
        return jsonify({'status': '✅ Pendiente enviado correctamente.'})
    else:
        return jsonify({'status': '❌ Error enviando a Make.', 'details': response.text}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
