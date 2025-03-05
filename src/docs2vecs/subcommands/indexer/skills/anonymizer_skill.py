from typing import List
from typing import Optional
from tspii.tools.pseudonymizer import CustomAnonymizer

from docs2vecs.subcommands.indexer.config import Config
from docs2vecs.subcommands.indexer.document import Document
from docs2vecs.subcommands.indexer.skills.skill import IndexerSkill

class AnonymizerSkill(IndexerSkill):
    def __init__(self, skill_config: dict, global_config: Config) -> None:
        super().__init__(skill_config, global_config)
        self.fakeData = self._config.get("fake_data", False)

    def run(self, input: Optional[List[Document]] = None) -> List[Document]:
        if not input:
            self.logger.info(f"No documents to anonymize")
            return input
        
        for document in input:
            print("\nOriginal content:") # DEBUG
            print(document.text) # DEBUG

            # Anonymize the text
            pseudonymizer = CustomAnonymizer(add_default_faker_operators=False)

            pseudonymizer.add_custom_recognizers()

            if self.fakeData:
                pseudonymizer.add_custom_fake_data_generators() # Will generate fale data instead of placeholders when anonymizing data

            document.text = pseudonymizer.anonymize_document(document.text)

            print("\Anonymized content:") # DEBUG
            print(document.text) # DEBUG

            print("\nMap:") # DEBUG
            print(pseudonymizer.deanonymize_mapping()) # DEBUG
            
        self.logger.info(f"Successfully anonymized {len(input)} documents")
        return input