# Evaluation and Submission

Your systems will be scored based on F1 score.

This page explains how you can (1) evaluate your own test-set outputs, and (2) submit 
your assignment 2 final outputs to ExplainaBoard for scoring.

## Preparation

In order to prepare for evaluation, you will want to create your outputs in two-column
CoNLL format, such as the example in [bert.conll](bert.conll).

You will also want to install version 0.0.9 of
[explainaboard_client](https://github.com/neulab/explainaboard_client) which will be
used for system submission, and can also be used for your own evaluation if you choose.
```shell
pip install --upgrade --force-reinstall explainaboard_client==0.0.9 explainaboard_api_client==0.2.8
```

Set your username and API key for the client:
```shell
export EB_USERNAME="[your username]"
export EB_API_KEY="[your API key]"
````

## Evaluation on your Test Set

To evaluate on your own test set you will need two files:
* One with manually annotated gold-standard labels,
  e.g. [bert.conll](bert.conll)
* Another for your system, let's call it `anlp_andrewid_mysys1`, (you can replace
  `andrewid` with your andrew ID). e.g. [bert-mysys1.conll](bert-mysys1.conll)

In order to evaluate, you can do the following:
```shell
python -m explainaboard_client.cli.evaluate_system \
  --username $EB_USERNAME \
  --api-key $EB_API_KEY \
  --task named-entity-recognition \
  --system-name anlp_andrewid_mysys1 \
  --custom-dataset-file bert.conll \
  --custom-dataset-file-type conll  \
  --system-output-file bert-mysys1.conll \
  --system-output-file-type conll \
  --source-language en
```

There are also plenty of other alternatives such as using
[seqeval](https://github.com/chakki-works/seqeval), which can be run offline, or using
the [explainaboard_client Python API](https://github.com/neulab/explainaboard_client/blob/main/docs/python_api/introduction.md),
which can be called directly from Python.

## Performing Analysis

As part of your report, you will need to perform a variety of analysis on your test
results.

### Significance Testing

You will want to test whether the difference in results between two systems is
significant. As described in class, an appropriate method to do this is through
paired bootstrapping tests.

If you are using ExplainaBoard for evaluation, you can select the checkboxes next to two
systems on the web interface and click "Pairwise Analysis" and it will report
pairwise significance tests between the models.

If you are using seqeval or another script for evaluation, you can implement pairwise
significance testing yourself using a separate script mirroring
[the one shown in class for text classification](https://github.com/neubig/anlp-code/blob/main/02-bowclassifier/bowclassifier.ipynb).

### Quantitative/Qualitative Analysis

In order to perform *quantitative* analysis of the results to better understand the
trends  of each system, you can do things like:
* Calculate which *types of entities* are getting better or worse accuracy
* Calculate whether the model is doing better on *capitalized or uncapitalized* entities
* Calculate whether the *length of the entity* has a significant effect on accuracy

These and other analyses are included in the ExplainaBoard web interface, or
alternatively you can write custom analysis scripts to do the analysis offline.

You will also want to actually look at the outputs and get an idea of what they look
like. If you do this after a certain amount of quantitative analysis, you can also look
for qualitative examples that match your quantitative analysis. For instance, if you
notice that your system is underperforming on a particular entity type, then you can
focus your qualitative analysis on that entity type..

## Submission of Final Outputs

To run on the final test set, you will generate an output file in a similar format as
above, and run the following command.

**Important:** make sure you write the submission name as `anlp_andrewid_XXX` with your
actual Andrew ID because this is how we will identify your submission. `XXX` is an
arbitrary string specifying your system name.

```shell
python -m explainaboard_client.cli.evaluate_system \
  --username $EB_USERNAME \
  --api-key $EB_API_KEY \
  --task named-entity-recognition \
  --system-name anlp_andrewid_mysys1 \
  --dataset cmu_anlp \
  --sub-dataset sciner \
  --split test \
  --system-output-file sciner-mysys1.conll \
  --system-output-file-type conll \
  --shared-users neubig@gmail.com \
  --source-language en
```

