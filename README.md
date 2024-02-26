# VectorSearchAPI

## Overview
This project is a Django-based web application that utilizes various libraries for RESTful API development, natural language processing (NLP), and document manipulation. It provides functionalities related to language processing, community interaction, and document management.

## Installation
1. Clone the repository: git clone git@github.com:Hebjies/VectorSearchAPI.git
2. Install dependencies using pip: pip install -r requirements.txt

## Start Up
1. Declare your openai key as an env var: export OPENAI_API_KEY="api_key"
2. Open Docker.
3. Start Docker container: docker-compose up -d
4. Run the Django development server: python manage.py runserver
5. Access the application in your web browser at `http://127.0.0.1:8000/api`.

## Usage

There are 2 endpoints: api/documents/ and api/answer/. The api/documents/ endpoint receives the docs (.docx) files (filename should not have empty spaces) and the api/answer/ receives a query and returns an answer. Please send one document at a time.

Here are some examples:

Upload documents:

curl --location 'http://127.0.0.1:8000/api/documents/' \
--header 'Authorization: Token 2596df360224a9b8a71f7120371bebfe27043040' \
--form 'title="Document Name"' \
--form 'docx_file=@"/Users/username/FolderName/filename.docx"'

Query documents:

curl --location 'http://127.0.0.1:8000/api/answer/' \
--header 'Authorization: Token 2596df360224a9b8a71f7120371bebfe27043040' \
--form 'answer="How much is the late fee?"'

Detailed documentation can be found at http://127.0.0.1:8000/docs

## Contact
For inquiries or support, please contact [heb.jimenez@gmail.com].

