# ComfyUI Easy Pony

This custom node is an abstrtaction of a helper node used in one of my other `currently un-published` custom nodes. It was created
to simplify the process of adding tscoring other attributes when prompting with `Pony` models.

> [!NOTE]
> I am not a prolific user of Pony models; This node was created to assist in converting prompts for one of my other custom nodes. YMMV
> in terms of the quality of the prompts generated.


## Installation

### Install from ComfyUI Manager

- Type `EasyPony` on the search bar of [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager).
- Click the install button.

### Manual Installation

To install `ComfyUI-EasyPony`:

1. Open the terminal in the ComfyUI `custom_nodes` folder.
2. Run: `git clone https://github.com/itsjustregi/ComfyUI-EasyPony`.
3. Restart ComfyUI.

### Update

To update `comfyui-ComfyUI-EasyPony`:

1. Open the terminal in the `comfyui-ComfyUI-EasyPony` folder.
2. Run: `git pull`.
3. Restart ComfyUI.

Parameters with null value (-) will not be included in the generated prompt.

## Practical Advice

Easy Pony is a helper node that simplifies the process of adding scoring and other attributes to the core when prompting with Pony models. Model selection determines the quality of the images from the prompt. The effectiveness of the parameters depends on the quality of the checkpoint used.

## Notes

The effectiveness of the parameters depends on the quality of the checkpoint used.

## License

This project is licensed under the MIT License.