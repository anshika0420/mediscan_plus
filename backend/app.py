from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import uuid
from image_model import predict_image_preset
from triage import triage_from_symptoms
from scheduler import schedule_appointment

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status":"ok","service":"MediScan+ backend"})

@app.route('/api/symptom', methods=['POST'])
def symptom():
    data = request.get_json()
    symptoms = data.get('symptoms', '')
    triage = triage_from_symptoms(symptoms)
    return jsonify({"triage": triage})

@app.route('/api/appointment', methods=['POST'])
def appointment():
    data = request.get_json()
    patient = data.get('patient')
    slot = schedule_appointment(patient, data.get('preferred_date'))
    return jsonify({"scheduled": True, "slot": slot})

@app.route('/api/predict_image', methods=['POST'])
def predict_image():
    if 'image' not in request.files:
        return jsonify({"error":"no file"}), 400
    f = request.files['image']
    filename = secure_filename(f.filename)
    save_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{uuid.uuid4().hex}_{filename}")
    f.save(save_path)
    result = predict_image_preset(save_path)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
