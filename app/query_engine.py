from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.response_synthesizers import CompactAndRefine

def create_query_engine(index):
    retriever = index.as_retriever()
    response_synthesizer = CompactAndRefine()
    return RetrieverQueryEngine(
        retriever=retriever,
        response_synthesizer=response_synthesizer
    )
