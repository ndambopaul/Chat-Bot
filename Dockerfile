# Use the official Python image as base
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy the Django application code
COPY ./my_django_app /app/my_django_app

# Expose the Django server port
EXPOSE 8000

# Run Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
