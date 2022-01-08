def model(*args, **kwargs):
  print(args, kwargs)


if __name__ == "__main__":
    params = {
        'k': 10,
        'estimate_k': True,
        'standardize': False,
        'seed': 1234
    }

    model(**params)