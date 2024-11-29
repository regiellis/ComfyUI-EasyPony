from typing import Dict
from enum import Enum

"""
EasyPony - Resources for implementation of EasyPony prompt sturcture
- https://civitai.com/articles/8547/prompting-for-score-or-source-or-rating-or-and-an-overview-of-prompting-syntax
- https://civitai.com/articles/4871/pony-diffusion-v6-xl-prompting-resources-and-info
- https://civitai.com/articles/4248/what-is-score9-and-how-to-use-it-in-pony-diffusion
- https://civitai.com/articles/6160/negative-prompt-for-pdxl-v2-works-with-other-models

"""


class EasyPony:

    class PonyTokens(Enum):
        ONLY_THE_BEST = "score_9, highly detailed"
        GOOD = "score_9, score_8_up, score_7_up, highly detailed"
        AVERAGE = "score_9, score_8_up, score_7_up, score_6_up"
        EVERYTHING = "score_9, score_8_up, score_7_up, score_6_up, score_5_up, score_4_up, highly detailed"

    SOURCES = [
        "source_anime",
        "source_pony",
        "source_fury",
        "source_cartoon",
    ]

    RATING = [
        "rating_safe",
        "rating_questionable",
        "rating_explicit",
    ]

    NEG = "text, deformed, bad hands, worst quality, low quality, deformed, censored, bad anatomy, watermark, signature,"

    CENSORSHIP = " ".join(
        [
            "bar censor, censor, censor mosaic, censored, filter abuse",
            "heavily pixelated, instagram filter, mosaic censoring, over filter",
            "over saturated, over sharpened, overbrightened, overdarkened",
            "overexposed, overfiltered, oversaturated",
        ]
    )

    QUALITY_BOOST = " ".join(
        [
            "ai-generated, artifact, artifacts, bad quality, bad scan, blurred",
            "blurry, compressed, compression artifacts, corrupted, dirty art scan",
            "dirty scan, dithering, downsampling, faded lines, frameborder, grainy",
            "heavily compressed, heavily pixelated, high noise, image noise, low dpi",
            "low fidelity, low resolution, lowres, moire pattern, moiré pattern",
            "motion blur, muddy colors, noise, noisy background, overcompressed",
            "pixelation, pixels, poor quality, poor lineart, scanned with errors",
            "scan artifact, scan errors, very low quality, visible pixels",
        ]
    )

    NEG_EXP = " ".join(
        [
            "3rd party watermark",
            "abstract, aliasing, alternate form, anatomically incorrect, artistic error",
            "asymmetrical, bad anatomy, bad aspect ratio, bad compression, bad cropping",
            "bad edit, bad feet, bad hands, bad leg, bad lighting, bad metadata, bad neck",
            "bad parenting, bad perspective, bad proportions, bad quality, bad shading",
            "bad trigger discipline, badly compressed, bar censor, black and white, black bars",
            "blur censor, blurred, blurry, broken anatomy, censor bar, censored, chromatic aberration",
            "color banding, color edit, color issues, compressed, compression artifacts, cropped",
            "deformed, depth of field, derivative work, disfigured, distracting watermark, downscaled",
            "edit, edited, edited screencap, elongated body, error, exaggerated anatomy, extra arms",
            "extra digits, extra fingers, extra legs, fused fingers, fused limbs, gif, gif artifacts",
            "greyscale, hair censor, has bad revision, has censored revision, has downscaled revision",
            "idw, incorrect leg anatomy, irl, jpeg artifacts, long neck, low quality, low res",
            "low resolution, lowres, md5 mismatch, meme, microsoft paint (software), missing arm",
            "missing body part, missing finger, missing leg, missing limb, mosaic censoring, ms paint",
            "mutated, mutation, mutilated, needs more jpeg, needs more saturation,",
            "novelty censor, obtrusive watermark, off-topic, photo, photoshop (medium), pixel art",
            "pixelated, pixels, recolor, resampling artifacts, resized, resolution mismatch, scan artifacts",
            "screencap, simple background, simple shading, sketch, source larger, source smaller, steam censor",
            "stitched, tail censor, third-party edit, third-party watermark, too many fingers, traditional art",
            "tumblr, typo, ugly, unfinished, upscaled, vector trace, wrong aspect ratio, wrong eye shape",
        ]
    )

    DEFAULT = " ".join(
        [
            "Raw Photo, Cowboy Shot, yorha no. 2 type b, short white hair, black dress, hairband, black gloves,"
            "clothing cutout, cleavage cutout, puffy sleeves, long sleeves, black hairband, feather-trimmed sleeves,"
            "juliet sleeves, mole under mouth, holding katana, black thighhighs, turtleneck, sunset, rubble in the background,"
            "depth of field, dynamic angle, photo realistic:1.4, realistic skin:1.4, fashion photography,"
            "sharp, analog film grain, hyperdetailed:1.15"
        ]
    )

    def __init__(self):
        pass

    @staticmethod
    def INPUT_TYPES():
        PSONA_UI_PONY_TOKENS: Dict = {
            "optional": {
                "prefix": ("STRING", {"forceInput": True}),
                "suffix": ("STRING", {"forceInput": True}),
            },
            "required": {
                "Quality": (
                    list(EasyPony.PonyTokens.__members__.keys()),
                    {"default": "EVERYTHING"},
                ),
                "Source": (["-"] + EasyPony.SOURCES, {"default": "-"}),
                "Rating": (["-"] + EasyPony.RATING, {"default": "-"}),
                "Prompt": ("STRING", {"default": EasyPony.DEFAULT, "multiline": True}),
                "SFW": ("BOOLEAN", {"default": True, "forceInput": False}),
                "Quality Boost (Beta)": ("BOOLEAN", {"default": False}),
                "Negative Boost (Beta)": ("BOOLEAN", {"default": False}),
            },
        }

        return PSONA_UI_PONY_TOKENS

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("Prompt", "Negative")
    OUTPUT_IS_LIST = (False, False)
    FUNCTION = "display"

    CATEGORY = "itsjustregi / EasyPony"

    def display(self, **kwargs):

        prompt_elements = []
        nagative = []

        quality_value = EasyPony.PonyTokens[kwargs["Quality"]].value
        source = "" if kwargs.get("Source") == "-" else kwargs["Source"]
        rating = "" if kwargs.get("Rating") == "-" else kwargs["Rating"]

        if kwargs.get("prefix"):
            quality_value = kwargs["prefix"]

        quality_value and prompt_elements.append(
            ", ".join([quality_value, source, rating])
        )

        kwargs["SFW"] and prompt_elements.append("(sfw:1.2)")

        kwargs.get("Prompt") and prompt_elements.append(kwargs["Prompt"])
        kwargs.get("suffix") and prompt_elements.append(kwargs["suffix"])

        final_prompt = " ".join(prompt_elements).lower()

        kwargs["SFW"] and nagative.append(f"{self.CENSORSHIP}".strip())
        kwargs["Quality Boost (Beta)"] and nagative.append(
            f"{self.QUALITY_BOOST}".strip()
        )
        kwargs["Negative Boost (Beta)"] and nagative.append(f"{self.NEG_EXP}".strip())

        final_negative = self.NEG + " ".join(nagative).lower()

        return (final_prompt, final_negative)
