from flask import Flask, request, jsonify

app = Flask(__name__)

def validar_descuento(descuento):
    if descuento < 0 or descuento > 100:
        raise ValueError("El descuento debe estar entre 0 y 100")
    return True

def calcular_precio(precio, descuento):
    validar_descuento(descuento)
    total = precio + (precio * descuento / 100)
    return total

def calcular_peso_envio(peso_unitario, cantidad, peso_empaque=0.5):
    if peso_unitario <= 0 or cantidad <= 0:
        raise ValueError("El peso unitario y la cantidad deben ser mayores a 0")
    return (peso_unitario * cantidad) + peso_empaque

@app.route('/calcular-precio', methods=['POST'])
def api_calcular_precio():
    data = request.get_json()
    try:
        precio = float(data.get('precio'))
        descuento = float(data.get('descuento', 0))
        total = calcular_precio(precio, descuento)
        return jsonify({"precio_final": total}), 200
    except (ValueError, TypeError) as e:
        return jsonify({"error": str(e)}), 400

@app.route('/calcular-peso', methods=['POST'])
def api_calcular_peso():
    data = request.get_json()
    try:
        peso_unitario = float(data.get('peso_unitario'))
        cantidad = int(data.get('cantidad'))
        peso_empaque = float(data.get('peso_empaque', 0.5))
        total_peso = calcular_peso_envio(peso_unitario, cantidad, peso_empaque)
        return jsonify({"peso_total": total_peso}), 200
    except (ValueError, TypeError) as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)