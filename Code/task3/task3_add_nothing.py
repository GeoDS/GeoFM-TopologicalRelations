
# import openai
import openai
import csv

# filename = "0_answer_one_to_one_5.csv"
import sys

if len(sys.argv) < 2:
    print("Usage: python script.py filename")
    sys.exit(1)

filename = sys.argv[1]
headers = ["relation_predicate", "Response"]
client = openai.OpenAI(api_key='')
def run(description_word):
    response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": """
                    The given seven PREDICATES: contains, within, touches, crosses, disjoint, overlaps, equals. 
                    Given a sentence that include a vernacular spatial relation term: please give the corresponding PREDICATES. 
                    - Indicate spatial relation from A to B only.
                    - The vernacular spatial relation term should consider its typical meanings of the terms and the general geographical relationship it represent. Also pay attention to any other context that you can get from the sentence. 
                    - MAKE SURE the [PREDICATE] satisfies the the dimension requirements defined by DE-9IM and OGC given Geometry Type A and Geometry Type B.
                    - MAKE SURE that the output includes all plausible predicates and excludes any that are impossible or irrelevant in the given context. 
                    OUTPUT FORMAT: 
                        Analysis: Provide a detailed, professional, and coherent examination of the spatial relation from A to B.
                        Answer: A [PREDICATE1/PREDICATE2...] B. For example: A [overlaps/within] B"""},
                {"role": "user", "content": """given the sentence: A {} B""".format(description_word.split('/')[0])}
            ],
            temperature=0.1
    )
    # with open("0_answer_one_to_one.txt","a") as outputfile:
    #     line="""relation_predicate:{}, response:{}""".format(description_word,response.choices[0].message.content)
    #     outputfile.writelines(line)
    #     outputfile.writelines("\n")
    line = [description_word, response.choices[0].message.content]
    with open(filename, "a", newline="") as outputfile:  # newline="" 用于防止在写入行之间产生空行
        csvwriter = csv.writer(outputfile)
        if outputfile.tell() == 0:
            csvwriter.writerow(headers)
        csvwriter.writerow(line)

# descrption_list={"15 miles (24 km) from/disjoint",
# "abuts/touches",
# "adjacent to/touches",
# "at the city's western edge/overlaps",
# "at the confluence of/crosses",
# "at the mouth of/crosses",
# "based in/within",
# "close to/disjoint",
# "connect/crosses",
# "covers/contains",
# "direction /disjoint",
# "directly across/touches",
# "directly north of/touches",
# "extend north into/touches",
# "flows through/crosses",
# "historically home to/disjoint",
# "in close proximity to/disjoint",
# "include/contains",
# "lies on/overlaps",
# "Located in/within",
# "located on/overlaps",
# "located partly within /touches",
# "neighboring/touches",
# "not contiguous with/disjoint",
# "on/crosses",
# "on the southwest/touches",
# "part of/within",
# "part of the population in/overlaps",
# "partly extending into/overlaps",
# "separate/touches",
# "shares the land with /touches",
# "small portion in/touches",
# "suburb of/touches",
# "the headquarter of/contains",
# "the site of/contains",
# "upstream from/crosses",
# "western end of/touches",
# "within/touches"}

############for 1-1
# descrption_list={
#     "is adjacent to",
# "is bordered by/borders",
# "is bounded by",
# "connect C and",
# "is the county seat of",
# "has some distance from",
# "is an enclave of",
# "extend into",
# "is halfway between C and",
# "is near",
# "is the neighboring of",
# "has part of the population in",
# "adjoint",
# "is directly south of",
# "is in",
# "intersect with",
# "is located in",
# "is the location of",
# "is midway between C and",
# "share border with",
# "is surrounded by",
# "is upstream from"
# }


descrption_list={"is in",
"is located in",
"is bordered by",
"is the county seat of",
"is home to",
"borders",
"is surrounded by",
"is suburb of",
"has part of the population in",
"is adjacent to",
"is between C and",
"share border with",
"is part of",
"extend into",
"is the location of",
"is an enclave of",
"is within",
"is halfway between C and",
"is neighboring",
"connect C and",
"is near",
"is mostly in",
"is partly in",
"is bounded by",
"is along",
"surrounds",
"is on",
"includes",
"is midway between C and",
"on the shore of",
"is situated on"}

# descrption_list:{'is between C and','is suburb of','straddles','surrounds','along','near','is situated on','is on the shore of','is located on','is to the south of','is home to','just south of','is mostly in','is partly in','is within'}
for description_word in descrption_list:
    run(description_word)
    print(description_word)



