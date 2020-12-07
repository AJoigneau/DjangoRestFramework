FROM python:3.8.6

# Set environment variables
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /

# Install dependencies.
RUN pip install -r /requirements.txt

# Set work directory.
RUN mkdir /code
WORKDIR /code
CMD python manage.py test

# Copy project code.
COPY . /code/

EXPOSE 81