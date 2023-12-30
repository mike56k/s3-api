from flask import Flask
from flask_restx import Api, Resource, fields
import os

app = Flask(__name__)
app.config['FILES_DIR'] = os.environ.get('S3_BUCKET_DIR')

api = Api(app)

class FileList(Resource):
    @api.doc('GET')
    @api.response(200, 'List of files')
    def get(self):
        files = os.listdir(app.config['FILES_DIR'])
        return {'files': files}

class FileContent(Resource):
    @api.doc('GET')
    @api.response(200, 'Content of the file')
    def get(self, filename):
        file_path = os.path.join(app.config['FILES_DIR'], filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                content = file.read()
                return {'filename': filename, 'content': content}
        else:
            return {'error': 'File not found'}, 404

api.add_resource(FileList, '/files')
api.add_resource(FileContent, '/files/<filename>')

if __name__ == '__main__':
    app.run(port='5000')