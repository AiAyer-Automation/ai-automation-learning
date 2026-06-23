from flask import Flask , request
from routes.tasks import tasks_bp
from external.ai_moke import fake_ai
from external.ai_engine import smart_ai

app = Flask(__name__)
app.register_blueprint(tasks_bp)


@app.route("/ai-auto", methods=["POST"])
def ai_auto():

    data = request.json
    text = data.get("text")
    result = smart_ai(text)
    return {
        "input": text,
        "output": result
    }

if __name__ == "__main__":
    app.run(debug=True)