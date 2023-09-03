import flask as fl
import subprocess as sbc

app = fl.Flask(__name__)


@app.route("/process")
def index():
    """
     @brief This function is called when the user clicks the index button. It calls python3 to run the main. py script and returns the result to the template.
     @return The result of the python3 script as a string
    """
    try:
        res = sbc.check_output(["python3", "main.py"], universal_newlines=True)
        return fl.render_template("index.html", result=res)
    except sbc.CalledProcessError as e:
        error = f"Error executing command: {e}"
        return fl.render_template("index.html", result=error)


@app.route("/")
def hello():
    return "Hello World!"


# Run the app if __main__ is called
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=False)
