# CMU Advanced NLP Assignment 2: End-to-end NLP System Building

by Emmy Liu, Zora Wang, Kenneth Zheng, Lucio Dery, Abhishek Srivastava, Kundan Krishna, Graham Neubig


So far in your machine learning classes, you may have experimented with standardized tasks and datasets that were provided and easily accessible. 
However, in the real world, NLP practitioners often have to solve a problem from scratch, which includes gathering and cleaning data, annotating 
the data, choosing a model, iterating on the model, and possibly going back to change the data. For this assignment, you'll get to experience this full process.

Please note that you'll be building your own system end-to-end for this project, and **there is no starter code**. You must collect your own data 
and train a model of your choice on the data. We will be releasing an unlabeled test dataset a few days before the assignment deadline, and you 
will run your already-constructed system over this data and submit the results.
We also ask you to follow several experimental best practices, and describe the result in your report.

The full process will include:

1. [Understand the task specification](#task-specification)
2. [Collect raw data](#collecting-raw-data)
3. [Annotate test and training data for development](#annotating-data)
4. [Train and test models using this data](#training-and-testing-your-model)
5. ["Deploy" your System](#system-deployment)
6. [Write your report](#writing-report)

## Task Specification

For this assignment, you'll be working on the task of *scientific entity recognition*, specifically in the domain of NLP papers from recent NLP conferences (e.g. ACL, EMNLP, and NAACL).
Specifically, we will ask you to identify entities such as task names, model names, hyperparameter names and their values, and metric names and their values in these papers. 

**Input:**
The input to the model will be a text file with one sentence per line.
The text will *already be tokenized* using the [spacy](https://spacy.io/api/tokenizer/) tokenizer, and you should not change the tokenization.
An example of the input looks like this:
```
Recent evidence reveals that Neural Machine Translation ( NMT ) models with deeper neural networks can be more effective but are difficult to train .
```

**Output:** 
The output of your model should be a file in [CoNLL format](https://simpletransformers.ai/docs/ner-data-formats/#text-file-in-conll-format), with one token per line, a tab, and then a corresponding tag.

Please refer to these [input](bert.txt) and [output](bert.conll) files for more specific examples. 

There are seven varieties of entity: `MethodName`, `HyperparameterName`, `HyperparameterValue`, `MetricName`, `MetricValue`, `TaskName`, `DatasetName`.
Details of these entities are included in the [annotation standard](annotation_standard.md), which you should read and understand carefully.

## Collecting Raw Data

You will next need to collect raw text data that can be used as inputs to your models.
This will consist of three steps.

### Obtaining PDFs of Scientific Papers

First, you will need to obtain PDFs of NLP papers that can serve as your raw data source. The best source for
recent NLP papers is the [ACL Anthology](https://aclanthology.org/). We recommend that you write a web-scraping script to find and download PDF links from here. 
Other good sources for data include [ArXiv](https://arxiv.org/) and [Semantic Scholar](https://www.semanticscholar.org/), both 
of which have web APIs which you can query to get the IDs and corresponding paper PDFs for various scientific papers.

### Extracting Sentences Line-by-line

In order to process the text from the PDF files, you will first need to convert it into plaintext. This is a popular problem and there are multiple libraries designed for this task. Some of them are:
[PyPDF2](https://pypdf2.readthedocs.io/en/latest/)
[SciPDF Parser](https://github.com/titipata/scipdf_parser)
[AllenAI Science Parse](https://github.com/allenai/science-parse)
[AllenAI Science Parse v2](https://github.com/allenai/spv2)

You do not need to extract text/numbers from tables and figures.

### Tokenizing the Data

As noted above, the inputs to your model will be tokenized using the [spacy](https://spacy.io/api/tokenizer/) tokenizer, so you should probably also tokenize the input data using this tokenizer as well.
Once you have done this, you should have a significant amount of raw data in the same input format as described above.

## Annotating Data

Next, you will want to annotate data for two purposes: testing/analysis and training.

_The testing/analysis data_ will be the data that you use to make sure that your system is working properly.
In order to do so, you will want to annotate enough data so that you can get an accurate idea of how your system is doing, and if any improvements to your system are having a positive impact.
Some guidelines:
* **Domain Relevance:** Your test data should be similar to the data that you will finally be tested on, so we recommend that you create it from NLP papers from recent NLP conferences (e.g. ACL, EMNLP, and NAACL).
* **Size:** Your test data should be large enough to distinguish between good and bad models. If you want some guidelines about this, please take a look at [this paper](https://arxiv.org/abs/2010.06595).

For annotation, please see the separate doc that details [annotation interfaces](annotation_interface.md) that you can use.

_The training data_ is a bit more flexible, you could possibly:
* Annotate it yourself manually through the same method as the test set.
* Do some sort of automatic annotation/data augmentation.
* Use other existing datasets for multi-task learning.


## Training and Testing Your Model

In order to _train_ your model, we highly suggest using pre-existing toolkits such as [HuggingFace Transformers](https://huggingface.co/docs/transformers/index).
You can read the tutorial on [token classification](https://huggingface.co/course/chapter7/2) which would be a good way to get started.

Because you will probably not be able to create a large dataset specifically for this task in the amount of time allocated, we strongly suggest that you use the knowledge that you have learned in this class to efficiently build a system.
For example, you may think about ideas such as:
1. Pre-training on a different task and fine-tuning
2. Multi-task learning, training on different tasks at once
3. Using prompting techniques

In order to _test_ your model, you will want to use an evaluation script.
Some options include:
* The [explainaboard_client library](https://github.com/neulab/explainaboard_client/issues), where you can use your created test data as a custom dataset.
* [seqeval](https://github.com/chakki-works/seqeval) a Python library for evaluating sequence labeling.

## System Deployment

The final "deployment" of your model will consist of running your model over a private test set (text only) and submitting your results to us.
You should try to finish building your system before this set is released, and basically not rely on it for model training or testing.
The test set will be released shortly (2-3 days) before the final submission deadline.

When you are done running your system over this data, you will:
1. submit the results to **ExplainaBoard** through a submission script similar to the one that you used in the first assignment.
2. submit any testing or training data that you created

Both of these will be due by **October 26**, and we will be releasing detailed scripts/formats shortly.

## Writing Report

We will ask you to write a report detailing some things about your system creation process (in the grading criteria below).

There will be a 7 page limit for the report, and there is no required template. However, we encourage you to use the [ACL template](https://github.com/acl-org/acl-style-files).

This will be due **October 31st** for submission via **Canvas**.


## Grading

The following points are derived from the "deployment" of the system:

* Your group submits testing/training data of your creation (**20 points**)
* Your group submits code for training the system in the form of a github repo. We will not necessarily run your code, but we may look at it, so please ensure that it contains up-to-date code with a README file outlining the steps to run it. (**20 points**)
* Points based on performance of the system on the output of the private test set (**10 points** for non-chance performance, plus **0 up to 10 points** based on level of performance)

The exact number of points assigned for a certain level of performance will be determined based on how well the class's models perform.

The following points are derived from the report:

* You report how the data was created. Please include the following details (**10 points**)
  - How did you obtain the raw PDFs, and how did you decide which ones to obtain?
  - How did you extract text from the PDFs?
  - How did you tokenize the inputs?
  - What data was annotated for testing and training (what kind and how much)?
  - How did you decide what kind and how much data to annotate?
  - What sort of annotation interface did you use?
  - For training data that you did not annotate, did you use any extra data and in what way?
* You report model details (**10 points**)
  - What kind of methods (including baselines) did you try? Explain at least two variations (more is welcome). This can include which model you used, which data it was trained on, training strategy, etc.
  - What was the justification for trying these methods?
* You report raw numbers from experiments (**10 points**)
  - What was the result of each model that you tried on the testing data that you created?
  - Are the results statistically significant? You can use the (a) built-in significance tests of ExplainaBoard, or (b) [a separate script](https://github.com/neubig/anlp-code/blob/main/02-bowclassifier/bowclassifier.ipynb) such as the one shown in class.
* Comparative quantitative/qualitative analysis (**10 points**)
  - Perform a comparison of the outputs on a more fine-grained level than just holistic accuracy numbers, and report the results. For instance, you may measure various models' abilities to perform recognition of various entities. ExplainaBoard provides some functionality by default, but you can also do so by writing customized analysis scripts.
  - Show examples of outputs from at least two of the systems you created. Ideally, these examples could be representative of the quantitative differences that you found above.
