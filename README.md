

# AI Self-Diagnosis Tool - Healthcare-AI-WebApp

The **Healthcare-AI-WebApp** leverages Artificial Intelligence (AI) to enhance healthcare by predicting the likelihood of various diseases based on user input. The web application uses machine learning and deep learning techniques to assess the risk of the following diseases:

- **Lung Disease**
- **Heart Disease**
- **Diabetes**


DEMONSTRATION FILES DRIVE LINK  :: https://drive.google.com/file/d/1iynKdlEP625zpN3qIQaIlSh8oyrvqllr/view?usp=drivesdk
In addition, this project integrates a chatbot that helps users interact with the system and get AI-powered advice about health-related concerns.

## Features

### Disease-Specific Pages
Each disease has a dedicated page providing detailed information about it, including:

- **Overview**: A brief explanation of the disease.
- **Symptoms**: Common signs and indicators of the disease.
- **Prediction Models**: Information about the AI model used and the required input parameters.

### Prediction Page
On the prediction page, users can input their health metrics (such as age, weight, medical history, etc.) to receive an AI-based prediction about their likelihood of developing any of the listed diseases.

### Chatbot Integration
The chatbot is powered by **Ollama**, an AI model that interacts with users, answering questions, offering advice, and assisting with predictions.

## Libraries and Tools Used

- **Flask**: A lightweight framework for backend web development.
- **Scikit-learn & TensorFlow**: Libraries used for training and deploying machine learning models for disease prediction.
- **SQLAlchemy**: ORM (Object-Relational Mapping) library for managing the application's database.
- **Ollama**: AI-powered chatbot model that interacts with users and provides advice.

## Setting Up Ollama for Chatbot Integration

### Step 1: Install Ollama
To run the chatbot feature, you need to have the **Ollama** client installed on your local machine. You can download Ollama from their official site or install it using the following command (if you have `homebrew` installed on macOS):

```bash
brew install ollama
```

For other platforms, please refer to the [Ollama installation guide](https://ollama.com/docs).

### Step 2: Set Up the `.gguf` Model File
The Ollama chatbot system uses `.gguf` model files. Make sure the necessary `.gguf` model file(s) are available in your working directory.

1. Download or copy the `.gguf` model file to your project directory (e.g., `chatbot_model.gguf`).
   
   - `.gguf` is a format used by Ollama to store machine learning models.
   - The model file should be compatible with the Ollama client, and it should be trained to handle health-related queries.

2. Ensure the model file path is correctly referenced in your application.

### Step 3: Run the Chatbot Server Using the `.gguf` Model File

Once you have the `.gguf` model file set up, you can run the chatbot server by executing the following commands from your project folder:

```bash
# Run Ollama with the specific .gguf model file
ollama run --model health_chatbot.gguf
```

This will load the `.gguf` model and start the chatbot server. The chatbot will then be available to interact with users through the Flask web application.

## How to Run the Web Application

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/Healthcare-AI-WebApp.git
cd Healthcare-AI-WebApp
```

### Step 2: Install Dependencies
It's recommended to use a virtual environment. Install the required libraries by running:
```bash
pip install -r requirements.txt
```

### Step 3: Start the Application
To start the Flask development server and load the chatbot integration, run:

```bash
python app.py
```

You should now be able to interact with the web application and the chatbot via `http://127.0.0.1:5000` in your browser.

## Contributing

If you would like to contribute to this project, please fork the repository and create a pull request with your changes. Any improvements to the models, UI, or documentation are welcome!



---

### Notes

- The `.gguf` model file should be set up to respond to health-related queries in a conversational manner. You can tweak the model file or use different versions based on your requirements.
- Ensure that your Ollama installation is working properly before trying to run the chatbot.
- If you face any issues with the Ollama client, check the logs for debugging or consult the [Ollama documentation](https://ollama.com/docs).

