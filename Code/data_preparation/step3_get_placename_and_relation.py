# import openai
from openai import OpenAI



def get_placename_and_relation(abstract):
    # response = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     messages=[
    #         {"role": "user", "content": """
    #          for each sentence, could you find out if the sentence fulfill the requirement: placename_1 [vernacular spatial relationship] placename_2. if does, then return as the following format: placename_1,vernacular spatial relationship,placename_2
    #          for example: San Diego is in the south of Los Angeles. So you should output San Diego,south of,Los Angeles. """},
    #         {"role": "assistant", "content": f"""{abstract}"""},
    #     ],
    #     temperature=0.2
    # )
    client = OpenAI(
        # This is the default and can be omitted
        api_key='',
    )

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": """for each sentence, could you find out if the sentence fulfill the requirement: placename_1 [geographic relation] placename_2. if does, then return as the following format: "original sentence",placename_1,geographic relation,placename_2. if doesn't, then return as the following format: "original sentence",none.
                               pay attention that: sometimes placename_1 or placename_2 might be somewhere else in the sentence instead of strictly fulfill the format requirement.
                               also pay attention that: I only need the information for current time isntead of historical.""",
            },
            {
                "role": "assistant", 
                "content": f"""{abstract}"""
            }
        ],
        model="gpt-4o",
    )

    # Extract and format the relevant part of the response
    # output = response['choices'][0]['message']['content']
    output=response.choices[0].message.content
    return output
# output_lines = output.split('\n')

# print(output)
# # Initialize an empty list to store geo relations
# geo_relations = []

# # Iterate through the lines and extract relations
# for line in output_lines:
#     parts = line.split(" - ")
#     if len(parts) == 2:
#         geo_relations.append(parts[0].strip() + " - " + parts[1].strip())

# # Join the relations and print them
# formatted_output = "\n".join(geo_relations)
# print(formatted_output)



with open("data_for_tx/text_description_tx.txt",'r') as readfile:
    text_documents=readfile.readlines()
i=0
sum=0
with open("data_for_tx/placename_and_relation_tx_2.txt",'a') as outputfile: 
    for text_document in text_documents:
        result=get_placename_and_relation(text_document)
        outputfile.write(str(i)+"\n"+result + "\n\n\n")
        num=result.strip().count("\n")+1
        print(str(i)+":"+str(num))
        i=i+1
        sum=sum+num
print(sum)