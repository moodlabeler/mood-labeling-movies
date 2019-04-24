from corpus_processing import Processor

pro = Processor()
pro.clear_lexicons()
pro.construct_lexicon("surprise")
pro.construct_lexicon("joy")
pro.construct_lexicon("fear")
pro.construct_lexicon("sadness")
print("Lexicon created")
