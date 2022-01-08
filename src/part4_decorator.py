import pandas as pd


from functools import wraps
import time

def timer(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        start = time.time()
        x = f(*args, **kwargs)
        print(f"time for {f.__name__}: {time.time() - start}")
        return x
    return wrap

def show_shape(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        print(f"\nfunction: {f.__name__}")
        for key, val in kwargs.items():
          if isinstance(val, pd.DataFrame):
            print(f"{key}.shape: {val.shape}")
        x = f(*args, **kwargs)
        return x
    return wrap

@timer
@show_shape
def process_data(df1, df2):
  time.sleep(0.3)
  return pd.concat([df1, df2])

@timer
@show_shape
def model_train(training_df):
  time.sleep(0.3)
  return training_df

@timer
@show_shape
def evaluate(evaluate_df, df1, df2):
  time.sleep(0.3)

@timer
def pipeline(df1, df2):
  df = process_data(df1=df1, df2=df2)
  df = model_train(training_df=df)
  evaluate(evaluate_df=df, df1=df1, df2=df2)

if __name__ == "__main__":

    d1 = {'col1': [1, 2], 'col2': [3, 4]}
    df1 = pd.DataFrame(data=d1)

    d2 = {'col1': [1, 2, 3], 'col2': [3, 4, 5]}
    df2 = pd.DataFrame(data=d2)

    pipeline(df1=df1, df2=df2)