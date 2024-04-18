from flask import Flask, Response, request, render_template
import cv2
# Import your processing and threshold functions
from processing.process_frame import ProcessFrame
from processing.thresholds import get_thresholds_squat, get_thresholds_bicepCurls, get_thresholds_shoulderPress, get_thresholds_dumbbellLateralRaises
from processing.utils import get_mediapipe_pose

app = Flask(__name__)

# Global variable to store the selected exercise and its thresholds
selected_exercise = None
thresholds = None
pose = get_mediapipe_pose()


@app.route('/')
def index():
    return render_template('exercise.html')


@app.route('/select_exercise', methods=['POST'])
def select_exercise():
    global selected_exercise, thresholds
    selected_exercise = request.form.get('exercise')

    # Determine thresholds based on the selected exercise
    if selected_exercise == 'squat':
        thresholds = get_thresholds_squat()
    elif selected_exercise == 'bicep curls':
        thresholds = get_thresholds_bicepCurls()
    elif selected_exercise == 'Shoulder Press':
        thresholds = get_thresholds_shoulderPress()
    elif selected_exercise == 'Dumbell lateral raises':
        thresholds = get_thresholds_dumbbellLateralRaises()
    else:
        thresholds = None

    return render_template('exercise.html', selected_exercise=selected_exercise)


@app.route('/video_feed')
def video_feed(pose):
    return Response(process_video(pose),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


def process_video(pose):
    global selected_exercise, thresholds
    if not selected_exercise or not thresholds:
        pass

    cap = cv2.VideoCapture(0)
    process_frame = ProcessFrame(
        thresholds=thresholds)

    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            processed_frame = process_frame.process(frame, pose)
            ret, buffer = cv2.imencode('.jpg', processed_frame)
            frame = buffer.tobytes()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


if __name__ == '__main__':
    app.run(debug=True)
