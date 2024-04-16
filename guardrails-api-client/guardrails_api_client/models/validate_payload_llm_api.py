from enum import Enum


class ValidatePayloadLlmApi(str, Enum):
    LITELLM_ACOMPLETION = "litellm.acompletion"
    LITELLM_COMPLETION = "litellm.completion"
    OPENAI_CHATCOMPLETION_ACREATE = "openai.ChatCompletion.acreate"
    OPENAI_CHATCOMPLETION_CREATE = "openai.ChatCompletion.create"
    OPENAI_CHAT_COMPLETIONS_CREATE = "openai.chat.completions.create"
    OPENAI_COMPLETIONS_CREATE = "openai.completions.create"
    OPENAI_COMPLETION_ACREATE = "openai.Completion.acreate"
    OPENAI_COMPLETION_CREATE = "openai.Completion.create"

    def __str__(self) -> str:
        return str(self.value)
