from dataclasses import dataclass, field
from typing import Optional
from transformers import Seq2SeqTrainingArguments

# NOTE: The transformers package is updated during our work
# , our "WrappedSeq2SeqTrainingArguments" is now a feature named "Seq2seqTrainingArguments"

@dataclass
class WrappedSeq2SeqTrainingArguments(Seq2SeqTrainingArguments):
    """
    sortish_sampler (:obj:`bool`, `optional`, defaults to :obj:`False`):
        Whether to use a `sortish sampler` or not. Only possible if the underlying datasets are `Seq2SeqDataset` for
        now but will become generally available in the near future.

        It sorts the inputs according to lengths in order to minimize the padding size, with a bit of randomness for
        the training set.
    predict_with_generate (:obj:`bool`, `optional`, defaults to :obj:`False`):
        Whether to use generate to calculate generative metrics (ROUGE, BLEU).
    """

    cfg: str = None
    sortish_sampler: bool = field(default=False, metadata={"help": "Whether to use SortishSampler or not."})
    predict_with_generate: bool = field(
        default=False, metadata={"help": "Whether to use generate to calculate generative metrics (ROUGE, BLEU)."}
    )
    generation_max_new_tokens: int = field(
        default=100, metadata={
            "help": "The max_length to use on each evaluation loop when predict_with_generate=True."
                    " Will default to the max_new_tokens value of the model configuration."}
    )
    generation_num_beams: int = field(
        default=4, metadata={
            "help": "The num_beams to use on each evaluation loop when predict_with_generate=True."
                    " Will default to the num_beams value of the model configuration."}
    )
    load_weights_from: Optional[str] = field(
        default=None, metadata={
            "help": "The directory to load the model weights from."}
    )
    customize_gen_stopping_criteria: Optional[list] = field(
        default=None, metadata={
            "help": "Stopping criteria for generation. "}
    )
    