from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load the dataset
data = pd.read_csv("ibmdata.csv")
print(data.head())

def try_home():
    return "Flask is running" 
# Analyze an argument using the dataset
def analyze_argument(user_arg):
    # Find arguments that match part of the user's argument
    similarity = data[data["argument"].str.contains(user_arg[:20], case = False, na = False)]

    if not similarity.empty:
        # Average quality score for similar arguments
        avg_score = similarity["WA"].mean()
        comment = "Similar to others in the dataset."
    else:
        # Default score if no match is found
        avg_score = 50
        comment = "Unique but not strong enough."

    return {"score": round(avg_score, 2), "comment": comment}

@app.route("/")
def index():
    print("Route is being accessed!")
    result = None
    if request.method == "POST":
        argument = request.form.get("argument")
        if argument:
            result = analyze_argument(argument)
    return "<h1>Flask is Working!</h1>"

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)