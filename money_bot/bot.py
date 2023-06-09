import logging

from telegram.ext import Application, PicklePersistence, CommandHandler, \
    MessageHandler, ConversationHandler

from config import TELEGRAM_BOT_TOKEN, BASE_DIR
from handlers import CONVERSATIONS
from handlers.common import start, reply_to_others, error_handler, \
    default_fallbacks, MAIN_ENTRY_POINT
from services.decorators import debug_conversation_handlers
from services.filters import ALL_NOT_CMND_NOR_BTN
from services.utils import validate_unique_states

logger = logging.getLogger(__name__)


def main() -> None:
    validate_unique_states(CONVERSATIONS)
    debug_conversation_handlers(CONVERSATIONS)

    application = Application.builder().token(
        TELEGRAM_BOT_TOKEN,
    ).persistence(
        PicklePersistence(filepath=BASE_DIR / "data/conversation"),
    ).build()

    main_conv = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            MAIN_ENTRY_POINT: [*CONVERSATIONS],
        },
        fallbacks=default_fallbacks,
        allow_reentry=True,
        name="main_conv",
        persistent=True,
    )

    application.add_handler(main_conv)
    application.add_handler(
        MessageHandler(ALL_NOT_CMND_NOR_BTN, reply_to_others)
    )
    application.add_error_handler(error_handler)

    application.run_polling()


if __name__ == "__main__":
    main()
