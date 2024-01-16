<h1>Microsoft-Future-Ready-Talent-Virtual-Internship-Project</h1>
<h2>Project Title:</h2><b><a href="https://fruitdetection.azurewebsites.net/">Automated Fruit Detection System for Image Analysis.</b></a>
<br>
<h2>Project Details</h2>
<b>Project Demo URL :</b> https://fruitdetection.azurewebsites.net/ <br>
<b>Demo Video URL :</b> https://drive.google.com/file/d/1bLptg01EM3NtTRZY6j6X_FCmrwf_2TN9/view <br>
<b>Github Repository URL :</b> https://github.com/YogeshMore2207/Fruit-Detection.git <br>
<b>Industry :</b> Lifestyle<br>
<h2>Azure Services Used</h2>
<h3>
Core Azure Services : <br>
1. Azure App Service <br>
2. Azure Storage Account(Blob Storage)  <br> <br>
Azure AI Service <br>
1. Azure AI Custom Vision Service
</h3>
<h2>Problem Statement</h2>
<p align="justify">The manual inspection and classification of fruits in large quantities can be time-consuming, error-prone, and labor-intensive. Traditional methods lack efficiency and precision, leading to challenges in quality control and timely decision-making. The need for an automated fruit detection system arises to address these challenges and enhance the overall productivity of fruit-related industries.</p>
<h2>Project Description</h2>
<p align="justify">The Automated Fruit Detection System is a custom vision application designed to automatically identify and classify fruits in images. Leveraging state-of-the-art machine learning techniques, the system aims to streamline processes in agriculture, inventory management, and food processing industries. Users can upload images containing fruits, and the system will provide accurate detection and classification results.</p><br>
<b>Key Features :</b>
<ul>
    <li>Automated Fruit Detection</li>
    <li>User-Friendly Interface</li>
    <li>Real-time Processing</li>
    <li>Accuracy and Reliability</li>
    <li>Azure App Service Hosting</li>
    <li>Azure Blob Service for Efficient Data Management</li>
</ul>
<b>Future Enhancements :</b>
<ul>
    <li>Integration with mobile applications for on-the-go fruit detection.</li>
    <li>Implementation of more advanced machine learning models for improved accuracy.</li>
    <li>Support for real-time video analysis.</li>
<h2>Core Azure Services</h2>
<b>Azure App Service :</b><br><p align="justify"><br>The project utilizes Azure App Service to host the web application, ensuring scalability, reliability, and ease of deployment. This service enables seamless integration with other Azure components and provides a secure environment for the application.</p>

<b>Azure Storage Account(Blob Storage) :</b><br><p align="justify">Azure Blob Storage is Microsoft's object storage solution for the cloud. It allows you to store and manage large amounts of unstructured data, such as text or binary data, making it suitable for various use cases, including serving images or documents to web applications, storing backups, and more.</p>
<h2>Azure AI Custom Vision Service</h2>
<b>Azure AI Custom Vision Service :</b><br><br><p align="justify">Azure Custom Vision is a cloud-based service provided by Microsoft as part of the Azure Cognitive Services suite. It is designed to help developers build custom image classification models without the need for extensive machine learning expertise. The service leverages pre-trained deep learning models and allows you to train a model using your own image datasets.</p>
<h2>Project Workflow</h2>
<p align="justify">
<ol>
<li>Set Up Environment:</li>
 - Import necessary modules and libraries, including Flask, Azure Cognitive Services SDK, PIL (Pillow), NumPy, and others.<br>
 - Load environment variables using dotenv for sensitive information such as Azure Storage connection strings, prediction endpoint, prediction key, project ID, and model name.
<li>Initialize Flask App:</li>
    - Create a Flask web application instance.
<li>Azure Blob Storage Integration:</li>
    - Use the Azure Storage SDK to interact with Azure Blob Storage.<br>
    - Fetch images from the specified container in Azure Blob Storage using the list_images function.
<li>Image Processing and Object Detection:</li>
    - Implement the detect_objects function to:<br>
        - Load configuration settings and authenticate the Custom Vision Prediction client.<br>
        - Open the uploaded image using Pillow (PIL) library.<br>
        - Use the Azure Custom Vision service to detect objects in the image.<br>
        -Draw bounding boxes around detected objects and annotate with tag names and probabilities.<br>
        - Save the modified image with bounding boxes.

<li>Flask Routes:</li>
    - Define two Flask routes:<br>
    - /: Display a list of images available in the Azure Blob Storage container on the             homepage.<br>
    - /upload: Handle image uploads, download the selected image, process it for object             detection, and render the result on a new page.

<li>Web Templates:</li>
    - Use HTML templates (index.html and result.html) for rendering the web pages.<br>
    - Display the list of images on the homepage, and after image upload, show the processed         image with detected object information.

<li>Run the Flask App:</li>
    - Use if __name__ == '__main__': to run the Flask application locally when the script is executed directly.
<li>Run the Application:</li>
- Execute the Python script to start the Flask development server.<br>
- Access the web application in a web browser.

<li>Upload and Process Images:</li>
- Upload an image using the provided web interface.<br>
- The application will download the selected image from Azure Blob Storage, process it using the Azure Custom Vision service, and display the result on a new webpage.

<li>Display Results:</li>
- Display the modified image with bounding boxes around detected objects.<br>
- Show the detected object names and probabilities on the result page.

</ol>
<h2>Screenshots</h2>
<h3>Azure App Service</h3>
<b>Description :</b><p align="justify">Azure App Service provides a scalable and reliable hosting environment. It ensures seamless deployment and high availability, facilitating an optimal user experience.</p>
<img src="https://github.com/YogeshMore2207/Fruit-Detection/blob/main/screenshots/Screenshot%202024-01-16%20141150.png" alt="azure-app-service"></img><br>
<h3>Azure Storage Account(Blob Storage)</h3>
<b>Description :</b><p align="justify"> Azure Blob Storage is Microsoft's object storage solution for the cloud. It allows you to store and manage large amounts of unstructured data, such as text or binary data, making it suitable for various use cases, including serving images or documents to web applications, storing backups, and more.</p>
<img src="https://github.com/YogeshMore2207/Fruit-Detection/blob/main/screenshots/Screenshot%202024-01-16%20141324.png" alt="azure-blob-storage-service"></img><br>
<h3>Azure AI Custom Vision Service</h3>
<b>Description :</b><p align="justify">The Automated Fruit Detection System is a custom vision application designed to automatically identify and classify fruits in images.</p>
<img src="https://github.com/YogeshMore2207/Fruit-Detection/blob/main/screenshots/Screenshot%202024-01-16%20141448.png" alt="azure-ai-custom-vision"></img><br>
<h3>Azure AI Custom Vision Service Training Dataset</h3>
<b>Description :</b><p align="justify"><b>Description :</b><p align="justify">The Automated Fruit Detection System is a custom vision application designed to automatically identify and classify fruits in images.</p></p>
<img src="https://github.com/YogeshMore2207/Fruit-Detection/blob/main/screenshots/Screenshot%202024-01-16%20141605.png" alt="trining dataset"></img><br>
<h3>Working Live Project Display</h3>
<b>Description :</b><p align="justify">Here I am attaching the final working website's screenshot for the reference.</p>
<img src="https://github.com/YogeshMore2207/Fruit-Detection/blob/main/screenshots/Screenshot%202024-01-16%20141924.png"></img>
<img src="https://github.com/YogeshMore2207/Fruit-Detection/blob/main/screenshots/Screenshot%202024-01-16%20142006.png"></img>

<h2>Conclusion</h2>
<p align="justify">
<b>In conclusion, the project demonstrates an end-to-end workflow for building a web application that leverages Azure services for image storage and analysis, providing users with insights into the content of uploaded images.</b>
</p> <br>
</h2><b><a href="https://fruitdetection.azurewebsites.net/">Automated Fruit Detection System for Image Analysis.</b></a>
