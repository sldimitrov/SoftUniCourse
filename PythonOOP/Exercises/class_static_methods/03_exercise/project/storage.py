from typing import List
from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:

    def __init__(self):
        self.categories: List[Category] = []
        self.documents = List[Document] = []
        self.topics: List[Topic] = []

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str) -> None:
        category = next(filter(lambda x: category_id == x.id, self.categories))
        category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        topic = next(filter(lambda x: x.id == topic_id, self.topics))
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        document = next(filter(lambda x: x.id == document_id, self.documents))
        document.edit(new_file_name)

    def delete_category(self, category_id) -> None:
        category = next(filter(lambda x: x.id == category_id, self.categories))
        self.categories.remove(category)

    def delete_topic(self, topic_id) -> None:
        topic = (next(filter(lambda x: x.id == topic_id, self.topics)))
        self.topics.remove(topic)

    def delete_document(self, document_id) -> None:
        document = next(filter(lambda x: x.id == document_id, self.documents))
        self.documents.remove(document)

    def get_document(self, document_id):
        document = next(filter(lambda x: x. x.id == document.id, self.documents))
        return document

    def __repr__(self):
        return "\n".join(d for d in self.documents)
