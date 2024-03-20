#mediapipe  ObjectDetecttion -> overview -> lite2



import cv2

BaseOptions =mp.tasks.BaseOptions
ObjectDetector=mp.tasks.vision.ObjectDetector
ObjectDetectorOptions=mp.tasks.vison.ObjectDetectorOptions
VisionRunningMode=mp.tasks.vision.RunningMode

options=ObjectDetectorOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    max_results=5,
    running_mode=VisionRunningMode,IMAGE)


cap=cv2.VdeoCapture("dance.mp4")

with ObjectDetector.reate_from_options(options)as detector:
    while cap. isOpened():
        ret.frame =cap.read()
        if ret:
            image =cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            mp_image = mp.image(image_format=mp.imageFormat.SRGB, data=image)
            detection_result =detector.detect(mp_image)
            annotated_image-visualize(frame.detection_result)
            cv2.imshow('Frame',annotated_image)
            if cv2.waitKey(5) == ord('q')