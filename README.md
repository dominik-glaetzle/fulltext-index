# Fulltext Index – Text Processing and Statistics

This project is the first step towards building a full-text index. Over the next few weeks, the index will be constructed step by step. The goal of this phase is to develop a system for preprocessing and analyzing a given text corpus.

## 🔍 Project Description

In this initial stage, we implement methods for:

- Reading text data from multiple files  
- Tokenizing and preprocessing the text (e.g., lowercasing, removing punctuation)  
- Computing statistical measures over the corpus  

## 📂 Corpus Structure

The corpus is built from a set of plain text files containing the texts to be indexed. All files are automatically read and processed as part of the pipeline.

## 🛠️ Processing Steps

1. **Reading Input Files**  
   All text files in the specified directory are read and combined into a single corpus.

2. **Text Preprocessing**  
   - Remove all punctuation  
   - Convert all tokens to lowercase  
   - Tokenize the text (using NLTK)

3. **Corpus Statistics**  
   The following statistics are computed for the given corpus:  
   - Total number of tokens  
   - Vocabulary size (number of unique tokens)  
   - Token frequency distribution