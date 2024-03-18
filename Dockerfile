FROM python:3.8-slim

WORKDIR /nrich

COPY . /nrich

# Install packages
COPY requirements.txt /nrich/
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run app when the container launches
ENTRYPOINT ["python", "ema_calculator.py"]
