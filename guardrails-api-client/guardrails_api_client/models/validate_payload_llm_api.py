from enum import Enum


class ValidatePayloadLlmApi(str, Enum):
    OPENAI_CHATCOMPLETION_ACREATE = "openai.ChatCompletion.acreate"
    OPENAI_CHATCOMPLETION_CREATE = "openai.ChatCompletion.create"
    OPENAI_COMPLETION_ACREATE = "openai.Completion.acreate"
    OPENAI_COMPLETION_CREATE = "openai.Completion.create"

    def __str__(self) -> str:
        return str(self.value)
