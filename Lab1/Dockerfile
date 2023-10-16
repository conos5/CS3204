FROM python:3.11 as base

# Create a working directory in the container
WORKDIR /app

# Copy the Python script from the Python_Files directory into the working directory
COPY Python_Files/matrix_multiplication.py /app/

RUN pip install numpy matplotlib

# Set the working directory as the default directory for CMD
CMD ["python", "matrix_multiplication.py"]

