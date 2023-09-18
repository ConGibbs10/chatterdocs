from typing import Any, Dict

from langchain.embeddings import HuggingFaceInstructEmbeddings, HuggingFaceEmbeddings
from langchain.embeddings import OpenAIEmbeddings
from langchain.embeddings.base import Embeddings

def get_embeddings(config: Dict[str, Any]) -> Embeddings:
    if config['openai']:
        embeddings = OpenAIEmbeddings()
    else:
        config = {**config["embeddings"]}
        config["model_name"] = config.pop("model")
        if config["model_name"].startswith("hkunlp/"):
            Provider = HuggingFaceInstructEmbeddings
        else:
            Provider = HuggingFaceEmbeddings
        embeddings = Provider(**config)
    return embeddings
