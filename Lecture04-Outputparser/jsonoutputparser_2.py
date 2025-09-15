from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

""" template = PromptTemplate(
    template='Give me the name, age and city of a fictional person \n (format_instruction)',
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
) """

template = PromptTemplate(
    template='Give me a JSON object with name, age and city of a fictional person. Example: {{"name": "John", "age": 30, "city": "New York"}}\n{format_instructions}',
    input_variables=[],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

prompt=template.format()
result=model.invoke(prompt)
#print(result)
final_result=parser.parse(result.content)
print(final_result)
print(type(final_result))
#print(final_result['name'])

#chain = template | model | parser

#result = chain.invoke({})

print(result)
