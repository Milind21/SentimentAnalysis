from flask import Flask, jsonify, request
from utilities import predict_pipeline

app = Flask(__name__)

@app.post('/predict')
def predict():
  data = request.json
  try:
    sample=data['text']
  except KeyError:
    return jsonify({'error':'Input Missing'})
  # add more checks in production
  sample = [sample]
  predictions = predict_pipeline(sample)
  try:
    result=jsonify(predictions[0])
  except TypeError as e:
    return jsonify({'error': str(e)})
  return result

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=5001 ,debug=True)