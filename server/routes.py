from server import app
import os
from flask import send_from_directory,jsonify,request,redirect
from server import aws_control

# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


@app.route('/api/persons',methods=['GET'])
def getItems():
  return jsonify(aws_control.get_items())

@app.route('/api/persons', methods=['POST'])
def createItem():
  newObject = request.get_json()

  if newObject is not None:
    response = aws_control.create_item(newObject)
  else:
    return redirect('/')

  return jsonify(response) 


@app.route('/api/persons/<id>', methods=['PUT'])
def updateItem(id):
  updateObject = request.get_json()
  
  if id is not None and updateObject is not None:
    response = aws_control.update_item(id,updateObject)
 
  return jsonify(updateObject)


@app.route('/api/persons/<id>', methods=['DELETE'])
def deleteItem(id):
  if id is not None:
    response = aws_control.delete_item(id)

  return jsonify(response)  



    
