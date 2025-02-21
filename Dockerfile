# Use the specified Python version
ARG PYTHON_VERSION=3.13.1

# Use the official Python image from the Docker Hub
FROM python:${PYTHON_VERSION}

# Set the working directory in the container
WORKDIR /app

# Copy the dependency files to the working directory
COPY poetry.lock pyproject.toml ./

# Install Poetry and project dependencies
RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-root

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port the app runs on
EXPOSE 8080

# Set the entrypoint for the container
CMD ["./entrypoint.sh"]
