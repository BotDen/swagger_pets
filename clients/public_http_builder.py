from httpx import Client

from clients.event_hooks import log_request_event_hook, log_response_event_hook


def get_public_http_client() -> Client:
    """
    Функция создания экземпляра httpx.Client с базовыми настройками

    :return: Готовый к использованию httpx.Client
    """
    return Client(
        timeout=10,
        base_url="https://petstore.swagger.io/v2",
        event_hooks={
            "request": [log_request_event_hook],
            "response": [log_response_event_hook],
        }
    )
