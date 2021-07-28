from flask import Flask,render_template,Response
import cv2
from pixellib.instance import instance_segmentation
import numpy
app=Flask(__name__)
camera = cv2.VideoCapture(0)

def gen_frame():
    while True:
        success, frame= camera.read()
        if not success:
            break
        else:
            segment_image = instance_segmentation()
            segment_image.load_model("mask_rcnn_coco.h5")
            result = segment_image.segmentFrame(frame, show_bboxes=True)
            image = result[1]
            cv2.imshow("image segmentation", image)
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'b'content-type:image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/vide_feed')
def video_feed():
    return Response(gen_frame(),mimetype='multipart/x-mixed-replace;boundary=frame')

if __name__=="__main__":
    app.run(debug=True)