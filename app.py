from flask import Flask, render_template, request
from chexnet import ChexNet
import os

app = Flask(__name__)
model = ChexNet('weights.h5')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        img = request.files.get('image')
        if img:
            img.save('uploaded_image.png')
            diagnosis = model.predict('uploaded_image.png')
            os.remove('uploaded_image.png')
            diagnosis = dict(zip(conditions, diagnosis))
            return render_template('result.html', diagnosis=diagnosis)
    return render_template('index.html')


conditions = [
    'Atelectasis', 'Cardiomegaly', 'Effusion',
    'Infiltration', 'Mass', 'Nodule', 'Pneumonia',
    'Pneumothorax', 'Consolidation', 'Edema',
    'Emphysema', 'Fibrosis', 'Pleural_Thickening', 'Hernia'
]

if __name__ == '__main__':
    app.run(debug=True)
