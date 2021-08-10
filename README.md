
# EchoNet Cardiogram Segmentation Model Pipeline

We have created a pipleine for the EchoNet Segmentation model that is built by Stanford University. A Streamlit UI and RESTful API accompanies this pipleine

### Deep Learning pipeline

We are aiming to make the above mentioned services, namely Frame-by-frame Semantic Segmentation of the Left Ventricle, Prediction of Ejection Fraction from Subsampled Clips, and Assesment of Cardiomyopathy using a deep learning pipeline. We  have an API that will accept a POST request with the video and process it to return an ejection fraction value. A GET request will be needed to retrieve the resulting video.

## Acknowledgements

 - [Echonet github repo](https://github.com/echonet/dynamic)
 - [Paper](https://www.nature.com/articles/s41586-020-2145-8)
 - [Website](https://echonet.github.io/dynamic/)

  
## API Reference

#### Get status

```http
  GET /api/
```
Sets up the environment to and API

#### Upload video for segmentaion

```http
  POST /api/send_video
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `file` | ` multipart/form-data` | **Required**. Video to be uploaded |

Uploads files to be analyzed by model and outputs a JSON laden with a CSV file containing the Ejection Fraction calculated by the model

#### Get segmented files

```http
  GET /api/get_video
```
Gets the annotated video of echocardiogram after the segmentation pipeline has been run on it

## Running the pipeline

### Creating Virtual Environment and activating it

### Step 1
Make sure python3 is installed on your system.

### Step 2
Open cmd and create a Virtual Environment using the command
```bash
python -m venv [virtualenvironmentname]
```

### Step 3 
Activate the Virtual Environment using the command 
```bash
[virtualenvironmentname]\Scripts\activate
```
### Step 4
Open another cmd and activate the same Virtual Environment the way you did in Step 3.
### Step 5 
In one of the cmd change the present working directory to the backend folder path of the cloned directory by using the command 
```bash
cd [pathofbackendfolder]
```
and in the other cmd change the present working directory to the frontend folder path of the cloned directory. 

## Installing the required packages

In the cmd which has present working directory as backend folder path type in 
```bash
pip install -r requirements.txt
```
and hit enter, all the requirements will be downloaded and installed.

## Executing the code

### Step 1
Change the CONFIG_PATH variable location in the Echocardiogram.py to the folder where the configure.yaml is located.

### Step 2
In the cmd which has present working directory as backend folder path and execute 
```bash
python backend.py
```

### Step 3
In the cmd which has present working directory as frontend folder path type in streamlit run app.py and the streamlit web page will automatically open incase it doesn't open go to web browser and type in http://localhost:8501/ and the streamlit webpage will open.

### Step 4
Once you see the streamlit webpage click on Browse Files and then select the a4c view video of the heart i.e. in .avi format as input to the model and click on Upload.

### Step 5
Once the above step is performed the pretrained models with weights are downloaded and you can see the progress in the console of cmd which has present working directory as backend folder and on successful execution you will be able to see the ejection fraction percentage for a given video and the segmented video o/p on the streamlit web page.

### Step 6
You can download the csv file of the ejection fraction percentage and the .avi format video file of segmented left ventricle for a given a4c view video as input from the streamlit webpage.

## Additional Results

Additional results will be saved in the EjectionFractionResults folder and SegmentationResults folder of the Destination folder which gets created in backend folder on successful execution.

## Authors

- [Amruth J]()
- [Mudit S]()
- [Eshaan G]()

