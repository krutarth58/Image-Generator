from flask import Flask, request
import requests
 
app = Flask(__name__)
 
@app.route("/")
def home():
    return """
<h2>AI Image Generator</h2>
 
    <form action="/generate" method="POST">
<input type="text" name="prompt" placeholder="Enter image prompt" size="40">
<input type="submit" value="Generate">
</form>
    """
 
@app.route("/generate", methods=["POST"])
def generate():
 
    prompt = request.form["prompt"]
 
    image_url = f"https://image.pollinations.ai/prompt/{prompt}"
 
    return f"""
<h3>Prompt: {prompt}</h3>
 
    <img src="{image_url}" width="500">
 
    <br><br>
 
    <a href="/">Generate Another Image</a>
    """
 
if __name__ == "__main__":
    app.run(debug=True)