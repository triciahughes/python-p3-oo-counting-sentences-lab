#!/usr/bin/env python3

class MyString:
    pass

    def __init__(self, value = ""):
        self.value = value
        
    def get_value(self, value):
        self._value = value

    def set_value(self, value):
        if (type(value) == str):
            self._value = value
        else:
            print("The value must be a string.")
   
    def is_sentence(self):
        
        # self.sentence = sentence
        if self._value.endswith("."):
            return True
        else:
            return False

    def is_question(self):
        if self._value.endswith("?"):
            return True
        else:
            return False

    def is_exclamation(self):
        if self._value.endswith("!"):
            return True
        else:
            return False

    def count_sentences(self):
        # sum(char == "." and "?" and "!" for char in self._value)
        # periods = self._value.count(".")
        # exs = self._value.count("!")
        # ques = self._value.count("?")
        # totals = periods + ques
        new_sentence_replace = self._value.replace("?", ".")
        new_sentence_split = new_sentence_replace.split(".")
        for i in new_sentence_split:
            if i == '':
                new_sentence_split.remove(i)
                print(new_sentence_split)   
        else:
            return(len(new_sentence_split))
        print(new_sentence_split)
        pass

    value = property(get_value, set_value)
