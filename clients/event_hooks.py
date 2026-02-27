from httpx import Request, Response

from tools.logger import get_logger

logger = get_logger("HTTP_CLIENT")


def log_request_event_hook(request: Request):
    """
    Логирует информацию об отправленном HTTP запросе
    :param request: Объект запроса
    """
    logger.info(f"Выполняем {request.method} запрос на {request.url}")


def log_response_event_hook(response: Response):
    """
    Логирует информацию о полученном ответе на HTTP запрос
    :param response: Объект ответа
    """
    logger.info(f"Получен ответ {response.status_code} от {response.url}")
