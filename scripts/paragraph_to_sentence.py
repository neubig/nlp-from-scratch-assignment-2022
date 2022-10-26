import argparse
from nltk.tokenize import sent_tokenize

if __name__ == '__main__':
    '''
    This script converts the released test set for this assignment
    from paragraph-segmented to sentence-segmented, as there was some
    confusion in the original assignment directions.

    To use, run this script to generate anlp-sciner-test-sentences.txt.
    Then, run your model over this sentence file to get its outputs
    in CoNLL format. Finally, run sentence_to_paragraph.py with your
    CoNLL outputs to remove the extra newlines and re-combine the
    sentences into paragraphs.

    While running a model trained on sentence-level inputs on paragraphs
    would probably still work fine, segmenting the test set in this way
    to match the trained model may improve performance.

    This uses the NLTK sentence tokenizer, which is far from perfect
    (over-splits a lot on things like inline references), but should
    be sufficient for this assignment.
    '''

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--infile', default='../data/anlp-sciner-test.txt',
        help='The provided test set file')
    parser.add_argument('-o', '--outfile', default='../data/anlp-sciner-test-sentences.txt',
        help='The output file for sentence-segmented data')
    args = parser.parse_args()

    sentences = []
    with open(args.infile) as f:
        for line in f.readlines():

            # tokenize each paragraph into sentences
            sentences_from_paragraph = sent_tokenize(line)
            sentences.extend(sentences_from_paragraph)

    # hacky fix for edge cases where the sentence tokenizer
    # splits a token in our test set
    problem_indices = [2522, 2528, 2813]
    for i in problem_indices:
        sentences[i:i+2] = [''.join(sentences[i:i+2])]

    # fix for edge cases where sentences are incorrectly
    # split after "et al .", "e.g.", or "i.e."
    # includes hacky fix for edge cases where i.e. shouldn't be merged
    cleaned_sentences = []
    for i, sentence in enumerate(sentences):
        if i == 0:
            cleaned_sentences.append(sentence)
            continue

        prev_sentence = cleaned_sentences[-1]
        if (prev_sentence[-7:] == 'et al .'
                or prev_sentence[-4:] == 'e.g.'
                or (prev_sentence[-4:] == 'i.e.' and i not in [2077, 2089])):
            cleaned_sentences[-1] += (' ' + sentence)

        else:
            cleaned_sentences.append(sentence)

    # write to output file
    with open(args.outfile, 'w') as f:
        f.write("\n".join(cleaned_sentences))
