from uuid import UUID

from pydantic import ValidationError
import pytest
from src.schemas.product import ProductIn
from tests.factorys import product_data


def test_schema_return_sucesses():
    data = product_data
    product = ProductIn.model_validate(data)

    assert product.name == "celular"
    assert isinstance(product.id, UUID)


def test_schema_return_raise():
    data = {"name": "celular", "quantity": 10, "price": 8.500}
    ProductIn.model_validate(data)
    with pytest.raises(ValidationError) as err:
        ProductIn.model_validate(data)

    assert err.value.errors()[0] == {
        "type": "missing",
        "loc": ("status",),
        "msg": "Field required",
        "input": {"name": "celular", "quantity": 10, "price": 8.5},
        "url": "https://errors.pydantic.dev/2.8/v/missing",
    }
