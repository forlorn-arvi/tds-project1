# I have doubt in Q10

### Post 1 (ID: 592777)

I have doubt in question 10 to convert pdf to markdown  
I am not getting correct markdown  
[@pds_staff](/u/pds_staff)


---

### Post 2 (ID: 593235)

Try using the pymupdf4llm Library  
pip install pymupdf4llm

import pymupdf4llm  
md_text = pymupdf4llm.to_markdown(“input.pdf”)

import pathlib  
pathlib.Path(“output.md”).write_bytes(md_text.encode())

import pymupdf4llm  
llama_reader = pymupdf4llm.LlamaMarkdownReader()  
llama_docs = llama_reader.load_data(“input.pdf”)

