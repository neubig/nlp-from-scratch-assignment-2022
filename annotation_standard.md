# Scientific Entity Recognition Annotation Standard

This annotation standard is basically complete, but we might add some details until **October 10th** to respond to questions from members of the class.

Here we give an example of how entities should be annotated by your created system.
We use some sentences from the BERT paper as an example: [https://arxiv.org/pdf/1810.04805.pdf](https://arxiv.org/pdf/1810.04805.pdf).

Here the entities that need to be annotated.

* [MethodName](#method-name)
* [HyperparameterName](#hyperparameter-name)
* [HyperparameterValue](#hyperparameter-value)
* [MetricName](#metric-name)
* [MetricValue](#metric-value)
* [TaskName](#task-name)
* [DatasetName](#task-value)

## Method Name

(Tag: MethodName)

Names of the baseline systems and proposed systems, could be: 

1. The main description of the method, such as: "Bidirectional Encoder Representations from Transformers". 
2. The abbreviated form (a cute name) of their method, such as: BERT.

For these systems in comparison, you should only annotate the names that, themselves or their abbreviated forms, are identical to what appears in table entries. 

Meanwhile, other standalone methods, such as the main system proposed by a relevant work, should also be labeled, even though they are not among the comparison list of the given paper. 

_Tricky cases_:
* "Human performance" is also be labeled as a MethodName.

_Example_: 

```
we O
improve O
the O
fine O
- O
tuning O
based O
approaches O
by O
proposing O
BERT B-MethodName
: O
Bidirectional B-MethodName
Encoder I-MethodName
Representations I-MethodName
from I-MethodName
Transformers I-MethodName
. O
```

## Hyperparameters

### Hyperparameter Name

(Tag: HyperparameterName)

Names of the hyper-parameters mentioned in the paper, that cannot be inferred while fitting models to the training data. This could either be the full description (e.g., "number of layers"), or the mathematical notation (e.g., "L"). 

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
( O
i.e. O
, O
Transformer O
blocks O
) O
as O
L B-HyperparameterName
, O
the O
hidden B-HyperparameterName
size I-HyperparameterName
as O
H B-HyperparameterName
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

## Task Name

(Tag: TaskName)

Name of the task that the methods are evaluated on, e.g.: "Named Entity Recognition". 

You should annotate task names that could inform the reader of problem being solved.
Good examples include "Natural Language Inference" and "Object Detection". 
Names that do not provide information about what task is being solved "task A" should not be annotated. 

_Example_: 

```
MNLI B-DatasetName
Multi B-DatasetName
- I-DatasetName
Genre I-DatasetName
Natural I-DatasetName
Language I-DatasetName
Inference I-DatasetName
is O
a O
large O
- O
scale, O
crowdsourced O
entailment B-TaskName
classification I-TaskName
task I-TaskName
```

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

