{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "caption.ipynb",
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "## Image Caption Generator \n",
        "\n",
        "We are going to use Transformers model to generate caption from an Image.\n",
        "\n",
        "### Installation\n",
        "\n",
        "\n",
        "\n",
        "1.   Transformers\n",
        "2.   Pytorch\n",
        "3. Image \n",
        "\n",
        "For installation, please do pip install package_name\n",
        "\n",
        "In Colab, Pytorch comes preinstalled and same goes with PIL for Image. You will only need to install **transformers** from Huggingface.\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "dsK2_BMGrMwt"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install transformers"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cYLlSVpnnpjr",
        "outputId": "5ed9e710-7b4e-4f8e-f6b3-5712b99e2f4e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting transformers\n",
            "  Downloading transformers-4.20.1-py3-none-any.whl (4.4 MB)\n",
            "\u001b[K     |████████████████████████████████| 4.4 MB 7.8 MB/s \n",
            "\u001b[?25hRequirement already satisfied: filelock in /usr/local/lib/python3.7/dist-packages (from transformers) (3.7.1)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.7/dist-packages (from transformers) (2.23.0)\n",
            "Requirement already satisfied: tqdm>=4.27 in /usr/local/lib/python3.7/dist-packages (from transformers) (4.64.0)\n",
            "Collecting pyyaml>=5.1\n",
            "  Downloading PyYAML-6.0-cp37-cp37m-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl (596 kB)\n",
            "\u001b[K     |████████████████████████████████| 596 kB 51.1 MB/s \n",
            "\u001b[?25hRequirement already satisfied: numpy>=1.17 in /usr/local/lib/python3.7/dist-packages (from transformers) (1.21.6)\n",
            "Collecting huggingface-hub<1.0,>=0.1.0\n",
            "  Downloading huggingface_hub-0.8.1-py3-none-any.whl (101 kB)\n",
            "\u001b[K     |████████████████████████████████| 101 kB 13.7 MB/s \n",
            "\u001b[?25hRequirement already satisfied: regex!=2019.12.17 in /usr/local/lib/python3.7/dist-packages (from transformers) (2022.6.2)\n",
            "Collecting tokenizers!=0.11.3,<0.13,>=0.11.1\n",
            "  Downloading tokenizers-0.12.1-cp37-cp37m-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (6.6 MB)\n",
            "\u001b[K     |████████████████████████████████| 6.6 MB 37.2 MB/s \n",
            "\u001b[?25hRequirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.7/dist-packages (from transformers) (21.3)\n",
            "Requirement already satisfied: importlib-metadata in /usr/local/lib/python3.7/dist-packages (from transformers) (4.11.4)\n",
            "Requirement already satisfied: typing-extensions>=3.7.4.3 in /usr/local/lib/python3.7/dist-packages (from huggingface-hub<1.0,>=0.1.0->transformers) (4.1.1)\n",
            "Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in /usr/local/lib/python3.7/dist-packages (from packaging>=20.0->transformers) (3.0.9)\n",
            "Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.7/dist-packages (from importlib-metadata->transformers) (3.8.0)\n",
            "Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.7/dist-packages (from requests->transformers) (2.10)\n",
            "Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /usr/local/lib/python3.7/dist-packages (from requests->transformers) (1.24.3)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.7/dist-packages (from requests->transformers) (2022.6.15)\n",
            "Requirement already satisfied: chardet<4,>=3.0.2 in /usr/local/lib/python3.7/dist-packages (from requests->transformers) (3.0.4)\n",
            "Installing collected packages: pyyaml, tokenizers, huggingface-hub, transformers\n",
            "  Attempting uninstall: pyyaml\n",
            "    Found existing installation: PyYAML 3.13\n",
            "    Uninstalling PyYAML-3.13:\n",
            "      Successfully uninstalled PyYAML-3.13\n",
            "Successfully installed huggingface-hub-0.8.1 pyyaml-6.0 tokenizers-0.12.1 transformers-4.20.1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "qrKcl2XWnaT8"
      },
      "outputs": [],
      "source": [
        "from transformers import VisionEncoderDecoderModel, ViTFeatureExtractor, AutoTokenizer\n",
        "import torch\n",
        "from PIL import Image"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "model = VisionEncoderDecoderModel.from_pretrained(\"nlpconnect/vit-gpt2-image-captioning\")\n",
        "feature_extractor = ViTFeatureExtractor.from_pretrained(\"nlpconnect/vit-gpt2-image-captioning\")\n",
        "tokenizer = AutoTokenizer.from_pretrained(\"nlpconnect/vit-gpt2-image-captioning\")\n",
        "\n",
        "device = torch.device(\"cuda\" if torch.cuda.is_available() else \"cpu\")\n",
        "model.to(device)\n",
        "\n",
        "\n",
        "\n",
        "max_length = 16\n",
        "num_beams = 4\n",
        "gen_kwargs = {\"max_length\": max_length, \"num_beams\": num_beams}\n",
        "def predict_step(image_paths):\n",
        "  images = []\n",
        "  for image_path in image_paths:\n",
        "    i_image = Image.open(image_path)\n",
        "    if i_image.mode != \"RGB\":\n",
        "      i_image = i_image.convert(mode=\"RGB\")\n",
        "\n",
        "    images.append(i_image)\n",
        "\n",
        "  pixel_values = feature_extractor(images=images, return_tensors=\"pt\").pixel_values\n",
        "  pixel_values = pixel_values.to(device)\n",
        "\n",
        "  output_ids = model.generate(pixel_values, **gen_kwargs)\n",
        "\n",
        "  preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)\n",
        "  preds = [pred.strip() for pred in preds]\n",
        "  return preds\n",
        "  \n",
        "predict_step(['sample2.jpg']) # ['a woman in a hospital bed with a woman in a hospital bed']"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "V-jYh878nnpe",
        "outputId": "156ef6f3-4441-4e44-d96c-57060797eb66"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['a man riding a horse on top of a beach']"
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "KIn1BxzCoBXw"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
