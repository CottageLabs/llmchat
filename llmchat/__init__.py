def get_default_config_template():
    return {
        # Chat
        'max_width': 100,

        # Chat Session
        'temperature': 1.2,
        'model_option_name': 'gemma-3-1b',
        'output_mode': 'simple',

        # Hugging Face LLM
        'device': 'cpu',
        'return_full_text': False,
    }


def get_default_commands():
    from llmchat.commands import ConfigsCommand, ModelsCommand, ResetConfigCommand  # noqa
    return [
        ConfigsCommand(),
        ModelsCommand(),
        ResetConfigCommand(),
    ]


from llmchat.chat_prompt_loop import ChatPromptLoop  # noqa
from llmchat.chat_session import ChatSession  # noqa
