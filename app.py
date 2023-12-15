from flask import Flask, request, render_template 
from PIL import Image

app = Flask(__name__)

# -----------------------------------------    
#             home page
# -----------------------------------------  

@app.route('/')
def index():
    # return "Welcome to my Flask App!"
    return render_template('index.html')

# -----------------------------------------    
#         text-to-text template
# -----------------------------------------  

@app.route('/text2text', methods=['POST'])
def text2text_page1():
    return render_template('text2text.html')

@app.route('/text2text_response', methods=['POST'])
def text2text_page2():
    input = request.form.get('number_input') 

    try:
        if int(input)%2 == 0:
            label = "even"
        else:
            label = "odd"
        return render_template(
            'text2text_response.html', 
            odd_or_even=label, 
            enteredNumber=input
            )
    except:   
        return "Invalid input!"

# -----------------------------------------    
#        image-to-image template
# -----------------------------------------  

@app.route('/image2image', methods=['POST'])
def image2image_page1():
    return render_template('image2image.html')

@app.route('/image2image_response', methods=['POST'])
def image2image_page2():
    input = request.files['file_upload']
    try:
        file = Image.open(input)
        file = file.convert('L')
        file_path = f"static/{input.filename}"
        file.save(file_path)
        return render_template('image2image_response.html', user_image=file_path)
    except:
        return "Image file format is not supported!"
