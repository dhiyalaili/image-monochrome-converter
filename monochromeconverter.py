from pathlib import Path
import streamlit as st
from PIL import Image, ImageOps
import numpy as np

def rgb_to_monochrome(image):
    # Convert image to grayscale
    grayscale = image.convert("L")
    return grayscale

# Constants
MAX_FILES = 10
ALLOWED_TYPES = ["png", "jpg", "jpeg"]

# Set up page configuration
st.set_page_config(page_title="Final Project Linear Algebra Group 2 - IE 2023 Class 3")

def hide_streamlit_style():
    """Applies custom styles to the Streamlit app."""
    st.markdown(
        """
        <style>
        body {
            font-family: Arial, sans-serif;
        }
        .block-container {
            padding: 2rem;
        }
        header {
            visibility: hidden;
        }
        footer {
            visibility: hidden;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Function to resize and pad images
def resize_and_pad(image, target_size=(300, 300), color=(255, 255, 255)):
    """Resize and pad an image to the target size while maintaining aspect ratio."""
    return ImageOps.pad(image, target_size, color=color)

# Hide default styles and apply custom styles
hide_streamlit_style()

# Add a place for a top logo or image at the top of all pages
top_image_path = Path("logo pu.png")  # Ganti dengan path gambar logo Anda
if top_image_path.exists():
    st.image(str(top_image_path), use_container_width=True)
else:
    st.warning("Top image not found.")

# Navigation menu
menu = st.sidebar.selectbox("Select a Page", ["Home", "Group Members", "Monochrome Converter"])

if menu == "Home":
    # Content for the home page
    st.markdown("<h1>Final Project Linear Algebra Group 2 - Class 3</h1>", unsafe_allow_html=True)
    st.markdown("<h2>Welcome to Image Monochrome Converter</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        Instruksi untuk menggunakan fitur Monochrome Converter:
        1. Unggah gambar dengan format **PNG**, **JPG**, atau **JPEG**.
        2. Anda dapat mengunggah hingga 10 gambar sekaligus.
        3. Tekan tombol **Monochrome Converter** pada menu untuk memproses gambar.
        4. Setelah diproses, unduh gambar yang telah selesai diconvert.
        """,
        unsafe_allow_html=True,
    )

elif menu == "Group Members":
    # Mapping names to image paths and roles
    anggota = [
        {"name": "Angelina Nesya Tanly", "image": "angel.jpg", "SID": "004202300074"},
        {"name": "Atika Mardatila", "image": "atika.jpg", "SID": "004202300051"},
        {"name": "Dhiya Laili Azizah Pancawati", "image": "dhiya.jpg", "SID": "004202300082"},
        {"name": "Mahanani Indah Marttaningrum", "image": "arum.jpg", "SID": "004202300043"},
    ]

    st.markdown("<h2 style='text-align: center;'>Group Members - Group 2</h2>", unsafe_allow_html=True)

    # Display members in a grid-like format
    col1, col2, col3, col4 = st.columns(4)  # Adjust column layout if needed
    columns = [col1, col2, col3, col4]

    for idx, member in enumerate(anggota):
        with columns[idx % 4]:
            image_path = Path(member["image"])
            if image_path.exists():
                original_image = Image.open(image_path)
                resized_image = resize_and_pad(original_image, target_size=(300, 300))  # Adjust size
                st.image(resized_image, caption=member["name"], use_container_width=False)
                st.markdown(
                    f"<p style='text-align: center;'>{member['SID']}</p>",
                    unsafe_allow_html=True,
                )
            else:
                st.warning(f"Image for {member['name']} not found: {member['image']}")

elif menu == "Monochrome Converter":
    # Streamlit app
    st.title("Image Monochrome Converter")
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
    # Open image
        image = Image.open(uploaded_file)
        st.image(image, caption="Original Image", use_container_width=True)

    # Convert to monochrome
        monochrome_image = rgb_to_monochrome(image)
        st.image(monochrome_image, caption="Monochrome Image", use_container_width=True)

    # Download button
        monochrome_array = np.array(monochrome_image)
        monochrome_image.save("monochrome_image.png")
        with open("monochrome_image.png", "rb") as file:
            st.download_button(
                label="Download Monochrome Image",
                data=file,
                file_name="monochrome_image.png",
                mime="image/png",
            )
