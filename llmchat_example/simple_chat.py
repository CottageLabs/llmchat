import logging

from llmchat import get_default_commands, get_default_config_template
from llmchat.chat_prompt_loop import ChatPromptLoop
from llmchat.chat_session import ChatSession
from llmchat.components.model_options import HuggingFaceModelOption, OpenAIModelOption
from llmchat.cpaths import CONFIG_PATH

log = logging.getLogger(__name__)


def main():
    DEFAULT_CONFIG = get_default_config_template()

    model_options = [
        HuggingFaceModelOption(name='gemma-3-1b', model_id="google/gemma-3-1b-it"),
        OpenAIModelOption(name='gpt-5-nano', model='gpt-5-nano-2025-08-07'),
    ]
    commands = get_default_commands()
    cs = ChatSession(
        available_models=model_options,
        default_config=DEFAULT_CONFIG,
        config_path=CONFIG_PATH,
    )
    chat_loop = ChatPromptLoop(cs, commands)
    chat_loop.initialize()
    chat_loop.run()


if __name__ == '__main__':
    main()
