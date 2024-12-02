

# AI Self-Diagnosis Tool - Healthcare-AI-WebApp

The **Healthcare-AI-WebApp** leverages Artificial Intelligence (AI) to enhance healthcare by predicting the likelihood of various diseases based on user input. The web application uses machine learning and deep learning techniques to assess the risk of the following diseases:

- **Lung Disease**
- **Heart Disease**
- **Diabetes**

## Features

### Disease-Specific Pages
Each disease has a dedicated page providing detailed information about it, including:

- **Overview**: A brief explanation of the disease.
- **Symptoms**: Common signs and indicators of the disease.
- **Prediction Models**: Information about the AI model used and the required input parameters.

### Prediction Page
On the prediction page, users can input their health metrics (such as age, weight, medical history, etc.) to receive an AI-based prediction about their likelihood of developing any of the listed diseases.

## Libraries and Tools Used

- **Flask**: A lightweight framework for backend web development.
- **Scikit-learn & TensorFlow**: Libraries used for training and deploying machine learning models.
- **SQLAlchemy**: ORM (Object-Relational Mapping) library for managing the application's database.

## How to Run the Project

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
Run the following command to start the Flask development server:
```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser to access the web application.

## Contributing

If you would like to contribute to this project, please fork the repository and create a pull request with your changes. Any improvements to the models, UI, or documentation are welcome!

## License

This project is open-source


