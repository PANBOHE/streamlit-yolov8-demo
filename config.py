from pathlib import Path
import sys

# 01 Bassic settings
# Get the absolute path of the current file
FILE = Path(__file__).resolve()
# Get the parent directory of the current file
ROOT = FILE.parent
# Add the root path to the sys.path list if it is not already there
if ROOT not in sys.path:
    sys.path.append(str(ROOT))
# Get the relative path of the root directory with respect to the current working directory
ROOT = ROOT.relative_to(Path.cwd())

# 02 Streamlit Sources Settings
IMAGE = '图像识别'
VIDEO = '视频识别'
WEBCAM = 'Webcam流接入'
RTSP = 'RTSP流接入'


SOURCES_LIST = [IMAGE, VIDEO, WEBCAM, RTSP]

# 03 Images config Settings
IMAGES_DIR = ROOT / 'data/images'
DEFAULT_IMAGE = IMAGES_DIR / 'data/demo.jpeg'
DEFAULT_DETECT_IMAGE = IMAGES_DIR / 'deta/demores.jpeg'

# 04 Videos config Settings
VIDEO_DIR = ROOT / 'data/videos'
VIDEOS_DICT = {
    'video_1': VIDEO_DIR / 'video_1.mp4',
    'video_2': VIDEO_DIR / 'video_2.mp4',
    'video_3': VIDEO_DIR / 'video_3.mp4',
}

# 05 Model settings
# MODEL_DIR = ROOT 
# DETECTION_MODEL = MODEL_DIR / 'yolov8n.pt'
# SEGMENTATION_MODEL = MODEL_DIR / 'yolov8n-seg.pt'
DETECTION_MODEL ='E:\\weights\\yolov8n.pt'
SEGMENTATION_MODEL = "yolov8n-seg.pt"


# Other information 
# ...