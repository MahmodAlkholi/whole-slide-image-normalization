# whole-slide-image-normalization
whole slide image analysis using TIA-TOOLBOX

PEX Platform.AI for Pathology
PEX Platform.AI for Pathology is a web-based tool designed to facilitate the visualization and stain normalization of Whole Slide Images (WSIs). The application allows pathologists, researchers, and healthcare professionals to explore and analyze pathology slides, extract regions of interest, and apply stain normalization techniques to enhance tissue sample analysis.

Table of Contents
Features
Technologies Used
Requirements
Installation
Usage
WSI Upload
Region of Interest Selection
Stain Normalization
Interactive Zoom and Pan
File Structure
Future Improvements
License
Contact
Features
WSI Upload: Supports multiple slide formats like .tif, .svs, and .ndpi, commonly used in digital pathology.
Dynamic Region Selection: Users can interactively select specific regions of the slide to zoom into and visualize based on coordinates and dimensions.
Power and Resolution Control: Fine-tune image magnification and resolution using dynamic sliders.
Stain Normalization: Leverages the Vahadane stain normalization algorithm to correct color variances in tissue stains, enhancing visual consistency across different images.
Thumbnail Preview: Generates and displays a thumbnail image of the entire slide, providing a quick overview of the WSI.
Interactive Image Exploration: Utilizes Plotly's interactive controls to zoom, pan, and select regions of interest within the normalized slide.
Comprehensive Error Handling: Detects and alerts users if the selected region is invalid (e.g., too uniform), preventing processing issues.
Target-Based Normalization: Applies stain normalization based on a pre-defined target image, ensuring consistency in the normalization process.
Dynamic Data Visualization: Visualize the WSI region dynamically, and interactively explore pathology images using hover-over pixel data with enhanced zooming.
Technologies Used
Streamlit: Framework for creating the web-based user interface.
TIA Toolbox: Toolkit for reading, visualizing, and analyzing whole slide images (WSIs).
NumPy: Library for numerical computation and image data manipulation.
Matplotlib: Used internally for various image-related tasks.
Plotly: Interactive plotting library used to enable advanced zooming, panning, and region selection in the image visualization.
Python Imaging Libraries: For reading and manipulating images.
Requirements
Python 3.x
Required Python packages:
bash
Copy code
pip install streamlit matplotlib numpy plotly tiatoolbox
Additional Dependencies
TIA Toolbox: The tiatoolbox package is required to work with WSIs. It can be installed via pip.
Tempfile: Python’s tempfile module is used for handling file uploads and storing them temporarily for processing.

Usage
WSI Upload
Use the Upload Image button to upload a pathology slide. Supported formats include .tif, .svs, and .ndpi.
Once uploaded, the application processes the slide and provides access to the slide's metadata.
Region of Interest Selection
Dynamically select the X and Y coordinates of the region you wish to visualize using interactive sliders.
Adjust the region size (width and height) to define the specific area of interest for detailed analysis.
Stain Normalization
Vahadane Stain Normalization is applied to adjust color discrepancies across samples by normalizing the stain using a pre-configured target image.
Users can select regions of the image for stain normalization based on the X, Y coordinates and dimensions.
Interactive Zoom and Pan
Once the stain normalization is applied, users can interactively zoom, pan, and explore the normalized slide region using Plotly.
Plotly controls provide enhanced exploration capabilities, such as hovering over pixels to get detailed information and dynamically adjusting the view.
Example Workflow
Upload: Upload your WSI in .tif, .svs, or .ndpi format.
Explore: Use the interactive sliders to select a region of interest and visualize a sample.
Normalize: Apply stain normalization to enhance the region of interest.
Interact: Use Plotly's zoom and pan features to explore the normalized region in detail
