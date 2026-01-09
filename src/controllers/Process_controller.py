from .Base_controller import Base_controller
from .Project_controller import Project_controller
from models.enums import ProcessEnum
import os
from langchain_community.document_loaders import TextLoader, PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


class Process_controller(Base_controller):
    def __init__(self, project_id: str):
        super().__init__()
        self.project_id = project_id
        self.project_path = Project_controller().get_project_dir(
            project_id=project_id
        )

    def get_file_extension(self, file_id: str):
        return os.path.splitext(file_id)[-1]

    def get_file_loader(self, file_id: str):
        file_extension = self.get_file_extension(file_id)
        file_path = os.path.join(self.project_path, file_id)

        if file_extension == ProcessEnum.txt.value:
            return TextLoader(file_path, encoding="utf-8")
        elif file_extension == ProcessEnum.pdf.value:
            return PyMuPDFLoader(file_path)
        return None

    def get_file_content(self, file_id: str):
        loader = self.get_file_loader(file_id)
        if loader is None:
            return []
        return loader.load()

    def process_file_content(
        self,
        file_content: list,
        file_id: str,
        chunk_size: int = 100,
        overlap: int = 20,
    ):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=overlap,
            length_function=len,
        )

        file_content_text = [doc.page_content for doc in file_content]
        file_content_metadata = [doc.metadata for doc in file_content]

        return text_splitter.create_documents(
            file_content_text,
            metadatas=file_content_metadata,
        )
