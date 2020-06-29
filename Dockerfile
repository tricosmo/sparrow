FROM python:3.7.3-stretch

# Working Directory
WORKDIR /app

# Copy source code to working directory
COPY . /app/

# Install packages from requirements.txt
# hadolint ignore=DL3013
RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt

ENV FLASK_APP=/app/web/hello.py
ENV FLASK_ENV=production
EXPOSE 8080
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
