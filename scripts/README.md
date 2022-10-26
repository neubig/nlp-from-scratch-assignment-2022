This directory contains scripts to convert the test set from paragraph-segmented into sentence-segmented, and model outputs from sentence-segmented back to paragraph-segmented.

## Usage

From the `scripts/` directory, running `python paragraph_to_sentence.py` (with default arguments) will generate `data/anlp-sciner-test-sentences.txt`, which is the test set segmented into sentences. This script requires the NLTK python package since we use its sentence tokenizer. You can then run your model over this data file to generate outputs in CoNLL format.

Then, running `python sentence_to_paragraph.py -i your_model_outputs.conll` (with other arguments default) will generate `data/output.conll`, which reformats your model outputs to paragraph-segmented which matches our expected evaluation format.

Note that these scripts expect the `data/` directory to be the same as this repository, so if your data files are moved please change the arguments to point to the correct files. For more details, see the docstrings and argparse descriptions within each script.
