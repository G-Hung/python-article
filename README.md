# python-article
repo to demo the things in article


# Setup

### Conda
```
conda env create --file=conda.yml

conda activate python_demo

# run this again if requirements.txt is updated
conda env update --file conda.yml --prune
```

### pre-commit, https://pre-commit.com/
```
# we should see pre-commit is installed, if not, checkout: https://pre-commit.com/
pre-commit --version

pre-commit run --all-files
```

