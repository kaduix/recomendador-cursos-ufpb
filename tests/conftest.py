import pytest


@pytest.fixture
def flask_client():
    """Cliente de teste Flask; exige SWI-Prolog disponível para PySwip."""
    import app as app_module

    app_module.app.config["TESTING"] = True
    with app_module.app.test_client() as client:
        yield client
