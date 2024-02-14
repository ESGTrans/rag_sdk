import os

from rag_sdk.utils.api_utils import RequestSender


class RAGCore:
    ENDPOINT = "https://rag.laplace-ai.com"

    def __init__(
        self,
        llm_model: str = "gpt-3.5-turbo",
        embedding_model: str = "shibing624/text2vec-base-chinese",
        vector_database_uri: str = None,
        collection_list: list = [],
    ):
        self.llm_model = llm_model
        self.embedding_model = embedding_model
        self.vector_database_uri = vector_database_uri
        self.collection_list = collection_list

        self.request_sender = RequestSender()

    def show_available_llm_models(self):
        pass

    def show_available_embedding_models(self):
        pass

    def show_available_collections(self):
        assert (
            self.vector_database_uri is not None
        ), "vector_database_uri is not provided!"
        pass

    def search(
        self,
        query: str,
        top_k: int = 5,
        filters: dict = {},
        verbose: bool = False,
        **kwargs,
    ):
        pass

    def chat(
        self,
        query: str,
        top_k: int = 5,
        filters: dict = {},
        verbose: bool = False,
        **kwargs,
    ):
        uri = f"{self.ENDPOINT}/rag/chat"
        data = {
            "llm_model": self.llm_model,
            "embedding_model": self.embedding_model,
            "vector_database_uri": self.vector_database_uri,
            "collection_list": self.collection_list,
            "query": query,
            "custom_topk": top_k,
            "query_filters": filters,
            "verbose": verbose,
            **kwargs,
        }
        response = self.request_sender.send_streaming_request("POST", uri, data=data)
        return response
