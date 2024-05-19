



# <p align="center"> Genie AI 💡</p>

An AI chatbot with Gemini API to assist in your daily usege of linux insated of RTFM 😉

# Installation


## Automated setup

Setuping the app on your machine

  #### pre steps
  
  1. download the repo
  
  ```bash
  git clone https://github.com/MicklSam/Genie-AI/blob/main/genie.py
  ```
  
  2. Run the installer file named "genie.py"
  ```bash
  ./genie.py
  ```
#### Get your own API key
 3. You will be asked for the api key. to get the key go to : 
  	 1. [Get API key | Google AI Studio](https://aistudio.google.com/app/apikey)
     2. click on `Create API KEY` button
  	 3. generate a new project if needed or select a previous google cloud project.
  	 4. Copy the api key Showen on the popup dialog
  	 
  	Also check the steps on the detailed images below
  <br/><br/><br/><br/>
  
  #### detailed images
    
    1. click on `Create API KEY` button
![1]![6](https://github.com/MicklSam/Genie-AI/assets/99088245/f06d8309-728a-400a-87f3-7f9ad6efe611)

    
    2. generate a new project if needed or select a previous google cloud project.
![2]![11](https://github.com/MicklSam/Genie-AI/assets/99088245/f1dac484-58a3-45fe-9134-fece70b0ec26)

    
  
  
  4. A Geny will spawn on your machine granting you infinite number of wishes ;)

## How to use
all you need is to call `geny` and your wishes will be granted ✨

#### examples:

1.
```bash
geny how to create a new directory?
```
###### output
```bash
mkdir directory_name
```
2.
```bash
geny how to list files in a directory?
```
###### output
```txt
ls
```

3.
```bash
geny how to copy files and directories?
```
###### output
```txt
cp [options] source destination
```
4.
```bash
geny What is 5 + 5?
```
###### output
```txt
Your question is off-topic for this assistant. I can only help with questions about Linux bash commands.
```

# <p align="center">Genie 🧞 and the project. </p>

## Manual setup

step by step how to create and the code explanations

1. First of all this is the python main logic code

```py
import requests
import json
import sys

# Replace with your actual API key
API_KEY = "AIzaSyCfc0ej_s8AKNiIFccX0P0Vk_gjvcsxPak"

if len(sys.argv) > 1:
    user_input = sys.argv[1]
else:
    print("No input text provided.")
    exit()

# Define the URL of the API endpoint
url = f"https://generativelanguage.googleapis.com/v1beta2/models/text-bison-001:generateText?key={API_KEY}"

# Prepare the data to be sent
data = {
    "prompt": {
        "text": user_input
    }
}

# Set headers with content type as JSON
headers = {"Content-Type": "application/json"}

# Send POST request with headers and data
response = requests.post(url, headers=headers, json=data)

# Check for successful response
if response.status_code == 200:
    try:
        response_data = response.json()
        # Fetch the generated content
        generated_text = response_data.get('candidates', [{}])[0].get('output', 'No output found.')

        # Check if the response contains a numerical result
        if generated_text.strip().isdigit():
            print("Genie: I’m sorry, I only answer bash specific questions.")
        else:
            # Print the response
            print(f"Genie: {generated_text.strip()}")
    except (KeyError, IndexError, json.JSONDecodeError) as e:
        print(f"Error parsing response: {e}")
else:
    print(f"Error: {response.status_code} - {response.text}")
```

<br/>
<br/>

The logic behind keeping genie only in the topic of bash commands is by passing a pre prompt that engineers the output for a specific case

```py
text="Help with any question I ask about Linux bash commands only in very summarized answer with a short example usage and don't add any markdown styling make sure all the output you give is pair text. other wise if my question is off topic please only answer politely by refusing to answer this question. So my questions is : "+" ".join(sys.argv[1:])
```
<br /><br /><br />
2. Now about how to convert the normal python code into a ready to install application for any Debian based Linux disruptions
by copying the above code don't forget to set your own API key [in this step](#get-your-own-api-key)
and set it in a file named `genie.py`
get the path of the file
```bash
pwd ./genie.py
```
copy the output and add `/genie.py` at the end of it
```bash
pwd genie

/home/<usrName>
```
thus the path is : 
`/home/<usrName>/genie.py`
copy it and keep it for the next step.

do the following 
```bash
nano ~/.bashrc
```

this will open a file for you in which go to `last line` in the file and add the following : 
```bash
alias genie='python3 /home/<usrName>/genie.py'
```

Now you are behind one step from the glow!
update the new settings for the system to read by doing : 
```bash
source ~/.bashrc
```
<br />

<h1 align="center">that's it 👀</h1>

