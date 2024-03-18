import pandas as pd
import numpy as np
import sys


def score_trend(row, model, max_increase, max_decrease):
    if pd.isna(row[model]):
        return np.nan  # Handling the NA values for the initial period without enough data
    change = row['interest_level'] - row[model]
    if change > 0:
        return 50 + (change / max_increase) * 50     # Scale to 50-100 range
    elif change < 0:
        return 50 + (change / abs(max_decrease)) * 50  # Scale to 0-50 range
    else:
        return 50


def ema(df_ema, span=4):
    # Calculate EMA using the pandas ewm()
    df_ema['ema'] = df_ema.groupby(['company_id', 'topic_id'])['interest_level'].transform(
        lambda x: x.ewm(span=span, adjust=False).mean())

    max_increase = (df_ema['ema'] - df_ema['interest_level'].shift(span - 1)).max()
    max_decrease = (df_ema['ema'] - df_ema['interest_level'].shift(span - 1)).min()

    df_ema['trend_score'] = df_ema.apply(lambda row: score_trend(row, 'ema', max_increase, max_decrease), axis=1)
    return df_ema


if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    df = pd.read_csv(input_file)
    df = ema(df)
    df.to_csv(output_file, index=False)
