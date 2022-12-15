# Designing Modern NLP Assignments for 2022
by [Graham Neubig](https://phontron.com) (2022-12-15)

In the past several years, arguably starting with the introduction of
[BERT](https://arxiv.org/abs/1810.04805) in 2018, and further accelerated by
the introduction of [GPT-3](https://arxiv.org/abs/2005.14165) in 2020, the field of
Natural Language Processing has seen huge changes. Up until these developments, there
was a pretty heavy focus on model architecture engineering/programming and training
your own models from scratch.

However, with the introduction of these new models, the focus has shifted to
finetuning these models on downstream tasks (BERT) or even using models as black-boxes
through [prompting](https://arxiv.org/abs/2107.13586) and model access through
APIs. Because of this, this also forced me to think about how I design my assignments
for the Advanced NLP course I teach at CMU.

I'm writing this post to share a little bit of the motivation behind the design of
the assignments, and welcome any teachers of NLP teachers to get in touch to
gneubig at cs.cmu.edu if you'd like to re-use them or have any questions!

## Assignment 1: Build your own BERT

While model architecture engineering is less prominent in the field now, it's still
important to understand how these models work and have basic skills in implementing
neural NLP models in toolkits such as PyTorch. Assignment 1 is
["Build your own BERT"](https://github.com/neubig/minbert-assignment), in which students
are asked to re-implement some parts of the BERT architecture and training algorithm,
read in existing pre-trained model weights, and fine-tune the weights on existing
data for a sentiment classification classification task.
This assignment is done individually.

This attempts to provide the following skills:
1. Programming neural models in PyTorch
2. Understanding how the pre-train and fine-tune paradigm works
3. Understanding the BERT architecture
4. Basic data munging and validation

To go above and beyond the requirements, students can also implement additional training
algorithms such as continued pre-training to aim for higher accuracy.

We set up a submission leaderboard through
[ExplainaBoard](https://explainaboard.inspiredco.ai), which is a tool that allows for
easy construction of NLP-related leaderboards (developed in a collaboration between
CMU and my company Inspired Cognition). If you are interested in using this tool in
your own class, please get in contact and I'll be happy to help you set it up.

## Assignment 2: Building an NLP System from Scratch

Assignment 2 is ["Building an NLP System from Scratch"](https://github.com/neubig/nlp-from-scratch-assignment-2022), where we specify a specific task for
and students (in groups of 2-3) create a system for this task from scratch. For 2022
we chose the task of "Entity Recognition in NLP Papers", but next year it will be
something different.

The most unique part of the assignment is that we **don't give the students any data**
for training or evaluating their systems, and rather only gave them a detailed
description of the [data annotation standard](annotation_standard.md). Because of this,
students need to read the standard carefully, annotate data themselves, and choose the
modeling method that they think is best for the task, and perform evaluation. In
addition, we require that students report how they chose the type and amount of data
to annotate, perform significance testing and error analysis, and do other best
practices in reporting results in a systematic and scientific manner. Submissions
were also accepted through ExplainaBoard.

This attempts to provide the following skills:
1. Carefully reading a task specification and understanding what is required
2. Based on the task specification annotating data for evaluation and training
3. Choosing a model architecture and training algorithm out of the many possible ones
4. Best practices in evaluation and result reporting
5. Teamwork and time management - how do we decide who does what, and do we want to
   spend more time on annotating data or on training a model?

I believe that this assignment is particularly important given (1) the current shifts
in NLP research towards more data-oriented approaches, and (2) the fact that in industry
it's going to be quite common to have to work with data that hasn't been carefully
curated into an appropriate format.

This was the first time doing this assignment, and there were also a number of things
that I think could have been done better:
1. The annotation standard was somewhat underspecified at first, and we had to make
   some changes to it after the fact. This caused trouble for some students as they
   had to make changes to their annotations, so I think it's important to do a very
   good dry run of the assignment with TAs beforehand.
2. We didn't provide an "expected" level of accuracy, so I feel that some groups were
   stressed about whether the accuracy that they achieved was sufficient. In the end
   we settled on a "passing" level of accuracy, then gave credit based on quintiles
   of the group submissions, which I think is fair, but it would have been best to
   decide this in advance.

## Assignment 3: Project Proposal and Baseline Reproduction

Starting in the 3rd assignment, students are free to tackle any task that they like in
groups of 2-3. In Assignment 3, they do a
[survey, a project proposal, and reproduce a baseline](https://phontron.com/class/anlp2022/assignments.html).

This attempts to provide the following skills:
1. Surveying the literature and identifying a task that is interesting and feasible
2. Writing a project proposal that points out a gap in the literature and attempts to
   fill it
3. Understanding the requirements to set up and run code from an existing
   state-of-the-art method

## Assignment 4: Final Project

In the final project, students attempt to implement something new that has not been
done before in the literature, either by proposing novel improvements to an existing
method, by applying existing methods to new varieties of data, or by proposing a new
task or dataset.

This attempts to provide the following skills:
1. Creative and critical thinking about how to make new contributions to the field of
   NLP
2. Implementation of these new ideas (in whatever form they take)
3. Paper writing skills

## Conclusion

I hope that by the end of the class, a student who has attended the lectures and done
the assignments will have the start of a modern toolset that allows them to be a
productive contributor to NLP research or development. What that means now in 2022 is
quite different than what that meant even 5 years ago, and I'm hoping that these
assignments are more reflective of the skills that are needed in the field now!