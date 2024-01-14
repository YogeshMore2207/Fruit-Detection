from flask import Flask, render_template, request
from azure.storage.blob import BlobServiceClient
from your_script import main
import os

app = Flask(__name__)

# Azure Storage account connection string
AZURE_STORAGE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=imagedataaset;AccountKey=hruUBI3GQpwLYZivfPlha22v+5GVY4QmqYgCLYMMH6bHbs2S4wmo5W+k1kFcrsM+v29q8dxUX7Nb+AStAExP5w==;EndpointSuffix=core.windows.net"

# Create a BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)

# Create a Blob Container
container_name = "images"
blob_container_client = blob_service_client.get_container_client(container_name)
# blob_container_client.create_container()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Perform image processing when files are uploaded
        files = request.files.getlist('file')
        
        for file in files:
            # Save the uploaded file to Azure Blob Storage
            blob_client = blob_container_client.get_blob_client(file.filename)
            blob_client.upload_blob(file.stream.read(), overwrite=True)

        # Call your image processing function
        main()
        return 'Image processing complete'

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
