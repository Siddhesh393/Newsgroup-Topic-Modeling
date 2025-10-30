# Topic Modeling on Newsgroup Dataset

## Project Overview

This project focuses on topic modeling, a technique in natural language processing (NLP) to identify the underlying topics in a collection of documents. The Newsgroup dataset, a popular dataset for text classification and clustering, serves as the basis for this project. The project explores two different models for topic modeling: **Latent Dirichlet Allocation (LDA)** and **Bidirectional Encoder Representations from Transformers (BERT)**.

## Dataset

The **Newsgroup dataset** consists of approximately 20,000 newsgroup documents, partitioned into 20 different newsgroups, each corresponding to a specific topic. The dataset is available in scikit-learn's datasets module and can be easily loaded for text processing tasks.

## Methodology

### 1. Data Preprocessing

Before applying any topic modeling technique, the text data undergoes several preprocessing steps:
- **Tokenization:** Splitting the text into individual words or tokens.
- **Stopwords Removal:** Removing common words that do not contribute to the topic modeling (e.g., "the", "and", "is").
- **Lemmatization:** Reducing words to their base or root form.
- **Vectorization:** Converting text data into numerical format (e.g., TF-IDF) for LDA and BERT input.

### 2. Latent Dirichlet Allocation (LDA)

LDA is a generative probabilistic model that assumes each document is a mixture of a small number of topics, and each topic is a mixture of words. LDA helps in identifying the hidden topic structure in the document corpus.

- **Implementation:** The LDA model is implemented using the `Sklearn` library.
- **Hyperparameters:** The number of topics is chosen based on coherence scores and manual inspection of results.
- **Output:** LDA provides a distribution of topics over documents and words over topics, which can be used to interpret the dominant themes.

### 3. BERT for Topic Modeling

BERT is a transformer-based model that generates contextual embeddings for words, capturing the semantic meaning of words in context. For topic modeling, BERT embeddings are clustered using algorithms like K-Means to identify coherent topics.

- **Implementation:** BERT embeddings are generated using the `Sentence-BERT` model, and clustering is performed using the `K-Means` algorithm.
- **Comparison:** The results from BERT are compared with LDA in terms of coherence, interpretability, and computational efficiency.

### 4. Evaluation

The models are evaluated based on:
- **Coherence Score:** Measures the semantic similarity of words within a topic.
- **Human Interpretation:** Manual inspection of topics to assess meaningfulness.
- **Runtime Performance:** Comparison of time taken to train and generate topics.

## Results

- **LDA:** Successfully identified coherent topics but sometimes struggled with capturing context-specific nuances.
- **BERT:** Provided more contextually relevant topics due to its ability to understand word semantics better. However, the choice of clustering algorithm and hyperparameters significantly impacted the results.

## Conclusion

Both LDA and BERT have their strengths in topic modeling. LDA is more traditional and interpretable, while BERT offers better contextual understanding but requires more computational resources and fine-tuning. This project demonstrates the application and comparison of these models on the Newsgroup dataset.

## Dependencies

- Python 3.7+
- Scikit-learn
- Transformers
- Sentence-Transformers
- Pandas
- Numpy

## Installation

Clone the repository and install the required packages:

```bash
git clone https://github.com/Siddhesh393/Topic-Modelling-Project.git
cd Topic-Modelling-Project/lda-bert


