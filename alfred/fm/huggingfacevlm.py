import logging
import torch
from PIL import Image
from transformers import AutoProcessor, CLIPModel
from typing import Optional, List, Tuple

from alfred.fm.model import LocalAccessFoundationModel
from .response import RankedResponse

logger = logging.getLogger(__name__)


class HuggingFaceCLIPModel(LocalAccessFoundationModel):
    """
     The HuggingFaceModel class is a wrapper for HuggingFace VLM Models
     Currently supports CLIP models.
    """

    def __init__(self, model_string: str, local_path: Optional[str] = None):
        """
        Constructor for HuggingFaceVLMModel

        :param model_string: model string for the HuggingFace model
        :type model_string: str
        :param local_path: (optional) local path to store the model
        :type local_path: Optional[str]
        """
        super().__init__(model_string, local_path)
        self.device = "cuda:0" if torch.cuda.is_available() else "cpu"
        self.model = CLIPModel.from_pretrained(model_string,
                                               cache_dir=local_path).to(
            self.device)
        self.tokenizer = None
        self.processor = AutoProcessor.from_pretrained(model_string,
                                                       cache_dir=local_path)
        self.model.eval()

    def _score_batch(
            self,
            batch_instance: Tuple[List[Image.Image], List[str]],
            **kwargs,
    ):
        """
        Scores a batch of instances

        :param batch_instance: batch of instances
        :type batch_instance: Tuple[List[Image.Image], List[str]]
        :param kwargs: (optional) additional arguments
        :type kwargs: Dict
        :return: list of RankedResponse
        :rtype: List[RankedResponse]
        """
        return_image_features = kwargs.get("return_image_features", False)
        return_raw_logits = kwargs.get("raw_logits", False)

        image, candidates = batch_instance

        text = self.processor(text=candidates,
                              padding=True,
                              truncation=True,
                              return_tensors="pt").to(self.device)
        image = self.processor(images=image,
                               return_tensors="pt").to(self.device)

        image_features = self.model.get_image_features(**image)
        text_features = self.model.get_text_features(**text)

        image_features = image_features / image_features.norm(
            p=2, dim=-1, keepdim=True)
        text_features = text_features / text_features.norm(
            p=2, dim=-1, keepdim=True)

        logits_per_image = image_features @ text_features.t()
        logits_per_text = logits_per_image.t().detach().cpu()

        logits = logits_per_text if return_raw_logits else logits_per_text.softmax(
            dim=0)
        prediction = [candidates[i] for i in logits.argmax(dim=0)]

        return [
            RankedResponse(prediction=prediction[i],
                           scores={
                               candidate: logits[cidx][i].item()
                               for cidx, candidate in enumerate(candidates)
                           },
                           logits={
                               candidate: logits_per_text[cidx][i].item()
                               for cidx, candidate in enumerate(candidates)
                           },
                           embeddings=image_features[i]
                           if return_image_features else None)
            for i in range(len(prediction))
        ]