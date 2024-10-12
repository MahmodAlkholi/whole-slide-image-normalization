

# import streamlit as st
# import os
# import numpy as np
# import matplotlib.pyplot as plt
# import tempfile
# from tiatoolbox.wsicore import wsireader
# from tiatoolbox import data
# from tiatoolbox.tools import stainnorm
# import plotly.express as px

# st.title('PEX Platform.AI for Pathology')
# st.image("pathology.jpg")

# uploaded_slide = st.file_uploader("UPLOAD IMAGE PLEASE", type=['tif', 'svs', 'ndpi'])

# if uploaded_slide:
#     st.write("Slide uploaded")

#     # Save the uploaded slide to a temporary file and use the path
#     with tempfile.NamedTemporaryFile(delete=False, suffix='.tif') as temp_file:
#         temp_file.write(uploaded_slide.getbuffer())
#         temp_file_path = temp_file.name

#     # Read the whole slide image (WSI)
#     wsi_reader = wsireader.WSIReader.open(input_img=temp_file_path, power=20)

#     # Access the WSI info
#     wsi_info = wsi_reader.info.as_dict()

#     # Dynamically set min and max resolution based on WSI levels
#     min_resolution = wsi_info['level_downsamples'][-1]
#     max_resolution = wsi_info["level_downsamples"][0]

#     power = st.slider("Select power value", min_value=1, max_value=100, value=30)
#     resolution = st.slider("Select resolution value", min_value=min_resolution, max_value=10.0, value=3.0)

#     # Dynamic sliders based on image dimensions
#     location_x = st.slider(f"(L)Select X coordinate for the region(R)", min_value=0, max_value=1000, value=800)
#     location_y = st.slider("(U)Select Y coordinate for the region(D)", min_value=0, max_value=1000, value=1000)
#     size_x = st.slider("Select width of the region", min_value=100, max_value=1500, value=800)
#     size_y = st.slider("Select height of the region", min_value=100, max_value=1500, value=800)

# # Function to check if the image is valid (e.g., not too uniform)
# def is_valid_image(image):
#     if np.ptp(image) < 10:  # ptp = range of values (max - min)
#         return False
#     return True

# # Function to create the image and perform stain normalization
# def create_image(uploaded_slide, power, resolution, location_x, location_y, size_x, size_y):
#     with tempfile.NamedTemporaryFile(delete=False, suffix='.tif') as temp_file:
#         temp_file.write(uploaded_slide.getbuffer())
#         temp_file_path = temp_file.name

#     # Read the whole slide image (WSI)
#     wsi_reader = wsireader.WSIReader.open(input_img=temp_file_path, power=power)

#     # Access the WSI info
#     wsi_info = wsi_reader.info.as_dict()

#     # Display WSI information
#     for key, value in wsi_info.items():
#         st.write(f"{key}: {value}")

#     # Get a thumbnail of the WSI
#     wsi_thumb = wsi_reader.slide_thumbnail(resolution=resolution, units="power")

#     # Read a sample region from the WSI based on user input
#     sample = wsi_reader.read_region(location=[location_x, location_y], level=0, size=[size_x, size_y])
#     sample = np.array(sample).copy()  # Ensure the array is writeable to avoid read-only issues

#     # Check if the sample is valid
#     if not is_valid_image(sample):
#         st.error("Sample image is too uniform or invalid for stain normalization. Try another region.")
#         os.remove(temp_file_path)
#         return

#     # Display the sample region
#     st.image(sample, caption="Sample Image", use_column_width=True)

#     # Stain normalization using the target image
#     target_image = data.stain_norm_target()
#     stain_normalizer = stainnorm.VahadaneNormalizer()

#     try:
#         stain_normalizer.fit(target_image)
#         normed_sample = stain_normalizer.transform(sample)
#     except np.linalg.LinAlgError as e:
#         st.error(f"Error during stain normalization: SVD did not converge. {e}")
#         os.remove(temp_file_path)
#         return
#     except Exception as e:
#         st.error(f"An unexpected error occurred during normalization: {e}")
#         os.remove(temp_file_path)
#         return

#     # Display the original thumbnail
#     st.subheader("Thumbnail")
#     st.image(wsi_thumb, use_column_width=True)

#     # Use Plotly for displaying the normalized sample with zooming capability
#     st.subheader("Normalized Sample with Zoom")

#     # Create a Plotly figure with zoom and pan enabled
#     fig = px.imshow(normed_sample)
#     fig.update_layout(
#         autosize=False,
#         width=800, 
#         height=800,
#         xaxis_title="X Coordinate",
#         yaxis_title="Y Coordinate",
#         dragmode="orbit",
#         hovermode=False
#     )

#     # Display the Plotly figure
#     st.plotly_chart(fig)

#     # Clean up the temporary file
#     os.remove(temp_file_path)

# # Button to trigger the normalization process
# norm_btn = st.button("Normalize the slide")

# # Perform normalization when the button is clicked and a slide is uploaded
# if norm_btn and uploaded_slide:
#     create_image(uploaded_slide, power, resolution, location_x, location_y, size_x, size_y)


import streamlit as st
import os
import numpy as np
import matplotlib.pyplot as plt
import tempfile
from tiatoolbox.wsicore import wsireader
from tiatoolbox import data
from tiatoolbox.tools import stainnorm
import plotly.express as px

st.title('PEX Platform.AI for Pathology')
st.image("pathology.jpg")

uploaded_slide = st.file_uploader("UPLOAD IMAGE PLEASE", type=['tif', 'svs', 'ndpi'])

if uploaded_slide:
    st.write("Slide uploaded")

    # Save the uploaded slide to a temporary file and use the path
    with tempfile.NamedTemporaryFile(delete=False, suffix='.tif') as temp_file:
        temp_file.write(uploaded_slide.getbuffer())
        temp_file_path = temp_file.name

    # Read the whole slide image (WSI)
    wsi_reader = wsireader.WSIReader.open(input_img=temp_file_path, power=20)

    # Access the WSI info
    wsi_info = wsi_reader.info.as_dict()

    # Dynamically set min and max resolution based on WSI levels
    min_resolution = wsi_info['level_downsamples'][-1]
    max_resolution = wsi_info["level_downsamples"][0]

    power = st.slider("Select power value", min_value=1, max_value=100, value=30)
    resolution = st.slider("Select resolution value", min_value=min_resolution, max_value=10.0, value=3.0)

    # Dynamic sliders based on image dimensions
    location_x = st.slider(f"(L)Select X coordinate for the region(R)", min_value=0, max_value=1000, value=800)
    location_y = st.slider("(U)Select Y coordinate for the region(D)", min_value=0, max_value=1000, value=1000)
    size_x = st.slider("Select width of the region", min_value=100, max_value=1500, value=800)
    size_y = st.slider("Select height of the region", min_value=100, max_value=1500, value=800)

# Function to check if the image is valid (e.g., not too uniform)
def is_valid_image(image):
    if np.ptp(image) < 10:  # ptp = range of values (max - min)
        return False
    return True

# Function to create the image and perform stain normalization
def create_image(uploaded_slide, power, resolution, location_x, location_y, size_x, size_y):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.tif') as temp_file:
        temp_file.write(uploaded_slide.getbuffer())
        temp_file_path = temp_file.name

    # Read the whole slide image (WSI)
    wsi_reader = wsireader.WSIReader.open(input_img=temp_file_path, power=power)

    # Access the WSI info
    wsi_info = wsi_reader.info.as_dict()

    # Display WSI information
    for key, value in wsi_info.items():
        st.write(f"{key}: {value}")

    # Get a thumbnail of the WSI
    wsi_thumb = wsi_reader.slide_thumbnail(resolution=resolution, units="power")

    # Read a sample region from the WSI based on user input
    sample = wsi_reader.read_region(location=[location_x, location_y], level=0, size=[size_x, size_y])
    sample = np.array(sample).copy()  # Ensure the array is writeable to avoid read-only issues

    # Check if the sample is valid
    if not is_valid_image(sample):
        st.error("Sample image is too uniform or invalid for stain normalization. Try another region.")
        os.remove(temp_file_path)
        return

    # Display the sample region
    st.image(sample, caption="Sample Image", use_column_width=True)

    # Stain normalization using the target image
    target_image = data.stain_norm_target()
    stain_normalizer = stainnorm.VahadaneNormalizer()

    try:
        stain_normalizer.fit(target_image)
        normed_sample = stain_normalizer.transform(sample)
    except np.linalg.LinAlgError as e:
        st.error(f"Error during stain normalization: SVD did not converge. {e}")
        os.remove(temp_file_path)
        return
    except Exception as e:
        st.error(f"An unexpected error occurred during normalization: {e}")
        os.remove(temp_file_path)
        return

    # Display the original thumbnail
    st.subheader("Thumbnail")
    st.image(wsi_thumb, use_column_width=True)

    # Use Plotly for displaying the normalized sample with enhanced zooming and interactivity
    st.subheader("Enhanced Normalized Sample with Zoom")

    # Create a Plotly figure with zoom, pan, and button controls
    fig = px.imshow(normed_sample, color_continuous_scale='Viridis')  # Use Viridis color scale

    fig.update_layout(
        title="Enhanced Pathology Image",
        xaxis_title="X Axis",
        yaxis_title="Y Axis",
        autosize=False,
        width=800, 
        height=800,
        margin=dict(l=0, r=0, b=0, t=50),
        dragmode="zoom",
        hovermode="closest",  # Closest hover point
        updatemenus=[dict(
            type="buttons",
            direction="left",
            buttons=[
                dict(args=["dragmode", "zoom"], label="Zoom", method="relayout"),
                dict(args=["dragmode", "pan"], label="Pan", method="relayout"),
                dict(args=["dragmode", "select"], label="Select", method="relayout", execute=True)
            ],
            showactive=True,
            x=0.1, y=1.15  # Positioning buttons above the plot
        )]
    )

    # Add hover template for additional information on hover
    fig.update_traces(
        hovertemplate="X: %{x}<br>Y: %{y}<br>Pixel Value: %{z}<extra></extra>"
    )

    # Display the Plotly figure
    st.plotly_chart(fig)

    # Clean up the temporary file
    os.remove(temp_file_path)

# Button to trigger the normalization process
norm_btn = st.button("Normalize the slide")

# Perform normalization when the button is clicked and a slide is uploaded
if norm_btn and uploaded_slide:
    create_image(uploaded_slide, power, resolution, location_x, location_y, size_x, size_y)
