from httpx import Client


def get_public_http_client() -> Client:
    """
    Функция создания экземпляра httpx.Client с базовыми настройками

    :return: Готовый к использованию httpx.Client
    """
    return Client(
        timeout=10,
        base_url="https://petstore.swagger.io/v2",
    )
