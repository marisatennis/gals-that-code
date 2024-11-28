**Made up You!**
==============================================================

### **Objectives**

By completing this challenge, you will:

*   Learn to handle **collections** and dynamically display them on the front-end.
    
*   Use **Flask** to process user inputs and integrate with OpenAI GPT for creative outputs.
    
*   Understand how to use **embed URLs** to display dynamic content (GIFs and Spotify tracks).
    
*   Build a fully interactive and personalized web application using HTML, JavaScript, and Python.
    

### **Task Description**

In this challenge, you’ll build a fun, interactive web app that:

1.  Asks users to input details about themselves (name, favorite hobby, dream setting, sidekick and any other thing you'd like to add!).
    
2.  Uses OpenAI GPT to generate based on the user’s input:
    
    *   Three unique one paragraph made up stories about them .
        
    *   Three GIF IDs (to embed GIFs from Giphy).
        
    *   Three Spotify track IDs (to embed songs from Spotify).
        
3.  Dynamically displays these collections on the front-end, allowing users to:
    
    *   Navigate through the options using "Next" and "Previous" buttons.
        
    *   Select their favorite story, GIF, and song.
        
4.  Displays a confirmation message once the user has made their selections.
    

### **Setup Instructions**

1.  Install your libraries:
```
pip install flask, openai, requests
```
    
2.  **Set Up API Keys:**
    
    *   **OpenAI API Key:** Get your API key from [OpenAI](https://platform.openai.com/). You will need an account and create a project and a key. There is a free version but you might need to pay ~£2 for usage if you run out. 
        
    *   **Giphy Embed Base URL:** No API key required, but ensure GPT generates valid GIF IDs.
    ```https://giphy.com/embed/{giphy_id}"```
        
    *   **Spotify Embed Base URL:** No API key required, but ensure GPT generates valid track IDs.
    ```"https://open.spotify.com/embed/track/{}?utm_source=generator"```
        
3.  Folder Structure: Your project should look like this:

```
project/
├── app.py  # Flask back-end
├── templates/
│   └── index.html  # Front-end HTML
├── static/
│   └── script.js  # Front-end JavaScript
    ├── styles.css  # Optional styling
└── requirements.txt

```
    
4.  Run the Flask App: Start the Flask server:
```
python app.py
```

    
5.  **Access the App:** Open your browser and go to http://127.0.0.1:5000.
    

### **Instructions**

#### **Step 1: Define a Class for the Outputs**

*   Create a class in app.py called GeneratedContent to store the three stories, three GIF IDs, and three Spotify track IDs.
    
*   Add methods to:
    
    *   Retrieve all stories, GIF URLs, and Spotify embed URLs.
        
    *   Format the outputs for easier use in the front-end. Some ideas below:

```
def get_story(self, index)

def get_gif_url(self, index)

def get_spotify_url(self, index)
```

#### **Step 2: User Input Form**

*   Create a form in index.html that asks the user for:
    
    *   Their name
        
    *   Their favorite hobby
        
    *   Their dream setting
        
    *   Their sidekick

    *   Any other thing
        
*   Add a submit button to send the form data to the Flask back-end.

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Story Picker</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Create Your Story</h1>
    
    <!-- User Input Form -->
    <form id="story-form" onsubmit="fetchData(); return false;">
       ...
    </form>
    
    <!-- Output Section -->
    <div id="output" style="display: none;">
        <h2>Your Story</h2>
       ...
    </div>

    <!-- Confirmation Section -->
    <div id="confirmation">
        
    </div>

    <script src="script.js"></script>
</body>
</html>

```
    

#### **Step 3: Use the Class in the Flask Back-End**
*   In app.py, use the GeneratedContent class to structure the output.
*   Generate three stories, three GIF IDs, and three Spotify track IDs using OpenAI GPT. Starter below:

```
from flask import Flask, request, render_template
import openai

app = Flask(__name__)

openai.api_key = 'your-openai-api-key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-content', methods=['POST'])
def generate_content():
    # get inputs from front end form

    # Generate three stories
    prompt = # write your prompt using the user inputs
 
    response = # write your open ai call here

    # Create an instance of the GeneratedContent class with the response

    # Return data to the front-end


if __name__ == '__main__':
    app.run(debug=True)

```
    
    
    

#### **Step 4: Front-End Navigation**

Use javascript to dynamically interact through the generated content by gpt.

*   In script.js, write functions to:
    
    *   Dynamically display one story, GIF, and song at a time.
        
    *   Allow users to navigate through the collections using "Next" and "Previous" buttons.
        
    *   Let users select their favorite from collection with a "Pick This!" button.
        
*   Display a confirmation message after all selections are made. Some Example code below:

```
// Variables to hold the collection of combined outputs
let collections = [];
let currentIndex = 0; // Track the current collection being displayed

// Fetch data from the back-end and initialize the collections
async function fetchData() {
    const formData = # get data from form
    const response = # send data to back end function to get the generated content
    const data = await response.json(); get the data

    // Combine each story, GIF, and Spotify track into a single collection
    for (let i = 0; i < data.stories.length; i++) {
      ...
    }

    // Display the first collection
    updateDisplay();
}

// Update the display with the current collection
function updateDisplay() {
   ...
}

// Navigate to the next collection
function next() {
    ...
}

// Navigate to the previous collection
function previous() {
    ...
}

// Handle selection of the current collection
function select() {
   ...
}


```

#### **Step 5: Style the Page**

*   Use CSS to make the app visually appealing. Add animations or transitions to the "Next" and "Previous" buttons for extra flair.
   
### **Deliverables**

1.  A working Flask app that:
    
    *   Displays three options for each output (story, GIF, song).
        
    *   Lets users navigate and select their favorite from each collection.
        
    *   Displays a confirmation message after selections.
        