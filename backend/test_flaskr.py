import os
from unicodedata import category
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format(
            "postgres", "root", "localhost:5432", self.database_name
        )

        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    def test_should_retrieve_categories(self):
        res = self.client().get('/categories')
        self.assertEqual(res.status_code, 200)

        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['categories']))

    def test_did_not_find_any_categories(self):
        res = self.client().get('/categories')
        self.assertEqual(res.status_code, 404)

    def test_should_retrieve_questions(self):
        res = self.client().get('/questions')
        self.assertEqual(res.status_code, 200)

        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['questions']))

    def test_did_not_find_any_questions(self):
        res = self.client().get('/questions')
        self.assertEqual(res.status_code, 404)

    def test_should_delete_question(self):
        res = self.client().delete('/questions/1')
        self.assertEqual(res.status_code, 200)

        data = json.loads(res.data)
        self.assertEqual(data['success'], True)

    def test_did_not_find_the_requested_question_to_delete(self):
        res = self.client().delete('/questions/55000')
        self.assertEqual(res.status_code, 404)

    def test_should_create_a_new_question(self):

        question = {'question': 'who is who', 'answer': 'yes',
                    'category': 'Science', 'difficulty': 4}

        res = self.client().post("/questions",
                                 json=question)

        self.assertEqual(res.status_code, 200, res.data)

    def test_could_not_create_new_question(self):
        res = self.client().post("/questions", json={})

        self.assertEqual(res.status_code, 400)

    def test_should_search_questions(self):
        res = self.client().post("/questions", json={"searchTerm": "b"})
        self.assertEqual(res.status_code, 200)

    def test_could_not_search_for_questions(self):
        res = self.client().post("/questions", json={})
        self.assertEqual(res.status_code, 400)

    def test_should_fetch_questions_based_on_category_id(self):
        res = self.client().get("/categories/1/questions")

        self.assertEqual(res.status_code, 200)

        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['questions']))

    def test_could_not_fetch_questions_based_on_category_id(self):

        res = self.client().get("/categories/10000/questions")
        self.assertEqual(res.status_code, 404)

    def test_could_play_quizzes(self):

        res = self.client().post("/quizzes",
                                 json={"previous_question": [1], "quiz_category": {"id": 1, "type": "Science"}})

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertIsNotNone(data["question"])

    def test_could_not_play_quizzes(self):

        res = self.client().post("/quizzes", json={})
        self.assertEqual(res.status_code, 400)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
