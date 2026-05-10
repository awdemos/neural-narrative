from src.dialogues.providers.ambient_narration_provider import AmbientNarrationProvider
from src.dialogues.transcription import Transcription
from src.maps.factories.local_information_factory import LocalInformationFactory
from src.prompting.abstracts.abstract_factories import (
    ProduceToolResponseStrategyFactory,
)


class AmbientNarrationProviderFactory:

    def __init__(
        self,
        playthrough_name: str,
        produce_tool_response_strategy_factory: ProduceToolResponseStrategyFactory,
        local_information_factory: LocalInformationFactory,
    ):
        self._playthrough_name = playthrough_name
        self._produce_tool_response_strategy_factory = (
            produce_tool_response_strategy_factory
        )
        self._local_information_factory = local_information_factory

    def create_provider(self, transcription: Transcription) -> AmbientNarrationProvider:
        return AmbientNarrationProvider(
            self._playthrough_name,
            transcription,
            self._produce_tool_response_strategy_factory,
            self._local_information_factory,
        )
