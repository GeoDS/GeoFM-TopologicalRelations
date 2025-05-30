# Foundation Models for Geospatial Reasoning
## Assessing Capabilities of LLMs in Understanding Geometries and Topological Spatial Relations

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
