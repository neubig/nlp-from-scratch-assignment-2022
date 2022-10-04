# Annotation Interface

When annotating structured data, you can do it in several ways. You can annotate plain-text data, but it is often easier to use an annotation interace.

## Annotating Plain Text

Given that you will want text in CoNLL format, you can always write a simple script to convert your input text into something that looks like the output format, but with "O" for each line, e.g.

```
BERT O
got O
an O
F1 O
score O
of O
50 O
. O

RoBERTa O
...
```

and manually annotate the tags


```
BERT B-MethodName
got O
an O
F1 B-MetricName
score I-MetricName
of O
50 B-MetricValue
. O

RoBERTa B-MethodName
...
```

## Annotating with an Interface

It may be easier to use an annotation interface.
One good one that we can recommend is [https://github.com/heartexlabs/label-studio](https://github.com/heartexlabs/label-studio).

**1. Installation**

Install the label-studio following the instructions here: 

If you are using pip installation, make sure your ‘python >=3.7 &lt;=3.9’.

Note that for Mac M1 users, try installing using <span style="text-decoration:underline;">docker</span> if other methods (e.g., pip) do not work. 

**2. Prepare your file**


* in TXT format

Results on selected GLUE tasks are shown in Table 6 .

In this table , we report the average Dev Set accuracy from 5 random restarts of fine - tuning .



* in JSON format

[

	{‘text’: "Results on selected GLUE tasks are shown in Table 6 .", "paperid": XXX}, 

	{‘text’: "In this table , we report the average Dev Set accuracy from 5 random restarts of fine - tuning .", "paperid": XXX}, 

	… … 

]

Note that your text should be pre-tokenized. The text field should contain whitespace-separated tokens, instead of raw (un-tokenized) sentences.

**3. An Example Annotation**

Start your label-studio, they go to the link prompt ([http://0.0.0.0:8080](http://0.0.0.0:8080/) by default). 

Log in to your account, click `create` on the top-right corner to create a new project: (1) specify the details in the `Project Name` tab, (2) upload your prepared dataset in the `Data Import` tab, (3) in the `Labeling Setup` tab, go to "Natural Language Processing" -> "Named Entity Recognition" task, then set up your labels like this: (you can copy-paste this into the "add label names" section. Blank spaces in name tags are removed for simplicity when parsing the annotated files. 



* MethodName
* HyperparameterName
* HyperparameterValue
* MetricName
* MetricValue
* TaskName
* DatasetName



![interface_0](https://user-images.githubusercontent.com/19615708/193353042-1314f8b2-12ab-4697-ae5d-762c18773635.png)


**4. Annotation**

Click on the label, then select the text span you want to annotate: 

![annotation_example](https://user-images.githubusercontent.com/19615708/193353252-385174c9-7244-449c-a932-421ed04ee317.png)

Click `Submit` when you finished each sample. You can also modify your annotations and `Update` after submission. 

When you finished your annotation, you can export the results. We recommend you use the "CONLL2003" format, where you get each line containing a token and its annotated label separated by whitespaces. 

However, the "CONLL2003" format contains extra columns (the middle two). To match our output format, you should remove them and only keep the token and the annotated tags. 

**Additional References**:

official documentation: [https://labelstud.io/guide/](https://labelstud.io/guide/) 

**Other Annotation Platforms**:

* brat: [https://github.com/nlplab/brat](https://github.com/nlplab/brat) 
* doccano: [https://github.com/doccano/doccano](https://github.com/doccano/doccano)
After annotating, please export your training data in CoNLL format.

