# 5293_final
Before you read this, please prepare two api keys: Qwen api key and Openai api key. Please add it to .env file in the folder.

Store Qwen api key in DASHSCHOPE_API_KEY, and store Openai api key in OPENAI_API_KEY

```
DASHSCOPE_API_KEY = xxx
OPENAI_API_KEY = xxx
```
and install openai in your environment by running this in your terminal:

```
pip install -r requirements.txt
```

how to run this: 

Option 1: To check, change, debug, or just test the code: First git clone this repository in your local machine. Open the terminal and run this: 

```
cd generate_resume
```
Then run: 
```
python main.py
```

and you will see a small line of phrase asking for your information, and you could input a short paragraph of your own introduction and press ENTER.

Option 2: Want a real interactive interface to use our framework? Run like this: Still git clone this repository to your local machine. Then do: 
```
cd generate_resume
```
Then run: 
```
streamlit run app.py
```
And you can choose to type in your email to receive updated information or just leave it blank. After you press ENTER, the interface will pop up!

Important!!!: For Free form textbox, current supported school include: Columbia University, Harvard, MIT, Stanford, UCBerkeley, and UCDavis. Important!!!: You'd better visualize .env file in the folder generate_resume and input your own Qwen api.
