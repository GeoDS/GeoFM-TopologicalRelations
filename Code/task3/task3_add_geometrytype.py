
import openai
import csv

import sys

# if len(sys.argv) < 2:
    # print("Usage: python script.py filename")
    # sys.exit(1)

# filename = sys.argv[1]
filename = "2_answer_object_geometry_type_3.csv"
headers = [ "relation_predicate","subject_geometry_type","object_geometry_type", "Response","actual_relation"]

client = openai.OpenAI(api_key='')
def run(relation_predicate,geometry_type_subject,geometry_type_object,relation):
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
                {"role": "user", "content": """given the sentence: A {} B and A is {}, B is {}""".format(relation_predicate, geometry_type_subject, geometry_type_object)}
            ],
            temperature=0.1
    )
    # with open("2_answer_object_geometry_type_2.txt","a") as outputfile:
    #     line="""relation_predicate:{}, object_geometry_type:{}, response:{}""".format(relation_predicate,geometry_type_object,response.choices[0].message.content)
    #     outputfile.writelines(line)
    #     outputfile.writelines("\n")
    line = [relation_predicate, geometry_type_subject, geometry_type_object, response.choices[0].message.content,relation]
    with open(filename, "a", newline="") as outputfile:  # newline="" 用于防止在写入行之间产生空行
        csvwriter = csv.writer(outputfile)
        if outputfile.tell() == 0:
            csvwriter.writerow(headers)
        csvwriter.writerow(line)

# descrption_list=[['along the border/touches', 'MultiPolygon'],
# ['along the border/within', 'Polygon'],
# ['along/crosses', 'LineString'],
# ['along/touches', 'Polygon'],
# ['bordering/overlaps', 'MultiPolygon'],
# ['bordering/touches', 'MultiPolygon'], ['bordering/touches', 'Polygon'], ['bordering/touches', 'LineString'],
# ['county seat of/overlaps', 'Polygon'],
# ['county seat of/within', 'Polygon'],
# ['is a certain direction from/disjoint', 'MultiPolygon'], ['is a certain direction from/disjoint', 'Polygon'],
# ['is a certain direction from/touches', 'Polygon'], ['is a certain direction from/touches', 'MultiPolygon'],
# ['is home to/contains', 'Point'], ['is home to/contains', 'Polygon'], ['is home to/contains', 'MultiPolygon'],
# ['is home to/disjoint', 'Polygon'], ['is home to/disjoint', 'MultiPolygon'],
# ['is home to/overlaps', 'MultiPolygon'], ['is home to/overlaps', 'Polygon'],
# ['in/overlaps', 'Polygon'],
# ['in/touches', 'Polygon'],
# ['in/within', 'Polygon'], ['in/within', 'MultiPolygon'],
# ['located in/touches', 'Polygon'],
# ['located in/within', 'Polygon'],
# ['mostly in/overlaps', 'Polygon'], ['mostly in/overlaps', 'MultiPolygon'],
# ['mostly in/touches', 'Polygon'], ['mostly in/touches', 'MultiPolygon'],
# ['near/disjoint', 'MultiPolygon'],
# ['near/touches', 'Polygon'],
# ['partly in/overlaps', 'Polygon'], ['partly in/overlaps', 'MultiPolygon'],
# ['partly in/touches', 'Polygon'], ['partly in/touches', 'MultiPolygon'],
# ['situated on/crosses', 'LineString'],
# ['situated on/overlaps', 'Polygon'],
# ['situated on/touches', 'Polygon'],
# ['straddling/crosses', 'LineString'],
# ['straddling/overlaps', 'Polygon'],
# ['surrounded by/overlaps', 'Polygon'],
# ['surrounded by/touches', 'Polygon'], ['surrounded by/touches', 'MultiPolygon'],
# ['surrounding/disjoint', 'MultiPolygon'],
# ['surrounding/overlaps', 'MultiPolygon']]

# descrption_list=[['across from','disjoint','Polygon','MultiPolygon'],
# ['across from','touches','Polygon','Polygon'],
# ['connect','crosses','LineString','MultiPolygon'],
# ['connect','crosses','Polygon','MultiPolygon'],
# ['connect','crosses','Polygon','Polygon'],
# ['distance from','disjoint','MultiPolygon','MultiPolygon'],
# ['distance from','disjoint','MultiPolygon','Polygon'],
# ['distance from','disjoint','Polygon','MultiPolygon'],
# ['distance from','disjoint','Polygon','Polygon'],
# ['enclave of','touches','MultiPolygon','Polygon'],
# ['enclave of','touches','Polygon','MultiPolygon'],
# ['extends into','overlaps','MultiPolygon','Polygon'],
# ['extends into','overlaps','Polygon','Polygon'],
# ['halfway between','disjoint','Polygon','MultiPolygon'],
# ['midway between','disjoint','Polygon','MultiPolygon'],
# ['midway between','disjoint','Polygon','Polygon'],
# ['nearby','disjoint','MultiPolygon','MultiPolygon'],
# ['nearby','disjoint','MultiPolygon','Polygon'],
# ['nearby','disjoint','Polygon','Polygon'],
# ['neighboring','touches','MultiPolygon','MultiPolygon'],
# ['neighboring','touches','MultiPolygon','Polygon'],
# ['neighboring','touches','Polygon','MultiPolygon'],
# ['neighboring','touches','Polygon','Polygon'],
# ['next to','disjoint','Polygon','MultiPolygon'],
# ['next to','disjoint','Polygon','Polygon'],
# ['next to','touches','MultiPolygon','Polygon'],
# ['on','crosses','Polygon','LineString'],
# ['on','disjoint','MultiPolygon','Polygon'],
# ['part of the population in','overlaps','MultiPolygon','Polygon'],
# ['part of the population in','overlaps','Polygon','Polygon'],
# ['separate from','disjoint','Polygon','LineString'],
# ['separate from','touches','Polygon','Polygon'],
# ['shares its borders with','touches','Polygon','Polygon'],
# ['situated on','crosses','MultiPolygon','LineString'],
# ['situated on','overlaps','MultiPolygon','Polygon'],
# ['situated on','overlaps','Polygon','Polygon'],
# ['straddle','crosses','Polygon','LineString'],
# ['straddle','overlaps','Polygon','Polygon'],
# ['surrounded by','touches','Polygon','MultiPolygon'],
# ['surrounded by','touches','Polygon','Polygon']]
# descrption_list=[['is between C and','polygon','polygon'],['is between C and','multipolygon','multipolygon'],['is suburb of','polygon','polygon'],['is suburb of','multipolygon','multipolygon'],['straddles','polygon','polygon'],['straddles','polygon','linestring'],['surrounds','polygon','polygon'],['surrounds','multipolygon','multipolygon'],['along','polygon','linestring'],['along','polygon','polygon'],['near','polygon','polygon'],['near','multipolygon','linestring'],['is situated on','polygon','linestring'],['is situated on','polygon','polygon'],['is on the shore of','polygon','polygon'],['is on the shore of','multipolygon','multipolygon'],['is located on','polygon','linestring'],['is located on','polygon','polygon'],['is to the south of','polygon','polygon'],['is to the south of','polygon','linestring'],['is home to','polygon','polygon'],['is home to','multipolygon','multipolygon'],['just south of','multipolygon','multipolygon'],['just south of','polygon','polygon'],['is mostly in','polygon','polygon'],['is mostly in','multipolygon','multipolygon'],['is partly in','multipolygon','multipolygon'],['is partly in','polygon','polygon'],['is within','multipolygon','multipolygon'],['is within','polygon','polygon']]

descrption_list=[['connect C and','2','crosses','geometry_type','LineString/MultiPolygon'],
['extend into','2','overlaps','geometry_type','Polygon/Polygon'],
['is bordered by','2','touches','geometry_type','Polygon/MultiPolygon'],
['is in','2','within','geometry_type','Polygon/MultiPolygon'],
['is neighboring','2','touches','geometry_type','Polygon/Polygon'],
['is on','2','crosses','geometry_type','Polygon/LineString'],
['is surrounded by','2','touches','geometry_type','Polygon/MultiPolygon'],
['is the county seat of','2','within','geometry_type','Polygon/Polygon']]

for description_word in descrption_list:
    geometry_type_subject = description_word[4].split('/')[0]
    geometry_type_object = description_word[4].split('/')[1]
    relation_predicate = description_word[0]
    relation=description_word[2]
    run(relation_predicate,geometry_type_subject,geometry_type_object,relation)
    print(description_word)