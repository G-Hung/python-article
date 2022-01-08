def model(*, k:int=10, estimate_k:bool=True, standardize:bool=False, seed:int=1234):
    print(f"k: {k}, estimate_k: {estimate_k}, standardize: {standardize}, seed: {seed}")

if __name__ == "__main__":
    try:
        model(10, False, True, 1234)
    except TypeError:
        print('TypeError is raised')
