## Phishing web urls identification by using text classification techniques

### Problem Statement:

To detect whether the website URL is legitimate or phished based on the URL of the website.

### What is Phishing ?
```
Phishing is a type of cyber attack where attacker do pose/pretend as legitimate or trusted entity to obtain 
sensitive information from targeted individuals. It is a type of social engineering where an attacker sends 
a fraudulent or fake messages that are designed to trick a person into revealing sensitive information.
```
### Dataset Description:
Given a dataset “datathon_train.csv” containing 2 columns and 100860 rows.
1st column contains the raw URL string of the website and other column contains 
binary values 0 and 1 where 0 represents legitimate website and 1 represents 
phished website.

### Approach:
* Tokenization with SpaCy : 
- Spacy is a NLP open source toolkit and library which have prebuilt pipeline for many languages.
- It builds the information extraction, natural language understanding systems and to pre-process text for deep learning.

**Deployement** :
The web app is deployed here : 
<a href="https://phishing-sites-detection.herokuapp.com/"> Phishy Website detection - Heroku</a>

##### About Spacy:
1. When you call nlp on a text, spaCy first tokenizes the text to produce a Doc object.
2. The Doc is then processed in several different steps – this is also referred to as the processing pipeline.
3. The pipeline used by the trained pipelines typically include a tagger, a lemmatizer, a parser and an entity recognizer. 
4. Each pipeline component returns the processed Doc, which is then passed on to the next component.

when we dont call any pipeline in spacy it can give a blanck pipeline which consists of only one stage that is tokenizer.

spacy tokenizer efficiently tokenizes the given text and return tokens.
```
step 1: replace all the "/" with spaces.
step 2: replace all the "." with " . "
step 3: Apply tokenization on the output of the above two steps.

on these generated tokens we applied the following methods to represent them into numerical values (vector reprsentation)
==> Count Vectorization
==> TF-IDF (Term frequency - Inverse Doc. frequency)
```

### Results
```
After applying the above convertions we applied Multinomial NaiveBayes Classifier.
==> Results of Count Vectorization:
      On Validation set :  Accuracy Score : 93%
                           Mathews Corr Coeff : 83.66
                           
      On Test set :        Accuracy Score : 96%
                           Mathews Corr Coeff : 85.9                      
                      
==> Results of TF-IDF :
      On Validation set : Accuracy Score : 94% 
                          Mathews Corr Coeff : 82.3
                          
      On Test Set       : Accuracy Score  : 92%
                          Mathews Corr Coeff : 82.3
```


