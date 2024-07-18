## Chat with Multiple PDFs using LangChain, Gemini, and Streamlit

This project allows you to have a conversation with the content of multiple uploaded PDF files, leveraging Google's Gemini large language model (LLM) through LangChain. The interactive web interface is built with Streamlit.

### Project Structure

```
└── 📁 utils
    ├── 📄 pdf_handler.py
    └── 📄 embedding_handler.py
📄 app.py
📄 requirements.txt 
📄 .env 
```

- **`app.py`:** The main Streamlit application file. It contains the logic for loading PDFs, processing text, creating embeddings, interacting with Gemini, and displaying the chat interface.
- **`utils/pdf_handler.py`:** Contains functions to extract text from PDF files.
- **`utils/embedding_handler.py`:** Contains functions to split the text into smaller chunks and create embeddings using language models.
- **`requirements.txt`:** Lists the required Python dependencies for the project.
- **`.env`:** File to store environment variables, such as your Google Cloud API key.

### Setup and Run

1. **Enable Google Cloud API and obtain credentials:**
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a project or select an existing one.
   - Enable the **Generative Language API**.
   - Create a service account and download the JSON key.

2. **Set up environment variables:**
   - Create a `.env` file in the root of your project and add the following:
     ```
     GOOGLE_API_KEY="SUBSTITUTE_YOUR_API_KEY_HERE"
     ```

3. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/chat-with-pdfs.git 
   cd chat-with-pdfs
   ```

4. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

5. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

6. **Run the application:**
   ```bash
   streamlit run app.py
   ```

7. **Access the application:** Open your web browser and go to `http://localhost:8501/`.

### Usage

1. **Upload PDFs:** Use the file upload widget in the sidebar to upload one or more PDF files.
2. **Process:** Click the "Process" button to extract text from the PDFs, split it into chunks, and create embeddings.
3. **Converse:** Type your question in the text box and press Enter. The chatbot will respond based on the information extracted from the PDFs.

### Notes

- Make sure you have enabled billing for your project on Google Cloud, as using the Gemini API may incur charges.
- The accuracy and quality of the chatbot's responses depend on the quality of the uploaded PDFs, the Gemini model being used, and how the questions are phrased.
- This is a basic project and can be extended with additional features such as support for different file formats, model customization options, enhanced user interface, and more. 
- Refer to the LangChain and Google Gemini documentation for more detailed information on customization and advanced usage. 
