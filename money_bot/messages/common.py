from enum import StrEnum


class StrEnumAsCallback(StrEnum):
    @property
    def as_callback(self) -> dict[str, str]:
        """Return dict with data for InlineKeyboardButton (text and
        callback_data).
        """
        return {"text": self.value, "callback_data": self.name}

    @classmethod
    def value_of(cls, attr: str) -> str:
        return getattr(cls, attr).value


class MainButtons(StrEnumAsCallback):
    exchange = "Операция по обмену 💱"
    russian_transfer = "Отправка по России 🇷🇺"
    abroad_transfer = "Перестановка 🌍"
    question = "Задать вопрос ❓"
    back_to_menu = "Вернуться в главное меню 🏠"


class PayMethod(StrEnumAsCallback):
    cash = "Наличные 💰"
    cash_moscow = "Наличные в Москве 💰🇷🇺"
    cash_minsk = "Наличные в Минске 💰🇧🇾"
    bank = "Банковский перевод 🏦"


class ApprovalButtons(StrEnumAsCallback):
    approve = "✅"
    abort = "❌"


QUESTION_PROMPT_MESSAGE = (
    "Пожалуйста, отправьте ваш вопрос *одним* сообщением. "
)
QUESTION_SUCCESS_MESSAGE = (
    "Спасибо! Ваш вопрос перенаправлен менеджеру, "
    "в ближайшее время с вами свяжутся."
)

START_MESSAGE = (
    "Привествуем вас в нашем боте. Мы оказываем услуги по купле/продаже "
    "криптовалюты и перемещению денежных средств между разными странами "
    "и внутри РФ (перестановки). Пожалуйста, выберите услугу:"
)

AMOUNT_PROMPT = "Введите сумму в рублях в числовом формате"
