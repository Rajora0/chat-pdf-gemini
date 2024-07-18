from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def get_chunks(raw_text):
    """Splits the text into smaller chunks.

    Args:
        raw_text: The input text string.

    Returns:
        A list of text chunks.
    """
    text_splitter = CharacterTextSplitter(
        separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len
    )
    chunks = text_splitter.split_text(raw_text)
    return chunks


def get_vectorstore(chunks):
    """Creates a vectorstore from the text chunks.

    Args:
        chunks: A list of text chunks.

    Returns:
        A FAISS vectorstore.
    """
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={"device": "cpu"}
    )
    vectorstore = FAISS.from_texts(texts=chunks, embedding=embeddings)
    return vectorstore