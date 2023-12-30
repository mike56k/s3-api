from flask import Flask, jsonify
import os

app = Flask(__name__)
app.config["FILES_DIR"] = "/mnt/s3"

@app.route('/files', methods=['GET'])
def get_file_list():
    files = os.listdir(app.config["FILES_DIR"])
    return jsonify({"files": files}), 200

@app.route('/files/<filename>', methods=['GET'])
def get_file_content(filename):
    file_path = os.path.join(app.config["FILES_DIR"], filename)
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        return jsonify({"filename": filename, "content": content})
    else:
        return jsonify({"error": "File not found"}), 404

if __name__ == '__main__':
    app.run()