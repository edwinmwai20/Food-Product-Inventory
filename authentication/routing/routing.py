from flask import Flask, request, jsonify
# from Models.repo import InventoryRepo (Import your repo here)

app = Flask(__name__)
repo = InventoryRepo()

@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(repo.get_all()), 200

@app.route('/inventory', methods=['POST'])
def add_item():
    data = request.json
    new_prod = Product(**data) 
    repo.add(new_prod)
    return jsonify(new_prod.to_dict()), 201

@app.route('/inventory/<int:id>', methods=['DELETE'])
def delete_item(id):
    success = repo.delete(id)
    return jsonify({"success": success}), 200 if success else 404