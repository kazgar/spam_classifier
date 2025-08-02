# SPAM Classifier

This repository is my take on the spam classification problem. Data used in this project is
from https://spamassassin.apache.org/. Working on this is part of my journey through <i>Hands-On Machine Learning with Scikit-Learn
and Tensorflow</i> book by Geron Aurelien.

### Dataset

______________________________________________________________________

The dataset contains multiple files,

- `ham_easy_<i>` and `ham_hard_<i>`: containing 'normal' emails
- `spam_<i>`: (you guessed it) containing examples of spam emails.

The dataset is fairly big (>10k emails), thus I didn't include it
in this repository.

______________________________________________________________________

### Approach

The biggest challenge in this problem is (surprise, surprise) - how to parse and encode emails such that those encodings
can encapsulate features that distinguish spam emails from regular ones. I chose rather simple approach, namely <b>Bag of Words (BoW)</b>, the count-based version).

In short:

1. Emails (only the body) were parsed—the parsing consisted of:
   - substituting all multiple newline characters (`"\n\n...\n"`) with space `" "` characters;
   - substituting all URLs with `"URL "` strings;
   - substituting all email addresses with `"EMAIL "` strings;
   - removing all punctuation;
   - stemming all leftover words → `"running"` would be transformed to `"run"` and so on...;
   - finally, all words were converted to lowercase.
2. Vocabulary was created from all words from all emails after parsing.
3. Emails were transformed to <b>Bag of Words</b> arrays. For example, if the vocabulary consisted of only 4 words:
   `["hello", "dog", "jumped", "bye"]`, then an email `"Hello hello! bye BYE .dog,,,"` would be converted to a `"[2, 1, 0, 2]"` array.
4. Lastly, a logistic regression model was trained and evaluated against the validation and test sets.

______________________________________________________________________

### Results

`GridSearchCV` from `scikit-learn` library was used to tune logistic regression parameters with 10-fold cross-validation. Model with the best
parameters was trained and evaluated on the test set. Overall model performance was solid, especially considering the simplicity of logistic regression:

- <b>Accuracy:</b> 97.58%
- <b>Precision:</b> 98.04%
- <b>Recall:</b> 94.86%

The relatively lower recall indicates that the model is more likely to **miss actual spam** (i.e., classify spam emails as normal).
However, the high precision shows that when the model predicts an email as spam, it's usually correct—minimizing false positives.
