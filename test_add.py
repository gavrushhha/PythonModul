from ProductandBasket import Basket, Product
import pytest

# tests = [('Мармелад', 'Мармелад'), ('Картофель', 'Картофель'), ('Морковь', 'Морковь')]
# tests = [('Мармелад, Картофель', 'Мармелад, Картофель')]
# tests = [('Мармелад', 'Мармелад')]
# @pytest.mark.parametrize('product,expected', tests)
# def test_add(product, expected):
#     assert Basket.add(product) == expected



test1 = [([Product('Хлеб', 50.0), Product('Морковь', 20.0), Product('Липтон', 100.0)], 'add')]
@pytest.mark.parametrize('product, s', test1)
def test_add(product: Product, s: str):
    basket1 = Basket()
    for p in product:
        basket1.add(p)
        assert s == basket1.add(p)

test2 = [([Product('Хлеб', 50.0), Product('Морковь', 20.0), Product('Липтон', 100.0)], 'remove')]
@pytest.mark.parametrize('product, s', test2)
def test_remove(product: Product, s: str):
    basket2 = Basket()
    for p in product:
        basket2.remove(p)
        assert s == basket2.remove(p)

test3 = [([Product('Хлеб', 50.0), Product('Морковь', 20.0), Product('Липтон', 100.0)], '170.0')]
@pytest.mark.parametrize('product, s', test3)
def test_summ(product: Product, s: str):
    basket3 = Basket()
    for p in product:
        basket3.add(p)
        assert s == basket3.count_sum(p)

test4 = [([Product('Хлеб', 50.0), Product('Морковь', 20.0), Product('Липтон', 100.0)])]

def test_field():
    bread = Product('Хлеб', 50.0)
    assert bread.name == 'Хлеб'


@pytest.mark.parametrize('name, price', test4)
def test_name(name: str, price: float):
    field_name = Product(name, price)
    assert field_name == name


@pytest.mark.parametrize('name, price', test4)
def test_price(name: str, price: float):
    field_price = Product(name, price)
    assert field_price == price




