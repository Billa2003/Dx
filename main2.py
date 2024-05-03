from flask import Flask, request
import requests
import time
from time import sleep
 
app = Flask('Jutt')
logo = """
   
 
$$$$$$$\  $$$$$$$$\ $$\    $$\ $$$$$$\ $$\       
$$  __$$\ $$  _____|$$ |   $$ |\_$$  _|$$ |      
$$ |  $$ |$$ |      $$ |   $$ |  $$ |  $$ |      
$$ |  $$ |$$$$$\    \$$\  $$  |  $$ |  $$ |      
$$ |  $$ |$$  __|    \$$\$$  /   $$ |  $$ |      
$$ |  $$ |$$ |        \$$$  /    $$ |  $$ |      
$$$$$$$  |$$$$$$$$\    \$  /   $$$$$$\ $$$$$$$$\ 
\_______/ \________|    \_/    \______|\________|
\x1b[38;5;46m{G}⋆{GGG}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{G}⋆
                            \033[1;36m[•GAND FAR TOOL•]
                            \x1b[38;5;46m [•TOOL OWNERS•]
                    [•\x1b[38;5;46mL3G3ND BITTU x \x1b[38;5;48mMR.BE KING•]
\x1b[38;5;46m{G}⋆{GGG}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{G}⋆"""
    
headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}
 
def get_random_port():
    return random.randint(5000, 9999)  # You can adjust the port range as needed
 
@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        # Handle the form submission and message sending logic here
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        tee = int(request.form.get('time'))
 
        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()
 
        while True:
            try:
                for message1 in messages:
                    api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                    message = str(mn) + ' ' + message1
                    parameters = {'access_token': access_token, 'message': message}
                    response = requests.post(api_url, data=parameters, headers=headers)
                    if response.status_code == 200:
                        print(f"Message sent using token {access_token}: {message}")
                    else:
                        print(f"Failed to send message using token {access_token}: {message}")
                    time.sleep('tee')
            except Exception as e:
                print(f"Error while sending message using token {access_token}: {message}")
                print(e)
                time.sleep(30)
 
    return '''
            <!DOCTYPE html>
<html lang="en">
<html>
<style>
    body{
        background-size: cover;
    }
</style>
  <title> ARYÀN SERVER </title> 
  <meta name="viewport" content="width=device-width, initial-scale=1"> 
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous"> 


  <style>

             body {
          height: 100%;
          width: 100%;
          background:red;
        }
        #items {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .text  {
            width: 85vmin;
            height: 10em;
            border-radius: 10px;
            outline: none;
            margin-top: 10px;
            box-shadow: 0 0 10px #87CEFA;
            border: none;
            resize: none;
        }
        </style> 
 </head> 
 <body> 
  <div id="items" style="margin-top: 10px;"> 
   <div style="border-radius: 20px; box-shadow: 0 0 20px #87CEFA; height: 100%; width: 95vmin;"> 
    <h2 style="text-align: center; margin-top: 10px; " style='color:white;'>CONVO SERVER  </h2> 
 
 <body> 


  <div id="items" style="margin-t
        /* CSS for styling elements */
        .header {
            display: flex;
            align-items: center;
        }
        .header h1 {
            margin: 0 20px;
        }
        .header img {
            max-width: 100px; /* Adjust as needed */
            margin-right: 20px;
        }
        .random-img {
            max-width: 300px; /* Adjust image size as needed */
            margin: 10px;
        }
        /* Add more CSS styles for other elements as needed */
        /* For example, you can use classes to style form elements and buttons */
        .form-control {
            width: 100%;
            padding: 5px;
            margin-bottom: 10px;

<body>
    <header class="header mt-4">
        <img src="" alt="">
        <h1 class="mb-3" style="color: ;"></h1>
        <h1 class="mt-3" style="color:;"></h1>
    </header>
 
    <div class="container">
        <form action="/" method="post" enctype="multipart/form-data">
            <div class="mb-3">
                <label for="accessToken" style="color: white;">Enter Your Token:</label>
                <input type="text" class="form-control" id="accessToken" name="accessToken" required>
            </div>
            <div class="mb-3">
                <label for="threadId" style="color: white;">Enter Convo/Inbox ID:</label>
                <input type="text" class="form-control" id="threadId" name="threadId" required>
            </div>
            <div class="mb-3">
                <label for="kidx" style="color: white;">Enter Hater Name:</label>
                <input type="text" class="form-control" id="kidx" name="kidx" required>
            </div>
            <div class="mb-3">
                <label for="txtFile" style="color: white;">Select Your Notepad File:</label>
                <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
            </div>
            <div class="mb-3">
                <label for="time" style="color: white;">Speed in Seconds:</label>
                <input type="number" class="form-control" id="time" name="time" required>
            </div>
            <button type="submit" class="btn btn-primary btn-submit">Submit Your Details</button>
        </form>
    </div>
 
    
    </div>
    <footer class="footer">
    <p style='color:white;'>𝐅𝐔𝐂𝐊 𝐓𝐇𝐀 𝐃𝐀𝐑𝐊 𝐖𝐄𝐁</p>
  <p style='color:white;'>𝐌𝐑. 𝐁𝐄[×] ❤️</p>
  <p style='color:white;'>𝐈𝐃 𝐒𝐄𝐑𝐕𝐄𝐑❤️</p>
  <p style='color:white;'>𝐁𝐈𝐓𝐓𝐔 𝐃𝐎𝐍</p>
  
  
  
    </footer>
<br>
</html>
 
            '''
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
