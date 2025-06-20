# # Use Python slim base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port (Railway uses 8000 by default)
EXPOSE 8000

# Start server with Gunicorn
CMD ["gunicorn", "group_chat.wsgi:application", "--bind", "0.0.0.0:8000"]
