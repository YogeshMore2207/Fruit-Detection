from flask import Flask, render_template, request
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
from PIL import Image, ImageDraw
import numpy as np
import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

app = Flask(__name__)

# Load environment variables
load_dotenv()

tempData = {"tag_names": []}

# Azure Storage account connection string
connection_string = os.getenv('AzureBlobStorageConnectionString')
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Azure Storage container name
container_name = 'images'
container_client = blob_service_client.get_container_client(container_name)

def list_images():
    blob_list = container_client.list_blobs()
    image_list = [blob.name for blob in blob_list]
    return image_list

def detect_objects(image_file):
    try:
        # Load Configuration Settings
        load_dotenv()
        prediction_endpoint = os.getenv('PredictionEndpoint')
        prediction_key = os.getenv('PredictionKey')
        project_id = os.getenv('ProjectID')
        model_name = os.getenv('ModelName')

        # Authenticate a client for the prediction API
        credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
        prediction_client = CustomVisionPredictionClient(endpoint=prediction_endpoint, credentials=credentials)

        tempData["tag_names"] = []

        # Load image and get dimensions
        image = Image.open(image_file)
        h, w, ch = np.array(image).shape

        # Detect objects in the image
        with open(image_file, mode="rb") as image_data:
            results = prediction_client.detect_image(project_id, model_name, image_data)

        # Draw bounding boxes on the image for detected objects
        draw = ImageDraw.Draw(image)
        lineWidth = int(w / 1000)
        color = 'red'
        for prediction in results.predictions:
            if (prediction.probability * 100) > 50:
                left = prediction.bounding_box.left * w
                top = prediction.bounding_box.top * h
                height = prediction.bounding_box.height * h
                width = prediction.bounding_box.width * w
                print("The Prediction", prediction)
                points = ((left, top), (left + width, top), (left + width, top + height), (left, top + height),
                          (left, top))
                draw.line(points, fill=color, width=lineWidth)
                draw.text((left, top), f"{prediction.tag_name}: {prediction.probability:.2f}%", fill=color)
                tempData["tag_names"].append(prediction.tag_name)
                print(f"Detected Tag: {prediction.tag_name}, Probability: {prediction.probability * 100:.2f}%")

        # Save the modified image with bounding boxes
        outputfile = 'static/images/output.jpg'
        image.save(outputfile)

        fruit = {"names": tempData["tag_names"], "image": outputfile}
        return fruit

    except Exception as ex:
        print(ex)
        return None

@app.route('/')
def index():
    image_list = list_images()
    return render_template('index.html', image_list=image_list)

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        selected_image = request.form.get('file')
        if not selected_image:
            return 'No image selected'

        # Download the selected image from Azure Blob Storage
        blob_client = container_client.get_blob_client(selected_image)
        image_content = blob_client.download_blob().readall()

        # Save the image locally for processing
        local_image_path = os.path.join('static/images', selected_image)
        with open(local_image_path, 'wb') as local_image_file:
            local_image_file.write(image_content)

        fruit = detect_objects(local_image_path)
        if fruit:
            return render_template('result.html', result_image=fruit["image"], fruit_names=fruit["names"])
        else:
            return render_template('result.html', error_message='Error processing image')
    return 'Invalid request'

if __name__ == '__main__':
    app.run(debug=True)
