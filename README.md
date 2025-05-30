# GeoFM-TopologicalRelations
## Foundation Models for Geospatial Reasoning: Assessing the Capabilities of Large Language Models in Understanding Geometries and Topological Spatial Relations

## Abstract

Large language models (LLMs) have demonstrated capabilities for the understanding of geospatial semantics. However, applying such pre-trained text-based models directly to geospatial datasets remains challenging due to their limited ability to represent and reason with geographical entities, specifically vector-based geometries and natural language descriptions of complex spatial relations. To address these issues, we investigate the extent to which a well-known-text (WKT) representation of geometries and their spatial relations (e.g., topological predicates) are preserved during spatial reasoning when the geospatial vector data in GIS are passed to LLMs including GPT-3.5-turbo, GPT-4, and DeepSeek-R1. Our workflow employs three distinct approaches to complete the spatial reasoning tasks for comparison, i.e., geometry embedding-based, prompt engineering-based, and everyday language-based evaluation. Our experiment results demonstrate that both the embedding-based and prompt engineering-based approaches to geospatial question-answering tasks with GPT models can achieve an accuracy of over 0.6 on average for the identification of topological spatial relations between two geometries. Among the evaluated models, GPT-4 with few-shot prompting achieved the highest performance with over 0.66 accuracy on topological spatial relation inference. Additionally, GPT-based reasoner is capable of properly comprehending inverse topological spatial relations and including an LLM-generated geometry can enhance the effectiveness for geographic entity retrieval. GPT-4 also exhibits the ability to translate certain vernacular descriptions about places into formal topological relations, and adding the geometry-type or place-type context in prompts may improve inference accuracy, but it varies by instance. The performance of these spatial reasoning tasks unveils the strengths and limitations of the current LLMs in the processing and comprehension of geospatial vector data and offers valuable insights for the refinement of LLMs with geographical knowledge towards the development of geo-foundation models capable of geospatial reasoning.


## Workflow

![title](GeoFMTopo-Framework.jpg)

## Reference
If you find our code or ideas useful for your research, please cite our paper:

*Ji, Y., Gao, S., Nie, Y., Majić, I., & Janowicz, K. (2025). [Foundation Models for Geospatial Reasoning: Assessing Capabilities of Large Language Models in Understanding Geometries and Topological Spatial Relations](https://arxiv.org/pdf/2505.17136). International Journal of Geographical Information Science, 39 (X), 1-33.*

```
@article{ji2025foundation,
  title={Foundation Models for Geospatial Reasoning: Assessing Capabilities of Large Language Models in Understanding Geometries and Topological Spatial Relations},
  author={Ji, Yuhan and Gao, Song and Nie, Ying and Majic, Ivan and Janowicz, Krzysztof},
  journal={International Journal of Geographical Information Science},
  volume={39},
  number={x},
  pages={1--33},
  year={2025},
  publisher={Taylor \& Francis}
}
```


## Code usage

### Table of Contents

1. [Data Preparation](#data-preparation)
2. [Task 1](#task-1)
    - [Experiment](#task-1-experiment)
    - [Result Analysis](#task-1-result-analysis)
3. [Task 2](#task-2)
    - [Experiment](#task-2-experiment)
    - [Result Analysis](#task-2-result-analysis)
4. [Task 3](#task-3)
    - [Experiment](#task-3-experiment)
    - [Result Analysis](#task-3-result-analysis)

### 1. Data Preparation

#### Task 1 and Task 2

- **extract_triplet**: Extract the topological relations between the spatial entities of road networks, POIs, tax parcels, and census block groups.
- **embedding-api**: Convert WKT of geometries into embeddings using sentence embedding models.

#### Task 3

- **step 1-3**: Follow the steps to obtain the abstract of places within the study areas, and extract the everyday description of the spatial relations.
- **step 4**: Query the data from OpenStreetMap and use the geometries to compute the formal topological spatial relations.

### 2. Task 1

#### Experiment

- **task1-RF**: Given the triplets, use the concatenation of the embeddings of the subject and object as the input, (geometry type A, predicate, geometry type B) as the label, for a random forest classifier.
- **task1-GPT-3.5/4/DeepSeek**: Use different prompt engineering strategies to obtain the response from GPT-3.5/GPT-4/DeepSeek for the topological relation qualification.

#### Result Analysis

- **task1-result**: Compute the evaluation metrics of task 1. Generate the confusion matrix for each pair of geometry types.

### 3. Task 2

#### Experiment

- **task2-subject**: Semantic search of the embeddings of (predicate + WKT(B)).
- **task2-object**: Semantic search of the embeddings of (WKT(A) + predicate).

#### Result Analysis

- **task2-result**: Compute the evaluation metrics of task 2. Generate the confusion matrix for each pair of geometry types.

### 4. Task 3

#### Experiment

- **task3_process_placename**: Process the one-to-one conversion between the everyday description and the formal predicate on context.
- **task3_add_nothing/geometrytype/placetype/placename**: Add the context to the prompts and generate the response from GPT-4.

#### Result Analysis

- **task3_result-analysis**: Compute the evaluation metrics and list the performance on each sample.
