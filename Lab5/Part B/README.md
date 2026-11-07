# Part B: Predict the Output — Python Dictionaries

## 📌 Overview

This section focuses on predicting the output of Python programs involving dictionaries. The objective is to understand dictionary behavior, copying, comprehensions, built-in methods, and common runtime errors.

---

## 🎯 Objectives

* Understand dictionary aliasing and shallow copying.
* Practice dictionary comprehensions.
* Learn how `setdefault()`, `pop()`, and `popitem()` work.
* Understand how Python handles equivalent dictionary keys.
* Identify errors caused by modifying a dictionary during iteration.
* Explain the output of each program.

---

## Q1. Dictionary Aliasing

### Code
```python
d = {"a": 1, "b": 2}
d2 = d
d2["c"] = 3
print(len(d))
Expected OutputPlaintext3
Explanationd2 = d makes both variables refer to the same dictionary. Adding "c" through d2 also modifies d, so its length becomes 3.Q2. Shallow CopyCodePythond = {"x": [1]}
e = d.copy()
e["x"].append(2)
print(d)
Expected OutputPlaintext{'x': [1, 2]}
ExplanationThe .copy() method creates a shallow copy. The inner list is shared between d and e, so appending 2 through e also changes the list inside d.Q3. Dictionary Comprehension with a ConditionCodePythonprint({k: v for k, v in zip("abc", range(3)) if v})
Expected OutputPlaintext{'b': 1, 'c': 2}
Explanationzip() pairs the letters with the numbers: a: 0, b: 1, and c: 2. The condition if v excludes the pair whose value is 0.Q4. The setdefault() MethodCodePythond = {"a": 1}
print(d.setdefault("a", 9), d.setdefault("b", 5), d)
Expected OutputPlaintext1 5 {'a': 1, 'b': 5}
Explanationsetdefault("a", 9) returns 1 because "a" already exists.setdefault("b", 5) inserts "b": 5 because the key is missing.The dictionary now contains both entries.Q5. Equivalent Dictionary KeysCodePythond = {1: "a", 1.0: "b", True: "c"}
print(d, len(d))
Expected OutputPlaintext{1: 'c'} 1
ExplanationIn Python, 1, 1.0, and True compare equal and have the same hash value. They therefore refer to the same dictionary key. Each assignment replaces the value associated with that key, so the final value is "c".Q6. Deleting a Key During IterationCodePythond = {"a": 1, "b": 2, "c": 3}
for k in d:
    if d[k] == 2:
        del d[k]
Expected ResultPlaintextRuntimeError: dictionary changed size during iteration
ExplanationDeleting a dictionary key while iterating directly over the dictionary changes its size. Python raises a RuntimeError when the iterator detects this structural change. A safe alternative is to iterate over list(d) or collect the keys to delete before removing them.Q7. The pop() and popitem() MethodsCodePythond = {"a": 1, "b": 2}
print(d.pop("z", None), d.popitem())
Expected OutputPlaintextNone ('b', 2)
Explanationpop("z", None) returns None because "z" does not exist and a default value was supplied.popitem() removes and returns the last inserted key-value pair. In this case, it returns ("b", 2).Q8. Dictionary Comprehension with Duplicate ValuesCodePythonprint({v: k for k, v in {"a": 1, "b": 1}.items()})
Expected OutputPlaintext{1: 'b'}
ExplanationThe comprehension reverses each key-value pair. Both original values are 1, so both entries attempt to use 1 as the new key. Dictionary keys must be unique, and the later value ("b") overwrites the earlier one ("a").📝 Summary of ConceptsQuestionConceptQ1AliasingQ2Shallow copyQ3Dictionary comprehensionQ4setdefault()Q5Equivalent dictionary keysQ6Modifying a dictionary during iterationQ7pop() and popitem()Q8Duplicate keys in a comprehension🧪 Practice InstructionsWrite down your predicted output before executing each snippet.Run each program using Python 3.x.Compare your prediction with the actual result.For each incorrect prediction, write one sentence explaining why.Revise the relevant dictionary concept.📚 Learning OutcomesAfter completing this section, students should be able to explain dictionary references, shallow copies, comprehensions, built-in dictionary methods, equivalent keys, and common runtime errors.Author: Bhavya DubeyLab: Python Dictionary — Part B
