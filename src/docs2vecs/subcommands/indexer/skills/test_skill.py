from typing import List
from typing import Optional

from docs2vecs.subcommands.indexer.config import Config
from docs2vecs.subcommands.indexer.document import Document
from docs2vecs.subcommands.indexer.skills.skill import IndexerSkill

class TestSkill(IndexerSkill):
    def __init__(self, skill_config: dict, global_config: Config) -> None:
        super().__init__(skill_config, global_config)

    def run(self, input: Optional[List[Document]] = None) -> List[Document]:
        for document in input:
            print(document.text)
        self.logger.info(f"TESTSKILL IS HERE")
        return input