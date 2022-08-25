# DOCUMENTATION TRIVIA API

`GET '/categories'`

- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, `categories`, that contains an object of `id: category_string` key: value pairs.

```json
{
  "1": "Science",
  "2": "Art",
  "3": "Geography",
  "4": "History",
  "5": "Entertainment",
  "6": "Sports"
}
```
`GET '/categories?page=1'`
 - This endpoint returns a list of questions,
    number of total questions, current category, categories.
- Request Arguments: None
- Params : page
- Returns:


```json
{
  "success":true,
  "categories":{1: "Science", 2: "Art", 3: "Geography", 4: "History", 5: "Entertainment", 6: "Sports"},
  "current_category":"Science",
  "questions": [
    {
        "answer": "Apollo 13",
        "category": 5,
        "difficulty": 4,
        "id": 2,
        "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"

    },

  ],
  "total_questions": 17
}
```



`DELETE '/questions/[question_id]'`

- This is an endpoint to DELETE question using a question ID.
- Request arguments : question_id  . `Example: /questions/1`
- Returns 

```json
{
    "success": true,
    "deleted": question_id
}

```

`POST /questions`
- This an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.
- Request arguments : question:string, answer:string, category:string, difficulty:int
- Returns a json object containing a success key, and the newly created question id (created)

`POST /questions/search`

- This is a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.
- Request params : searchTerm:string
- Return json object structured as { success:bool, questions:array, total_questions:int ,current_category:string}

`GET /categories/<int:category_id>/questions`

-  This is an Endpoint to get questions based on category.
- Request Params : category_id
- return any question that belongs to the category identified by category_id


```json
{
  "success":true,
  "current_category":"Science",
  "questions": [
    {
        "answer": "Apollo 13",
        "category": 5,
        "difficulty": 4,
        "id": 2,
        "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"

    },

  ],
  "total_questions": 17
}
```

`POST /quizzes`

- This is a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided
- Request params : previous_questions : array<int>, quiz_category:object<id:int,type:string>
