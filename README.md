# NRICH. TEST CASE. TASK 2

This application calculates Exponential Moving Average (EMA) trend scores for a given dataset

## Building the Image

To build the Docker image, run:
```python
docker build -t ema_trend_calculator
```

## Running the Container

To process an input CSV file and generate an output CSV file with EMA trend scores, run:

```python
docker run -v /path/to/data:/nrich ema_trend_calculator /nrich/input.csv /nrich/output.csv
```