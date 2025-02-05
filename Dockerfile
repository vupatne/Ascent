FROM python:3.7

ENV FLASK_APP app.py

COPY app.py gunicorn-cfg.py requirements.txt ./
COPY constants ./constants
COPY controller ./controller
COPY repository ./repository
COPY static ./static
COPY templates ./templates
COPY utils ./utils
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "app:app"]
