# 10 - NLP & Chatbots

Three generations of chatbot, from hand-written rules to semantic similarity and voice.

| Folder | Approach |
|---|---|
| `rule_based/` | if/elif rules and regular expressions - no learning |
| `embedding_based/` | spaCy word vectors + cosine similarity to answer questions from a knowledge base |
| `voice_assistant/` | speech-to-text, text-to-speech, voice commands and a spoken Q&A assistant |

Each sub-folder has a `drafts/` folder (where applicable) with earlier versions of the scripts.

```bash
pip install spacy SpeechRecognition pyttsx3 PyAudio
python -m spacy download en_core_web_md
python embedding_based/spacy_embedding_qa_cosine_similarity.py
```
