
from pathlib import Path
import PIL
# from PIL import Image
import streamlit as st


import config
import helper

# Setting page layout
st.set_page_config(
    page_title="Yolo系列demo展示",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main page heading
st.title("YoloV8 Demo")

# Sidebar
st.sidebar.header("模型设置")

# Model Options
model_type = st.sidebar.radio(
    "模式选择", ['检测', '分割'])

confidence = float(st.sidebar.slider(
    "设置置信度", 25, 100, 40)) / 100

# Selecting Detection Or Segmentation
if model_type == '检测':
    # model_path = Path(config.DETECTION_MODEL)
    model_path = "yolov8n.pt"
elif model_type == '分割':
    model_path = Path(config.SEGMENTATION_MODEL)

# Load Pre-trained ML Model
try:
    model = helper.load_model(model_path)
except Exception as ex:
    st.error(f"Unable to load model. Check the specified path: {model_path}")
    st.error(ex)

st.sidebar.header("影像相关设置")
source_radio = st.sidebar.radio(
    "请选择视频源", config.SOURCES_LIST)

source_img = None
# If image is selected
if source_radio == config.IMAGE:
    source_img = st.sidebar.file_uploader(
        "请上传图片", type=("jpg", "jpeg", "png", 'bmp', 'webp'))

    col1, col2 = st.columns(2)

    with col1:
        try:
            if source_img is None:
                default_image_path = str(config.DEFAULT_IMAGE)
                default_image = PIL.Image.open(default_image_path)
                st.image(default_image_path, caption="默认图片",
                         use_column_width=True)
            else:
                uploaded_image = PIL.Image.open(source_img)
                st.image(source_img, caption="上传图片",
                         use_column_width=True)
        except Exception as ex:
            st.error("Error occurred while opening the image.")
            st.error(ex)

    with col2:
        if source_img is None:
            default_detected_image_path = str(config.DEFAULT_DETECT_IMAGE)
            default_detected_image = PIL.Image.open(
                default_detected_image_path)
            st.image(default_detected_image_path, caption='图像检测',
                     use_column_width=True)
        else:
            if st.sidebar.button('图像检测'):
                res = model.predict(uploaded_image,
                                    conf=confidence
                                    )
                boxes = res[0].boxes
                res_plotted = res[0].plot()[:, :, ::-1]
                st.image(res_plotted, caption='图像检测',
                         use_column_width=True)
                try:
                    with st.expander("图像检测结果"):
                        for box in boxes:
                            st.write(box.data)
                except Exception as ex:
                    # st.write(ex)
                    st.write("No image is uploaded yet!")

elif source_radio == config.VIDEO:
    helper.play_stored_video(confidence, model)

elif source_radio == config.WEBCAM:
    helper.play_webcam(confidence, model)

elif source_radio == config.RTSP:
    helper.play_rtsp_stream(confidence, model)

elif source_radio == config.YOUTUBE:
    helper.play_youtube_video(confidence, model)

else:
    st.error("Please select a valid source type!")