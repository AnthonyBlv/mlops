FROM python:3.11.10-slim-bookworm


RUN pip install "fastapi[standard]"
RUN pip install joblib
RUN pip install pandas
RUN pip install "scikit-learn"

COPY . .

CMD ["fastapi", "dev", "app.py", "--host", "0.0.0.0", "--port", "8080"]