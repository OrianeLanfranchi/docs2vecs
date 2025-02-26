from typing import List
from typing import Optional

from llama_index.embeddings.azure_openai import AzureOpenAIEmbedding

from docs2vecs.subcommands.indexer.config import Config
from docs2vecs.subcommands.indexer.document import Document
from docs2vecs.subcommands.indexer.skills.skill import IndexerSkill


class AzureAda002EmbeddingSkill(IndexerSkill):
    def __init__(self, config: dict, global_config: Config):
        super().__init__(config, global_config)

    def az_ada002_embeddings(self, content: str):
        embed_model = AzureOpenAIEmbedding(
            deployment_name=self._config["deployment_name"],
            api_key=self._config["api_key"],
            azure_endpoint=self._config["endpoint"],
            api_version=self._config["api_version"],
        )
        return embed_model.get_query_embedding(content)

    def run(self, input: Optional[List[Document]] = None) -> Optional[List[Document]]:
        self.logger.info("Running AzureAda002EmbeddingSkill...")
        self.logger.info(f"Number of documents: {len(input)}")

        for doc in input:
            self.logger.debug(f"Processing document: {doc.filename}")
            for chunk in doc.chunks:
                self.logger.debug(f"Creating embedding for chunk: {chunk.chunk_id}")
                chunk.embedding = "" if not chunk.content else self.az_ada002_embeddings(chunk.content)

        return input
