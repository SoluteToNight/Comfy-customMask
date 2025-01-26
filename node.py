import numpy as np
import torch
from PIL import Image, ImageDraw, ImageFont
from torch.ao.nn.quantized.functional import threshold


def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)
class GenerateMask:

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "image": ("IMAGE",),
        }
        }

    RETURN_TYPES = ("MASK",)
    FUNCTION = "process"
    OUTPUT_NODE = True
    CATEGORY = "CUSTOM MASK"

    def process(self,image):
        data = np.array(image)
        r_channel = data[:, :, 0]
        g_channel = data[:, :, 1]
        b_channel = data[:, :, 2]
        threshold = 5
        mask = (r_channel <= threshold) & (g_channel <= threshold) & (b_channel <= threshold)
        mask_image = mask.astype(np.uint8) * 255
        mask_pil = Image.fromarray(mask_image)
        return(mask,)

