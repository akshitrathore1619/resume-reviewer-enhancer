from flask import Flask, request, jsonify 
 
app = Flask(__name__) 
 
@app.route('/resume-review', methods=['POST']) 
def review_resume(): 
    data = request.get_json() 
    resume_text = data.get("resume_text", "") 
 
    if not resume_text: 
        return jsonify({"error": "No resume text provided"}), 400 
 
    response = { 
        "feedback": { 
            "missing_sections": ["Certifications", "Projects"], 
            "keyword_suggestions": ["Cloud Computing", "Machine Learning"], 
            "resume_score": 7.5 
        } 
    } 
    return jsonify(response) 
 
if __name__ == '__main__': 
    app.run(debug=True) 
