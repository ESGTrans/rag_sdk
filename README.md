# rag_sdk
Simple RAG Development Kit

## Usage
- Installation
```
poetry add git+https://github.com/ESGTrans/rag_sdk.git
```

- Import to project
```python
from rag_sdk.core import RAGCore

```

## Quickstart

### Retrieval QA
```python
rag = RAGCore(vector_database_uri="xx.xx.xx.xx:6333", collection_list=["greenhousegas"])
response_object = rag.chat(query="台泥碳排減量做得如何?", chain_category="qa")

for chunk in response_object:
    print(chunk, end="", flash=True)

```

### Summarization
```python
rag = RAGCore(vector_database_uri="xx.xx.xx.xx:6333", collection_list=["greenhousegas"])
response_object = rag.chat(query="台泥溫室氣體排放情形", chain_category="summarize")

for chunk in response_object:
    print(chunk, end="", flash=True)

```

### Use Custom Prompt Template

#### 固定參數:
- `reference_documents`: 放置 query 的相似度搜尋結果

```python
custom_template = """請根據以下來源文章，用列點方式回答以下問題

來源文章: 
{reference_documents}

要回答的問題: {question}
"""

template_variables = {
    "question": "各間公司分別認列了哪些與綠建築相關的作為?"
}
retrieve_query = "綠建築"
custom_topk = 10

rag = RAGCore(vector_database_uri="xx.xx.xx.xx:6333", collection_list=["greenhousegas"])
response_object = rag.chat(query=retrieve_query, custom_topk=custom_topk, custom_prompt_template=custom_template, custom_prompt_template_variables=template_variables)

for chunk in response_object:
    print(chunk, end="", flash=True)

```

## Development

### Prompt Template

- Add a new category under `rag_sdk/prompt_templates/`
- Add a new prompt template with variables, ex: `bullet_points.py`

```python
custom_template = """請根據以下來源文章，用列點方式回答以下問題

來源文章: 
{reference_documents}

要回答的問題: {question}
```

- Use it in your project
```python
from rag_sdk.prompt_templates.qa.bullet_points import custom_template as custom_template_bullet_points
response_object = rag.chat(query=retrieve_query, custom_topk=custom_topk, custom_prompt_template=custom_template_bullet_points, custom_prompt_template_variables=template_variables)
```

### Other API Features

- Open a issue for new feature request
