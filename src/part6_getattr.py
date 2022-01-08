import sklearn.ensemble

def get_estimator(params: dict):
  return getattr(sklearn.ensemble, params['estimator'])(**params['hyperparams'])


if __name__ == "__main__":

    params_rf = {
        'estimator': 'RandomForestClassifier',
        'hyperparams': {
            'n_estimators': 42,
            'max_depth': 3,
            'max_features': 'sqrt'
        }
    }

    params_gb = {
        'estimator': 'GradientBoostingClassifier',
        'hyperparams': {
            'n_estimators': 10,
            'learning_rate': 0.05,
            'subsample': 0.5
        }
    }

    estimator_rf = get_estimator(params_rf)
    estimator_gb = get_estimator(params_gb)
    print(estimator_rf, estimator_gb)
