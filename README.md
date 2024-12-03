### **Image Optimizer Toolset** 🖼️⚡

A powerful and efficient toolset for compressing and converting images to the WebP format, tailored for developers and web enthusiasts who aim to optimize their website's performance by reducing image sizes without compromising quality. 🚀

---

### **Features** ✨
- **Image Compression:** 🗜️ Leverages the [TinyPNG API](https://tinypng.com/developers) to compress `.jpg`, `.jpeg`, and `.png` images effectively.  
- **WebP Conversion:** 🔄 Converts compressed images to the WebP format using the `Pillow` library, ensuring optimal file sizes for modern web usage.  
- **Customizable Settings:** ⚙️ Easily configure API keys, quality levels, and input/output directories through a centralized `config.py` file.  

---

### **Installation** 🛠️

#### **Prerequisites** 📝
1. **Python 3.7+**  
   Ensure Python is installed on your system.  
   To check your version:  
   ```bash
   python --version
   ```
2. **TinyPNG API Key** 🗝️  
   Sign up at [TinyPNG Developers](https://tinypng.com/developers) to obtain an API key.

---

#### **Step 1: Clone the Repository**  
```bash
git clone https://github.com/alireza-tahriri-masule/image-optimizer-toolset.git
cd image-optimizer-toolset
```

---

#### **Step 2: Create a Virtual Environment (Optional but Recommended)** 🌱
```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

---

#### **Step 3: Install Dependencies** 📦  
Install all required libraries using the `requirements.txt` file:  
```bash
pip install -r requirements.txt
```

---

#### **Step 4: Configure the Project** 🔧
1. Open the `config.py` file.
2. Add your TinyPNG API key to the `TINIFY_API_KEY` variable:
   ```python
   TINIFY_API_KEY = "your-api-key-here"
   ```
3. Update the quality level or directory paths if needed.

---

### **Usage** 🎬

#### **Step 1: Compress Images** 🖼️🗜️  
To compress all images in the `input_images` directory and save them to the `compressed_images` directory, run:  
```bash
python compress_images.py
```

#### **Step 2: Convert Images to WebP** 🌐  
To convert the compressed images to WebP format and save them to the `webp_images` directory, run:  
```bash
python convert_to_webp.py
```

---

### **Project Structure** 📁
```plaintext
image-optimizer-toolset/
├── input_images/         # 📸 Directory for original images
├── compressed_images/    # 📦 Directory for compressed images
├── webp_images/          # 🌍 Directory for WebP images
├── compress_images.py    # 🗜️ Script for compressing images
├── convert_to_webp.py    # 🔄 Script for converting images to WebP
├── config.py             # ⚙️ Configuration file for settings
├── requirements.txt      # 📋 List of dependencies
└── README.md             # 📚 Project documentation
```

---

### **Dependencies** 📚
The project relies on the following Python libraries:
- **`tinify`** 🗜️: For interacting with the TinyPNG API.
- **`Pillow`** 🎨: For processing and converting images.

To install these dependencies:  
```bash
pip install -r requirements.txt
```

---

### **Example Workflow** 🛠️
1. Place your images in the `input_images` folder. 📸  
2. Run `compress_images.py` to compress the images. 🗜️  
3. Run `convert_to_webp.py` to convert the compressed images to WebP format. 🔄  
4. Check the `compressed_images` and `webp_images` directories for the output. 📂

---

### **License** 📜
This project is open-source and available under the MIT License. 🎉

---

### **Contributing** 🤝
Feel free to fork the repository, make improvements, and submit pull requests. Any contributions are welcome! 💡
