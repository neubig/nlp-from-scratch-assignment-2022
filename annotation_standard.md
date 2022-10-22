# Scientific Entity Recognition Annotation Standard

This annotation standard is basically complete, but we might add some details until **October 10th** to respond to questions from members of the class.

Here we give an example of how entities should be annotated by your created system.
We use some sentences from the BERT paper as an example: [https://arxiv.org/pdf/1810.04805.pdf](https://arxiv.org/pdf/1810.04805.pdf).

**Entities:** Here the entities that need to be annotated.

* [MethodName](#method-name)
* [HyperparameterName](#hyperparameter-name)
* [HyperparameterValue](#hyperparameter-value)
* [MetricName](#metric-name)
* [MetricValue](#metric-value)
* [TaskName](#task-name)
* [DatasetName](#task-value)

**Annotated Sections:**
In the test set most paper textual content will be included, such as:

* Paper titles
* Section headers
* Main textual paragraphs of the paper
* Appendices

And the following will NOT be included:
* Tables, figures, and captions
* The "references" section

So you may want to perform any annotation you do on the parts of the paper that will be included in the test set, as that will likely result in better final performance.

## Method Name

(Tag: MethodName)

Names of the baseline and proposed systems, could be:

1. The main description of the method, such as: "Bidirectional Encoder Representations from Transformers". 
2. The abbreviated form (a cute name) of their method, such as: BERT.

In most cases, these are the system names that appear as table entries in their abbreviated forms.

For MethodName, you should only annotate **(1)** the proposed system, **(2)** the baselines for the proposed system, **(3)** other standalone methods for the same task(s) tackled by the proposed system.

_Example_: 

```
Our O
proposed O
model O
BERT B-MethodName
(
Bidirectional B-MethodName
Encoder I-MethodName
Representations I-MethodName
from I-MethodName
Transformers I-MethodName
)
outperforms O
ELMo B-MethodName
, O
which O
is O
based O
on O
BiLSTMs O
, O
on O
multiple O
tasks O
. O
```

_Tricky cases_:
* In the above example, "BiLSTMs" is not annotated as it is neither the proposed system ("BERT") nor a direct baseline to the proposed system ("ELMo").
* "Human performance" should also be labeled as MethodName if it is directly compared to the proposed system.
* In phrases like "the pretrained BERT model", only the specific method name "BERT" should be annotated.

## Hyperparameters

### Hyperparameter Name

(Tag: HyperparameterName)

Names of the hyper-parameters mentioned in the paper, that cannot be inferred while fitting models to the training data. This could either be the full description (e.g., "number of layers"), or the mathematical notation (e.g., "L").

_Tricky cases_:
* "train/dev/test split ratio" should be labeled as HyperparameterName.

### Hyperparameter Value

(Tag: HyperparameterValue)

Value of the hyper-parameters, such as: "12" for L, "768" for H, etc.

You might want to include the units of numbers, such as labeling "110M" instead of "110". Note that a lot of hyper-parameters descriptions are located in the appendices.

_Example_: 

```
we O
denote O
the O
number B-HyperparameterName
of I-HyperparameterName
layers I-HyperparameterName
as O
L B-HyperparameterName
, O
the O
hidden B-HyperparameterName
size I-HyperparameterName
as O
H B-HyperparameterName
and O
learning B-HyperparameterName
rate I-HyperparameterName
as O
θ B-HyperparameterName
( O
θ B-HyperparameterName
is O
set O
to O
0.001 B-HyperparameterValue
) O
```

## Evaluation Metrics

### Metric Name

(Tag: MetricName)

Names of the evaluation metrics being used for method evaluation. 

You need only annotate the name of the metric and not include other context. For example, given a string "the accuracy on test set" you should only annotate "accuracy".

Some metrics are often abbreviated, e.g. using "acc." for "accuracy". The abbreviations are also considered valid metric names.

_Example_: 

```
Spearman B-MetricName
correlations I-MetricName
are O
reported O
for O
STS B-DatasetName
- I-DatasetName
B I-DatasetName
, O
and O
accuracy B-MetricName
scores O
are O
reported O
for O
the O
other O
tasks O
. O
```

*Tricky Cases:*

- For a phrase like "macro F1 score", annotate only "macro F1" (i.e. the shortest part of the phrase that fully specifies the metric).
- A p-value is not considered an evaluation metric and shouldn't be annotated.

### Metric Value

(Tag: MetricValue)

Evaluation results of methods on each metric. Many analyses use relative metric values (+5.3%) instead of absolute values (45.6%), these relative values should also be annotated as valid metric values. 

Although these are often reported in tables, we do not require parsing and annotation of table content. We also do not require annotation of the mapping relations between models, datasets, and metrics. You might find it beneficial if doing them nonetheless. 

_Example_:

```
BERTLARGE B-MethodName
obtains O
a O
score O
of O
80.5 B-MetricValue
```

_Tricky Cases_:
* Be sure to include % at the end of the number, for example, annotating "45.6%" instead of "45.6", since they would represent different values.
* When talking about an increase such as "20% improvement", only "20%" should be annotated, not "improvement".

## Task Name

(Tag: TaskName)

Name of the task(s) that the current work is evaluated on, e.g.: "Named Entity Recognition".

You should not annotate,
1. Tasks that are mentioned but not evaluated with the proposed work. 
2. Names that do not provide information about what task is being solved: "task A", "subtask A" should not be annotated.

_Example_: 

```
BERT B-MethodName
outperforms O
other O
methods O
on O
natural B-TaskName
language I-TaskName
inference I-TaskName
( O
NLI B-TaskName
) O
, O
question B-TaskName
answering I-TaskName
. O

It O
was O
not O
evaluated O
on O
machine O
translation O
. O
```

_Tricky Cases_:
* In the above example, machine translation is not annotated since the proposed work ("BERT") is not evaluated on that task.
* (Pre-)training objectives such as "Masked Language Modeling (MLM)", "Next Sentence Prediction (NSP)", and "Cloze" should not be labeled as TaskName unless the proposed work is evaluated on those tasks.

## Dataset Name

(Tag: DatasetName)

Name of the dataset of target tasks. Some works evaluate on dataset benchmarks (i.e., a collection of datasets) such as GLUE. You could also label the benchmark name as a dataset name.

_Example_: 

```
F1 B-MetricName
scores O
are O
reported O
for O
QQP B-DatasetName
and O
MRPC B-DatasetName
```

*Tricky Cases*:

- In phrases like "the CoNLL dataset", only annotate "CoNLL" (i.e. the shortest part of the phrase that uniquely identifies the dataset)
