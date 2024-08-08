import streamlit as st
 

source = ("图片检测", "视频检测")
source_index = st.sidebar.selectbox("选择输入", range(
    len(source)), format_func=lambda x: source[x])

if source_index == 0:
    uploaded_file = st.sidebar.file_uploader(
        "上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file is not None:
        is_valid = True
        with st.spinner(text='资源加载中...'):
            st.sidebar.image(uploaded_file)
            # picture = Image.open(uploaded_file)
            # picture = picture.save(f'data/images/{uploaded_file.name}')
            # opt.source = f'data/images/{uploaded_file.name}'
    else:
        is_valid = False
else:
    uploaded_file = st.sidebar.file_uploader("上传视频", type=['mp4'])
    if uploaded_file is not None:
        is_valid = True
        with st.spinner(text='资源加载中...'):
            st.sidebar.video(uploaded_file)
            with open(os.path.join("data", "videos", uploaded_file.name), "wb") as f:
                f.write(uploaded_file.getbuffer())
            opt.source = f'data/videos/{uploaded_file.name}'
    else:
        is_valid = False

if is_valid:
    print('valid')
    if st.button('开始检测'):

        #detect(opt)

        if source_index == 0:
            with st.spinner(text='Preparing Images'):
                # for img in os.listdir(get_detection_folder()):
                #     st.image(str(Path(f'{get_detection_folder()}') / img))

                st.balloons()
        else:
            with st.spinner(text='Preparing Video'):
                # for vid in os.listdir(get_detection_folder()):
                #     st.video(str(Path(f'{get_detection_folder()}') / vid))

                st.balloons()