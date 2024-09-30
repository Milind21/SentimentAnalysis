FROM python:3.9.12

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN python -c "import nltk; nltk.download('omw-1.4'); nltk.download('wordnet')"

COPY . . 

EXPOSE 5001

CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]