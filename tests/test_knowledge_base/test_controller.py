from app.controller import controller_knowledge_base
from unittest.mock import patch, MagicMock
from pytest import raises
from fastapi import HTTPException


class TestKnowledgeBaseController:
    @patch("app.databases_holder")
    def test_empty_database_should_return_empty_dict(self, mock_database_holder):
        mock_database_holder.database_container = {}
        databases = controller_knowledge_base.get_databases()
        assert databases == {}

    mocked_empty_databases = {"database1": None, "database2": None}

    @patch.dict("app.databases_holder.database_container", mocked_empty_databases)
    def test_filled_empty_database_should_return_dict(self):
        databases = controller_knowledge_base.get_databases()
        assert databases == {"database1": None, "database2": None}

    mocked_database = MagicMock()
    mocked_database.docstore._dict = "123"
    mocked_databases = {"database1": mocked_database, "database2": None}

    @patch.dict("app.databases_holder.database_container", mocked_databases)
    def test_filled_database_should_return_dict(self):
        databases = controller_knowledge_base.get_databases()
        assert databases == {"database1": "123", "database2": None}

    mocked_creating_databases = {}

    @patch.dict("app.databases_holder.database_container", mocked_creating_databases)
    def test_should_create_empty_database(self):
        controller_knowledge_base.create_database("new_database")
        databases = controller_knowledge_base.get_databases()
        assert databases == {"new_database": None}

    mocked_exception_creating_databases = {"new_database": None}

    @patch.dict(
        "app.databases_holder.database_container", mocked_exception_creating_databases
    )
    def test_should_raise_exception_on_create_database(self):
        with raises(HTTPException) as exc_info:
            controller_knowledge_base.create_database("new_database")
