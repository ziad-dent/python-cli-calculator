FROM python:3.11-alpine
WORKDIR /app
COPY calc.py .
CMD [ "python", "calc.py" ]
